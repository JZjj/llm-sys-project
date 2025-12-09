"""
Module for LLM-based code security evaluation.
"""

import json
from openai import OpenAI
from utils import LLMIssue, LLMEvalResult, CodeSample

MODEL = "gpt-4.1-mini"
client = None


# ---------------------------------------------------------
# Initialization
# ---------------------------------------------------------

def ensure_llm_ready():
    """
    Ensures OpenAI client is ready before running evaluation.
    """
    global client
    if client is None:
        try:
            client = OpenAI()
        except Exception:
            raise RuntimeError("OpenAI client not initialized. Set OPENAI_API_KEY.")


# ---------------------------------------------------------
# Prompt Construction
# ---------------------------------------------------------

def build_prompt(sample: CodeSample) -> str:
    """
    Build the evaluation prompt for a single code sample.
    """
    return f"""
Evaluate the security of the following {sample.language} code.

Return STRICT JSON:
{{
  "security_score": 1-5,
  "vulnerable": true/false,
  "issues": [
    {{
      "type": "...",
      "severity": "low|medium|high|critical",
      "description": "..."
    }}
  ]
}}

CODE (id={sample.id}, source={sample.source_type}):
```{sample.language}
{sample.code}

"""

def run_llm_eval(sample: CodeSample) -> LLMEvalResult:
"""
Runs LLM-based security evaluation on a single code sample.

Returns:
    LLMEvalResult with:
        - security_score: int (1–5)
        - vulnerable: bool
        - issues: list of LLMIssue
"""
ensure_llm_ready()

prompt = build_prompt(sample)

# ---- Query the LLM ----
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.0,
)

raw = response.choices[0].message["content"]

# ---- Parse JSON strictly ----
try:
    data = json.loads(raw)
except json.JSONDecodeError:
    # fallback: extract only the JSON portion
    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        data = json.loads(raw[start:end])
    except Exception:
        raise RuntimeError(f"LLM returned invalid JSON:\n\n{raw}")

# ---- Convert issues list ----
issues = []
for item in data.get("issues", []):
    issues.append(
        LLMIssue(
            type=item.get("type", ""),
            severity=item.get("severity", "low"),
            description=item.get("description", ""),
        )
    )

# ---- Return structured evaluation result ----
return LLMEvalResult(
    security_score=int(data.get("security_score", 1)),
    vulnerable=bool(data.get("vulnerable", False)),
    issues=issues,
)
