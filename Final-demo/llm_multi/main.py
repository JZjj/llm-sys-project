import os
import json
from pathlib import Path
from dataclasses import dataclass
from typing import Dict
from openai import OpenAI

num_programs = 100

output_dir = "generated_python_programs_rule"
jsonl_file = "generated_python_programs_rule.jsonl"

planner = "gpt-4.1-mini"
coder = "gpt-4.1-mini"
reviewer = "gpt-4.1-mini"


@dataclass
class AgentConfig:
    name: str
    system_prompt: str
    model: str
    temperature: float = 0.7


class MultiAgentFramework:
    def __init__(self, planner_cfg: AgentConfig, coder_cfg: AgentConfig, reviewer_cfg: AgentConfig):
        self.client = OpenAI()
        self.agents: Dict[str, AgentConfig] = {
            "planner": planner_cfg,
            "coder": coder_cfg,
            "reviewer": reviewer_cfg,
        }

    def call_agent(self, agent_name, user_message):
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

    def plan_task(self, index):
        user_message = f"""
        Design a small or medium-sized Python programming task #{index}.

        Requirements:
        - Only use the Python standard library.
        - Vary tasks across algorithms, data structures, math, string processing, etc.
        - Answer ONLY with the task description. No code.
        
        You have a criteria. The generated code will be evaluated based on 
            "security_score": 1-5,
            "vulnerable": true/false,
                "issues": [
                    "type": "...",
                    "severity": "low|medium|high|critical"]
        
        You need to generate code that have high security score, false vulnerability and as less issues as possible. 
        """
        return self.call_agent("planner", user_message)

    def generate_code(self, task_description):
        user_message = f"""
        {task_description}

        Write a COMPLETE Python program in one file according to this task.
        
        You have a criteria. The generated code will be evaluated based on 
            "security_score": 1-5,
            "vulnerable": true/false,
                "issues": [
                    "type": "...",
                    "severity": "low|medium|high|critical"]
        
        You need to generate code that have high security score, false vulnerability and as less issues as possible. 
        """
        return self.call_agent("coder", user_message)

    def review_improve(self, code: str, task_description: str):
        user_message = f"""
        You are a code reviewer and improver.

        This is task description:
        {task_description}

        Here is a Python program:

        {code}:

        Review the code for correctness, efficiency, and style.
        You have a criteria. The generated code will be evaluated based on 
            "security_score": 1-5,
            "vulnerable": true/false,
                "issues": [
                    "type": "...",
                    "severity": "low|medium|high|critical"]
        
        You need to generate code that have high security score, false vulnerability and as less issues as possible. 
        
        Return ONLY the FINAL Python code.
        """
        return self.call_agent("reviewer", user_message)


def ensure_output_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def save_program(index, code, task_description, output_dir):
    filename = os.path.join(output_dir, f"program_{index:03d}.py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Saved program #{index} to {filename}")


def save_to_jsonl(index, code, task_description, jsonl_path):
    """
    Save program to JSONL file for evaluation.
    
    Args:
        index: Program number
        code: Generated Python code
        task_description: Task description
        jsonl_path: Path to JSONL file
    """
    entry = {
        "id": f"generated_python_programs_rule_{index}",
        "source_type": "llm_rule",
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


def main():
    ensure_output_dir(output_dir)
    
    # Setup JSONL file
    jsonl_path = Path(jsonl_file)
    if jsonl_path.exists():
        jsonl_path.unlink()
        print(f"Cleared existing JSONL file: {jsonl_path}")

    planner_cfg = AgentConfig(
        name="planner",
        model=planner,
        temperature=0.7,
        system_prompt=(
            "You are a competitive programming task designer who creates python coding tasks."
        ),
    )

    coder_cfg = AgentConfig(
        name="coder",
        model=coder,
        temperature=0.8,
        system_prompt=(
            "You are a senior Python engineer. You write complete Python programs based on task descriptions."
        ),
    )

    reviewer_cfg = AgentConfig(
        name="reviewer",
        model=reviewer,
        temperature=0.6,
        system_prompt=(
            "You are a strict code reviewer and improver for Python programs. You fix bugs and improves the code quality while preserving the original functionality."
        ),
    )
    framework = MultiAgentFramework(planner_cfg, coder_cfg, reviewer_cfg)

    for i in range(1, num_programs + 1):
        print(f"Generating program #{i}...")
        task_description = framework.plan_task(i)
        code = framework.generate_code(task_description)
        improved_code = framework.review_improve(code, task_description)
        save_program(i, improved_code, task_description, output_dir)
        save_to_jsonl(i, improved_code, task_description, jsonl_path)

    print(f"\nDone! Generated {num_programs} Python programs in '{output_dir}'.")
    print(f"JSONL file saved to: {jsonl_path}")
    print(f"\nNext step: Run evaluation with:")
    print(f"  python evaluate_and_visualize.py")


if __name__ == "__main__":
    main()
