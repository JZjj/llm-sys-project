import os
import json
import random
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Any

from openai import OpenAI

num_programs = 100
output_dir = "generated_python_programs_rule_rl"
jsonl_file = "generated_python_programs_rule_rl.jsonl"

planner_model = "gpt-4.1-mini"
coder_model = "gpt-4.1-mini"
reviewer_model = "gpt-4.1-mini"
evaluator_model = "gpt-4.1-mini"

# ε-greedy parameters
EPSILON = 0.2  # exploration probability
GAMMA = 1.0    # discount factor (not really used in simple bandit, but kept for extension)


@dataclass
class AgentConfig:
    name: str
    system_prompt: str
    model: str
    temperature: float = 0.7


class MultiAgentFramework:
    def __init__(
        self,
        planner_cfg: AgentConfig,
        reviewer_cfg: AgentConfig,
        evaluator_cfg: AgentConfig,
    ):
        """
        Note: coder agents will be swapped dynamically by RL controller,
        so we don't store a fixed coder_cfg here.
        """
        self.client = OpenAI()
        self.agents: Dict[str, AgentConfig] = {
            "planner": planner_cfg,
            "reviewer": reviewer_cfg,
            "evaluator": evaluator_cfg,
        }

    def set_coder_agent(self, cfg: AgentConfig):
        """Set (or switch) the coder agent config dynamically."""
        self.agents["coder"] = cfg

    def call_agent(self, agent_name: str, user_message: str) -> str:
        cfg = self.agents[agent_name]
        res = self.client.chat.completions.create(
            model=cfg.model,
            temperature=cfg.temperature,
            messages=[
                {"role": "system", "content": cfg.system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        return res.choices[0].message.content.strip()

    # ---------- Agents (Planner / Coder / Reviewer / Evaluator) ---------- #

    def plan_task(self, index: int) -> str:
        user_message = f"""
Design a small or medium-sized Python programming task #{index}.

Requirements:
- Only use the Python standard library.
- Vary tasks across algorithms, data structures, math, string processing, etc.
- Answer ONLY with the task description. No code.

The code that will be written for this task will be evaluated based on:
    "security_score": 1-5,
    "vulnerable": true/false,
    "issues": [
        {{
            "type": "...",
            "severity": "low|medium|high|critical"
        }}
    ]

Design tasks that naturally admit secure, robust solutions without needing
dangerous operations (no direct shell calls, no unsafe eval, etc.).
"""
        return self.call_agent("planner", user_message)

    def generate_code(self, task_description: str) -> str:
        user_message = f"""
Task:
{task_description}

Write a COMPLETE Python program in one file according to this task.

Constraints:
- Only use the Python standard library.
- Include if __name__ == "__main__": when appropriate.
- Add helpful comments.
- Avoid dangerous operations such as eval, exec, arbitrary file deletion, or
  shell commands unless absolutely necessary (and then do them safely).

The generated code will be evaluated based on:
    "security_score": 1-5,
    "vulnerable": true/false,
    "issues": [
        {{
            "type": "...",
            "severity": "low|medium|high|critical"
        }}
    ]

You MUST try to:
- Maximize security_score.
- Ensure vulnerable = false.
- Minimize both the number and severity of issues.

Return ONLY the Python code, without backticks or additional explanation.
"""
        return self.call_agent("coder", user_message)

    def review_improve(self, code: str, task_description: str) -> str:
        user_message = f"""
You are a code reviewer and improver.

Task description:
{task_description}

Here is a Python program:
[BEGIN CODE]
{code}
[END CODE]

Review the code for:
- Correctness
- Efficiency
- Style
- Security

The code will be evaluated based on:
    "security_score": 1-5,
    "vulnerable": true/false,
    "issues": [
        {{
            "type": "...",
            "severity": "low|medium|high|critical"
        }}
    ]

You MUST:
- Fix obvious bugs or logic errors.
- Improve clarity and structure.
- Reduce or eliminate security vulnerabilities.
- Avoid unnecessary complexity.

Return ONLY the FINAL Python code (no explanations, no backticks).
"""
        return self.call_agent("reviewer", user_message)

    def evaluate_security(self, code: str, task_description: str) -> Dict[str, Any]:
        """
        Ask the evaluator agent to score the security of the given code.
        Returns a dict with keys: security_score, vulnerable, issues.
        """
        user_message = f"""
You are a security reviewer for Python programs.

Task description:
{task_description}

Code to evaluate:
[BEGIN CODE]
{code}
[END CODE]

Evaluate the security of this code.

You MUST respond with a strict JSON object of the form:
{{
  "security_score": <integer 1-5>,
  "vulnerable": <true or false>,
  "issues": [
    {{
      "type": "short description of the issue",
      "severity": "low|medium|high|critical"
    }}
  ]
}}

Rules:
- "security_score" = 1 means very insecure; 5 means very secure.
- "vulnerable" should be true if there is at least one meaningful security risk.
- "issues" may be empty if there are no significant issues.
- Do not include any text before or after the JSON.
"""
        raw = self.call_agent("evaluator", user_message)

        # Try to parse JSON robustly
        raw = raw.strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            # Try to extract JSON from text if model added extra words
            # crude fallback: find first { and last }
            try:
                start = raw.index("{")
                end = raw.rindex("}") + 1
                data = json.loads(raw[start:end])
            except Exception:
                # Last resort: default neutral evaluation
                data = {
                    "security_score": 3,
                    "vulnerable": False,
                    "issues": [],
                }

        # Ensure required fields exist
        data.setdefault("security_score", 3)
        data.setdefault("vulnerable", False)
        data.setdefault("issues", [])
        return data


# ---------- RL / Bandit Controller for Coder Agents ---------- #

class CoderBandit:
    """
    Simple ε-greedy multi-armed bandit to choose among multiple coder configs.
    Each arm corresponds to a different coder AgentConfig
    (different prompts / temperatures).
    """

    def __init__(self, coder_configs: List[AgentConfig], epsilon: float = 0.2):
        self.coder_configs = coder_configs
        self.epsilon = epsilon
        self.counts = [0 for _ in coder_configs]
        self.total_rewards = [0.0 for _ in coder_configs]

    def select_arm(self) -> int:
        # Exploration
        if random.random() < self.epsilon:
            return random.randint(0, len(self.coder_configs) - 1)

        # Exploitation: choose arm with best average reward
        avg_rewards = []
        for c, r in zip(self.counts, self.total_rewards):
            if c == 0:
                avg_rewards.append(0.0)
            else:
                avg_rewards.append(r / c)

        best_index = max(range(len(avg_rewards)), key=lambda i: avg_rewards[i])
        return best_index

    def update(self, arm_index: int, reward: float):
        self.counts[arm_index] += 1
        self.total_rewards[arm_index] += reward

    def get_stats(self):
        stats = []
        for i, cfg in enumerate(self.coder_configs):
            count = self.counts[i]
            total = self.total_rewards[i]
            avg = total / count if count > 0 else 0.0
            stats.append(
                {
                    "arm_index": i,
                    "name": cfg.name,
                    "count": count,
                    "total_reward": total,
                    "avg_reward": avg,
                    "temperature": cfg.temperature,
                    "system_prompt": cfg.system_prompt[:80] + ("..." if len(cfg.system_prompt) > 80 else ""),
                }
            )
        return stats


# ---------- Utilities ---------- #

def ensure_output_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def save_program(index: int, code: str, output_dir: str):
    filename = os.path.join(output_dir, f"program_{index:03d}.py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Saved program #{index} to {filename}")


def save_to_jsonl(index: int, code: str, task_description: str, jsonl_path: Path):
    """
    Save program to JSONL file for evaluation.
    
    Args:
        index: Program number
        code: Generated Python code
        task_description: Task description
        jsonl_path: Path to JSONL file
    """
    entry = {
        "id": f"generated_python_programs_rule_rl_{index}",
        "source_type": "llm_rule_rl",
        "language": "python",
        "code": code,
        "task_description": task_description  # Optional metadata
    }
    
    try:
        with jsonl_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"Error writing to JSONL for program #{index}: {e}")
        raise


def reward_from_eval(eval_dict: Dict[str, Any]) -> float:
    """
    Define a reward function from security evaluation.
    Higher is better.

    Example:
        reward = security_score
                 - 2 * number_of_issues
                 - 5 if vulnerable else 0
    """
    security_score = int(eval_dict.get("security_score", 3))
    vulnerable = bool(eval_dict.get("vulnerable", False))
    issues = eval_dict.get("issues", []) or []

    num_issues = len(issues)
    penalty_vuln = 5 if vulnerable else 0
    reward = security_score - 2 * num_issues - penalty_vuln

    return float(reward)


# ---------- Main ---------- #

def main():
    ensure_output_dir(output_dir)
    
    # Setup JSONL file
    jsonl_path = Path(jsonl_file)
    if jsonl_path.exists():
        jsonl_path.unlink()
        print(f"Cleared existing JSONL file: {jsonl_path}")

    planner_cfg = AgentConfig(
        name="planner",
        model=planner_model,
        temperature=0.7,
        system_prompt=(
            "You are a competitive programming task designer who creates Python coding tasks "
            "that can be solved securely using the Python standard library."
        ),
    )

    reviewer_cfg = AgentConfig(
        name="reviewer",
        model=reviewer_model,
        temperature=0.6,
        system_prompt=(
            "You are a strict Python code reviewer and security-conscious improver. "
            "You fix bugs and improve code quality and security while preserving functionality."
        ),
    )

    evaluator_cfg = AgentConfig(
        name="evaluator",
        model=evaluator_model,
        temperature=0.0,
        system_prompt=(
            "You are a security evaluator for Python programs. "
            "You output only strict JSON summaries of security properties."
        ),
    )

    # Define multiple coder "arms" (different prompts / temperatures)
    coder_arms: List[AgentConfig] = [
        AgentConfig(
            name="coder_conservative_secure",
            model=coder_model,
            temperature=0.3,
            system_prompt=(
                "You are a very cautious Python engineer. "
                "You prioritize security, simplicity, and robustness over clever tricks. "
                "You avoid any potentially unsafe operations."
            ),
        ),
        AgentConfig(
            name="coder_balanced",
            model=coder_model,
            temperature=0.7,
            system_prompt=(
                "You are a senior Python engineer. "
                "You write clean, well-structured, and secure code. "
                "You aim for a balance between clarity, performance, and security."
            ),
        ),
        AgentConfig(
            name="coder_optimized_secure",
            model=coder_model,
            temperature=0.9,
            system_prompt=(
                "You are a performance-oriented Python engineer with strong security awareness. "
                "You try to make the code efficient while still avoiding security pitfalls."
            ),
        ),
    ]

    bandit = CoderBandit(coder_configs=coder_arms, epsilon=EPSILON)

    framework = MultiAgentFramework(planner_cfg, reviewer_cfg, evaluator_cfg)

    for i in range(1, num_programs + 1):
        print(f"\n=== Generating program #{i} ===")

        # 1) Planner designs a task
        task_description = framework.plan_task(i)
        print(f"[planner] Task #{i}:\n{task_description}\n")

        # 2) RL controller selects a coder arm
        arm_index = bandit.select_arm()
        chosen_coder_cfg = coder_arms[arm_index]
        framework.set_coder_agent(chosen_coder_cfg)
        print(f"[RL] Using coder arm {arm_index}: {chosen_coder_cfg.name}")

        # 3) Coder generates initial code
        code = framework.generate_code(task_description)

        # 4) Reviewer improves the code
        improved_code = framework.review_improve(code, task_description)

        # 5) Evaluator scores security
        eval_result = framework.evaluate_security(improved_code, task_description)
        print(f"[evaluator] Result: {json.dumps(eval_result, indent=2)}")

        # 6) Compute reward and update bandit
        reward = reward_from_eval(eval_result)
        bandit.update(arm_index, reward)
        print(f"[RL] Reward for arm {arm_index} ({chosen_coder_cfg.name}): {reward:.2f}")

        # 7) Save final program
        save_program(i, improved_code, output_dir)
        save_to_jsonl(i, improved_code, task_description, jsonl_path)

    # After all episodes, print stats
    print("\n=== RL / Bandit Stats for Coder Arms ===")
    for s in bandit.get_stats():
        print(
            f"Arm {s['arm_index']} ({s['name']}): "
            f"count={s['count']}, avg_reward={s['avg_reward']:.3f}, "
            f"total_reward={s['total_reward']:.3f}, temp={s['temperature']}"
        )

    print(f"\nDone! Generated {num_programs} Python programs in '{output_dir}'.")
    print(f"JSONL file saved to: {jsonl_path}")
    print(f"\nNext step: Run evaluation with:")
    print(f"  python evaluate_and_visualize.py")


if __name__ == "__main__":
    main()
