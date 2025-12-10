"""
Code Generation Script for Single Model Evaluation

This script generates 100 Python code samples using a single LLM model.
The generated code is saved both as individual Python files and as a JSONL file
for evaluation.

Author: LLM Systems Project
Date: 2024
License: MIT
"""

import os
import json
import logging
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from openai import OpenAI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
NUM_PROGRAMS = 100
OUTPUT_DIR = "generated_python_programs"
JSONL_FILE = "generated_python_programs.jsonl"
MODEL = "gpt-4.1-mini"

# Initialize OpenAI client
client: Optional[OpenAI] = None


@dataclass
class GenerationConfig:
    """Configuration for code generation."""
    model: str = MODEL
    temperature: float = 0.7
    system_prompt: str = "You are a senior Python engineer who writes secure, well-structured Python programs."


def ensure_llm_ready() -> None:
    """Ensure OpenAI client is initialized."""
    global client
    if client is None:
        try:
            client = OpenAI()
            logger.info("OpenAI client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise RuntimeError(
                "OpenAI client not initialized. Set OPENAI_API_KEY environment variable."
            )


def generate_task_description(index: int) -> str:
    """
    Generate a task description for code generation.
    
    Args:
        index: Task number (1-100)
        
    Returns:
        Task description string
    """
    prompt = f"""
Design a small or medium-sized Python programming task #{index}.

Requirements:
- Only use the Python standard library (no external dependencies)
- Vary tasks across algorithms, data structures, math, string processing, file I/O, etc.
- Make the task clear and well-defined
- Answer ONLY with the task description. No code, no explanations.

Examples of good tasks:
- "Write a function to find all anagrams of a given word in a list"
- "Implement a function to calculate the factorial of a number using recursion"
- "Create a program to count word frequencies in a text file"
"""
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are a competitive programming task designer."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Error generating task description for task #{index}: {e}")
        raise


def generate_code(task_description: str, index: int) -> str:
    """
    Generate Python code for a given task description.
    
    Args:
        task_description: Description of the programming task
        index: Task number
        
    Returns:
        Generated Python code
    """
    prompt = f"""
{task_description}

Write a COMPLETE Python program in one file according to this task.

Requirements:
- Write secure, well-structured code
- Include proper error handling where appropriate
- Add comments for clarity
- Include a main() function with example usage if applicable
- Use only Python standard library
- Make the code production-ready

Return ONLY the Python code, no explanations or markdown formatting.
"""
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            temperature=0.8,
            messages=[
                {"role": "system", "content": "You are a senior Python engineer who writes secure, well-structured code."},
                {"role": "user", "content": prompt},
            ],
        )
        code = response.choices[0].message.content.strip()
        
        # Remove markdown code blocks if present
        if code.startswith("```python"):
            code = code[9:]
        elif code.startswith("```"):
            code = code[3:]
        if code.endswith("```"):
            code = code[:-3]
        
        return code.strip()
    except Exception as e:
        logger.error(f"Error generating code for task #{index}: {e}")
        raise


def ensure_output_dir(path: str) -> None:
    """Create output directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created output directory: {path}")


def save_program(index: int, code: str, task_description: str, output_dir: str) -> None:
    """
    Save generated program to a file.
    
    Args:
        index: Program number
        code: Generated Python code
        task_description: Task description
        output_dir: Output directory path
    """
    filename = os.path.join(output_dir, f"program_{index:03d}.py")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        logger.debug(f"Saved program #{index} to {filename}")
    except Exception as e:
        logger.error(f"Error saving program #{index}: {e}")
        raise


def save_to_jsonl(index: int, code: str, task_description: str, jsonl_path: Path) -> None:
    """
    Save program to JSONL file for evaluation.
    
    Args:
        index: Program number
        code: Generated Python code
        task_description: Task description
        jsonl_path: Path to JSONL file
    """
    entry = {
        "id": f"generated_python_programs_{index}",
        "source_type": "llm_single",
        "language": "python",
        "code": code,
        "task_description": task_description  # Optional metadata
    }
    
    try:
        with jsonl_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        logger.error(f"Error writing to JSONL for program #{index}: {e}")
        raise


def main():
    """Main function to generate 100 Python programs."""
    ensure_llm_ready()
    
    # Setup output directories
    ensure_output_dir(OUTPUT_DIR)
    jsonl_path = Path(JSONL_FILE)
    
    # Clear existing JSONL file if it exists
    if jsonl_path.exists():
        jsonl_path.unlink()
        logger.info(f"Cleared existing JSONL file: {jsonl_path}")
    
    logger.info(f"Starting generation of {NUM_PROGRAMS} Python programs...")
    print(f"\n{'='*60}")
    print(f"Generating {NUM_PROGRAMS} Python Programs")
    print(f"{'='*60}\n")
    
    success_count = 0
    error_count = 0
    
    for i in range(1, NUM_PROGRAMS + 1):
        try:
            print(f"[{i}/{NUM_PROGRAMS}] Generating program #{i}...")
            
            # Generate task description
            task_description = generate_task_description(i)
            logger.debug(f"Task #{i} description: {task_description[:100]}...")
            
            # Generate code
            code = generate_code(task_description, i)
            
            # Save to file
            save_program(i, code, task_description, OUTPUT_DIR)
            
            # Save to JSONL
            save_to_jsonl(i, code, task_description, jsonl_path)
            
            success_count += 1
            print(f"  ✓ Generated and saved program #{i}")
            
        except KeyboardInterrupt:
            logger.warning("Generation interrupted by user")
            print("\nGeneration interrupted by user")
            break
        except Exception as e:
            error_count += 1
            logger.error(f"Error generating program #{i}: {e}")
            print(f"  ✗ Error generating program #{i}: {e}")
            continue
    
    # Summary
    print(f"\n{'='*60}")
    print("Generation Complete!")
    print(f"{'='*60}")
    print(f"Successfully generated: {success_count}/{NUM_PROGRAMS} programs")
    if error_count > 0:
        print(f"Errors: {error_count}")
    print(f"\nOutput:")
    print(f"  - Python files: {OUTPUT_DIR}/")
    print(f"  - JSONL file: {jsonl_path}")
    print(f"\nNext step: Run evaluation with:")
    print(f"  python evaluate_single.py --dataset {jsonl_path} --name 'SingleModel'")


if __name__ == "__main__":
    main()

