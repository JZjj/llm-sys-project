#!/usr/bin/env python3
"""
Multi-model code generation script.

- Sends the same code task to multiple models
- Collects their answers
- Prints all outputs side-by-side
- (Optional) simple "ensemble" that picks the longest answer as final

Usage:
    export OPENAI_API_KEY="sk-..."
    python multi_model_code_gen.py
"""

import os
from typing import List, Dict

from openai import OpenAI

# ----------------------------
# Configuration
# ----------------------------
# List of models you want to use
# You can change these to whatever models you have access to.
MODELS = [
    "gpt-4.1-mini",
    "gpt-4.1",
]

SYSTEM_PROMPT = """You are an expert software engineer.
Generate clean, well-structured code with comments and no extra explanations unless asked."""
# Example user task; you can replace this dynamically (e.g., input()).
DEFAULT_TASK = "Write a Python function that takes a list of integers and returns the list sorted using merge sort."


def get_client() -> OpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Please set OPENAI_API_KEY in your environment.")
    return OpenAI(api_key=api_key)


def build_user_prompt(task: str) -> str:
    return (
        "You are asked to WRITE CODE ONLY.\n"
        "Task:\n"
        f"{task}\n\n"
        "Output requirements:\n"
        "- Return ONLY code inside one Markdown Python code block.\n"
        "- Do not add prose explanation outside the code block.\n"
    )


def call_model(client: OpenAI, model: str, task: str) -> str:
    """Call one LLM model to generate code for the given task."""
    user_prompt = build_user_prompt(task)
    resp = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        max_output_tokens=800,
        temperature=0.2,
    )
    # Extract the text
    content = resp.output[0].content[0].text
    return content


def run_multi_model(task: str) -> Dict[str, str]:
    """Run the same task across multiple models and return their outputs."""
    client = get_client()
    outputs = {}
    for m in MODELS:
        print(f"\n=== Calling model: {m} ===")
        try:
            out = call_model(client, m, task)
            outputs[m] = out
        except Exception as e:
            outputs[m] = f"ERROR: {e}"
    return outputs


def pick_best_output(outputs: Dict[str, str]) -> str:
    """
    Very simple "ensemble":
    - Pick the output with the largest length (rough heuristic).
    You can replace this with more advanced evaluation later (tests, static analysis, etc.).
    """
    best_model = None
    best_text = None

    for model, text in outputs.items():
        if text.startswith("ERROR:"):
            continue
        if best_text is None or len(text) > len(best_text):
            best_text = text
            best_model = model

    if best_text is None:
        return "No valid outputs (all models errored)."

    banner = f"# Final selection from model: {best_model}\n\n"
    return banner + best_text


def main():
    # 1) Get a task from user or use default
    print("Multi-model code generation\n")
    user_task = input(
        f"Enter your code generation task (or press Enter to use default):\n"
        f"Default: {DEFAULT_TASK}\n> "
    ).strip()
    if not user_task:
        user_task = DEFAULT_TASK

    # 2) Call multiple models
    outputs = run_multi_model(user_task)

    # 3) Print each model's answer
    print("\n\n================ ALL MODEL OUTPUTS ================\n")
    for model, text in outputs.items():
        print(f"\n---------- Model: {model} ----------\n")
        print(text)
        print("\n------------------------------------\n")

    # 4) Simple automatic selection
    final_code = pick_best_output(outputs)

    print("\n\n================ FINAL SELECTED CODE ================\n")
    print(final_code)
    print("\n=====================================================\n")


if __name__ == "__main__":
    main()
