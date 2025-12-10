"""
Module for LLM-based code security evaluation.
"""

import json
from openai import OpenAI
from utils import LLMIssue, LLMEvalResult, CodeSample

MODEL = "gpt-4.1-mini"
client = None


def ensure_llm_ready():
    global client
    if client is None:
        try:
            client = OpenAI()
        except Exception:
            raise RuntimeError("OpenAI client not initialized. Set OPENAI_API_KEY.")


def build_prompt(sample: CodeSample) -> str:
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