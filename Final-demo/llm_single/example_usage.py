"""
Example usage of the single model evaluation system.

This script demonstrates how to use both code generation and evaluation functions programmatically.
"""

from pathlib import Path
from evaluate_single import (
    load_code_samples,
    run_evaluation,
    create_visualizations
)
# Note: generate_code.py is a standalone script, but you can import functions if needed

def example_basic_evaluation():
    """Example: Basic evaluation of a JSONL file."""
    print("Example 1: Basic Evaluation")
    print("=" * 50)
    
    # Path to your JSONL file
    jsonl_path = Path("your_code_samples.jsonl")
    
    # Run evaluation
    results_df = run_evaluation(jsonl_path, max_samples=10)
    
    # Create visualizations
    output_dir = Path("example_results")
    create_visualizations(results_df, output_dir, "ExampleDataset")
    
    print(f"\nResults saved to: {output_dir}")
    print(f"Total samples evaluated: {len(results_df)}")


def example_custom_analysis():
    """Example: Custom analysis of results."""
    print("\nExample 2: Custom Analysis")
    print("=" * 50)
    
    import pandas as pd
    
    # Load existing results
    results_df = pd.read_csv("evaluation_results/dataset_results.csv")
    
    # Filter vulnerable samples
    vulnerable = results_df[results_df['llm_vulnerable'] == True]
    print(f"Vulnerable samples: {len(vulnerable)}")
    
    # Get high security samples
    high_security = results_df[results_df['llm_security_score'] >= 4.5]
    print(f"High security samples (>=4.5): {len(high_security)}")
    
    # Analyze static issues
    with_issues = results_df[results_df['static_num_issues'] > 0]
    print(f"Samples with static analysis issues: {len(with_issues)}")
    
    # Calculate statistics
    print(f"\nStatistics:")
    print(f"  Average security score: {results_df['llm_security_score'].mean():.2f}")
    print(f"  Median security score: {results_df['llm_security_score'].median():.2f}")
    print(f"  Vulnerability rate: {(results_df['llm_vulnerable'].mean() * 100):.2f}%")
    print(f"  Average static issues: {results_df['static_num_issues'].mean():.2f}")


def example_load_samples():
    """Example: Loading and inspecting samples."""
    print("\nExample 3: Loading Samples")
    print("=" * 50)
    
    jsonl_path = Path("your_code_samples.jsonl")
    
    # Load samples
    samples = load_code_samples(jsonl_path)
    
    print(f"Loaded {len(samples)} samples")
    
    # Inspect first few samples
    for i, sample in enumerate(samples[:3], 1):
        print(f"\nSample {i}:")
        print(f"  ID: {sample.id}")
        print(f"  Source: {sample.source_type}")
        print(f"  Language: {sample.language}")
        print(f"  Code length: {len(sample.code)} characters")


def example_generate_and_evaluate():
    """Example: Complete workflow - generate code then evaluate."""
    print("Example 4: Generate and Evaluate")
    print("=" * 50)
    
    import subprocess
    
    # Step 1: Generate code
    print("Step 1: Generating code samples...")
    subprocess.run(["python", "generate_code.py"])
    
    # Step 2: Evaluate generated code
    print("\nStep 2: Evaluating generated code...")
    results_df = run_evaluation(
        Path("generated_python_programs.jsonl"),
        max_samples=10  # Evaluate first 10 for quick test
    )
    
    # Step 3: Create visualizations
    print("\nStep 3: Creating visualizations...")
    create_visualizations(results_df, Path("example_results"), "GeneratedCode")
    
    print(f"\nComplete! Results saved to example_results/")


if __name__ == "__main__":
    print("Single Model Evaluation - Example Usage")
    print("=" * 50)
    print("\nNote: Update file paths in the examples before running.")
    print("\nUncomment the example you want to run:")
    print()
    
    # Uncomment to run examples:
    # example_basic_evaluation()
    # example_custom_analysis()
    # example_load_samples()
    # example_generate_and_evaluate()
    
    print("\nFor command-line usage, see:")
    print("  # Generate code:")
    print("  python generate_code.py")
    print("  # Evaluate code:")
    print("  python evaluate_single.py --help")

