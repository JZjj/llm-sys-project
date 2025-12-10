"""
Code Security Evaluation and Visualization Tool

This module provides functionality to evaluate code security using both static analysis
(Bandit) and LLM-based evaluation (GPT-4.1-mini). It processes JSONL files containing
code samples and generates comprehensive comparison visualizations.

Author: LLM Systems Project
Date: 2024
License: MIT
"""

import json
import sys
import logging
import traceback
from pathlib import Path
from dataclasses import asdict
from typing import Dict, List, Optional, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configure logging for better error tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add parent directory to path to import from LLM evaluation
sys.path.insert(0, str(Path(__file__).parent.parent / "LLM evaluation"))

try:
    from utils import CodeSample, CombinedResult
    from static_analysis import run_static_analysis
    from llm_eval import run_llm_eval, ensure_llm_ready
    from security_eval import load_code_samples, combine
except ImportError as e:
    logger.error(f"Failed to import evaluation modules: {e}")
    logger.error("Make sure the 'LLM evaluation' directory exists and contains the required modules")
    raise


# Note: load_code_samples and combine are now imported from security_eval.py
# to avoid code duplication and ensure consistency with the base evaluation system


def run_evaluation(jsonl_path: Path, max_samples: Optional[int] = None) -> pd.DataFrame:
    """
    Run comprehensive security evaluation on a JSONL file containing code samples.
    
    This function processes each code sample in the JSONL file through two evaluation
    methods:
    1. Static Analysis (Bandit): Rule-based pattern matching for known vulnerabilities
    2. LLM Evaluation (GPT-4.1-mini): Semantic understanding of code security
    
    The function handles errors gracefully, continuing evaluation even if individual
    samples fail, and provides progress feedback.
    
    Args:
        jsonl_path: Path to the JSONL file containing code samples to evaluate
        max_samples: Maximum number of samples to evaluate (None for all samples).
                    Useful for testing or quick evaluations.
        
    Returns:
        pandas.DataFrame containing evaluation results for all successfully processed
        samples. Columns include security scores, vulnerability flags, issue counts,
        and detailed issue information.
        
    Raises:
        FileNotFoundError: If the JSONL file does not exist
        ValueError: If max_samples is negative
        
    Example:
        >>> results_df = run_evaluation(Path("data.jsonl"), max_samples=10)
        >>> print(f"Evaluated {len(results_df)} samples")
    """
    if max_samples is not None and max_samples < 0:
        raise ValueError("max_samples must be non-negative")
    
    logger.info(f"Starting evaluation of {jsonl_path.name}")
    print(f"\n{'='*60}")
    print(f"Evaluating: {jsonl_path.name}")
    print(f"{'='*60}")
    
    # Load code samples with error handling
    try:
        samples = load_code_samples(jsonl_path)
    except Exception as e:
        logger.error(f"Failed to load samples from {jsonl_path}: {e}")
        raise
    
    # Limit samples if specified
    original_count = len(samples)
    if max_samples:
        samples = samples[:max_samples]
        logger.info(f"Limited evaluation to {len(samples)} samples (from {original_count})")
    
    if not samples:
        logger.warning("No samples to evaluate")
        return pd.DataFrame()
    
    combined_results = []
    success_count = 0
    error_count = 0
    
    # Evaluate each sample
    for idx, sample in enumerate(samples, 1):
        print(f"[{idx}/{len(samples)}] Evaluating sample {sample.id}...")
        
        try:
            # Run static analysis (Bandit)
            logger.debug(f"Running static analysis for {sample.id}")
            sa_res = run_static_analysis(sample)
            
            # Run LLM evaluation
            logger.debug(f"Running LLM evaluation for {sample.id}")
            llm_res = run_llm_eval(sample)
            
            # Combine results
            combined_result = combine(sample, sa_res, llm_res)
            combined_results.append(combined_result)
            success_count += 1
            
        except KeyboardInterrupt:
            logger.warning("Evaluation interrupted by user")
            print("\nEvaluation interrupted by user")
            break
        except Exception as e:
            error_count += 1
            logger.error(f"Error evaluating {sample.id}: {e}")
            logger.debug(traceback.format_exc())
            print(f"  Error evaluating {sample.id}: {e}")
            continue
    
    # Create DataFrame from results
    if not combined_results:
        logger.warning("No successful evaluations")
        return pd.DataFrame()
    
    try:
        df = pd.DataFrame([asdict(r) for r in combined_results])
        logger.info(
            f"Evaluation complete: {success_count} successful, {error_count} errors"
        )
        return df
    except Exception as e:
        logger.error(f"Error creating DataFrame: {e}")
        raise


def create_comparison_graphs(
    results_dict: Dict[str, pd.DataFrame], 
    output_dir: Path
) -> None:
    """
    Create comprehensive comparison graphs for evaluation results.
    
    This function generates multiple visualization graphs comparing security metrics
    across different datasets. It creates:
    - Security score distributions (box plots)
    - Vulnerability rate comparisons (bar charts)
    - Static analysis issue breakdowns (grouped bar charts)
    - LLM-detected issue distributions (box plots)
    - Correlation plots (scatter plots)
    - Summary statistics table (visual table)
    
    All graphs are saved as high-resolution PNG files (300 DPI) suitable for
    presentations and publications.
    
    Args:
        results_dict: Dictionary mapping dataset names (e.g., "Plain", "Rule", "Rule+RL")
                     to pandas DataFrames containing evaluation results
        output_dir: Directory path where graphs will be saved. Will be created if
                   it doesn't exist.
        
    Raises:
        ValueError: If results_dict is empty or contains invalid data
        OSError: If output directory cannot be created or written to
        
    Example:
        >>> results = {"Plain": df1, "Rule": df2, "Rule+RL": df3}
        >>> create_comparison_graphs(results, Path("output/"))
    """
    if not results_dict:
        raise ValueError("results_dict cannot be empty")
    
    # Validate that all DataFrames have required columns
    required_columns = [
        'llm_security_score', 'llm_vulnerable', 'llm_num_issues',
        'static_num_issues', 'static_high', 'static_medium', 'static_low'
    ]
    for name, df in results_dict.items():
        if df.empty:
            logger.warning(f"Dataset {name} is empty, skipping")
            continue
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            raise ValueError(f"Dataset {name} missing required columns: {missing}")
    
    # Create output directory
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Output directory: {output_dir}")
    except OSError as e:
        logger.error(f"Cannot create output directory {output_dir}: {e}")
        raise
    
    # Set style for better-looking graphs
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10
    
    # Combine all results for comparison
    all_results = []
    for name, df in results_dict.items():
        if df.empty:
            continue
        df_copy = df.copy()
        df_copy['dataset'] = name
        all_results.append(df_copy)
    
    if not all_results:
        logger.warning("No data to visualize")
        return
    
    try:
        combined_df = pd.concat(all_results, ignore_index=True)
    except Exception as e:
        logger.error(f"Error combining DataFrames: {e}")
        raise
    
    # 1. Security Score Comparison (Box Plot)
    try:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=combined_df, x='dataset', y='llm_security_score', palette='Set2')
        plt.title('LLM Security Score Distribution by Dataset', fontsize=14, fontweight='bold')
        plt.xlabel('Dataset', fontsize=12)
        plt.ylabel('Security Score (1-5)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_dir / 'security_score_comparison.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Created security_score_comparison.png")
    except Exception as e:
        logger.error(f"Error creating security score comparison: {e}")
    
    # 2. Vulnerability Rate Comparison (Bar Chart)
    plt.figure(figsize=(10, 6))
    vuln_rates = combined_df.groupby('dataset')['llm_vulnerable'].mean() * 100
    vuln_rates.plot(kind='bar', color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
    plt.title('Vulnerability Rate by Dataset', fontsize=14, fontweight='bold')
    plt.xlabel('Dataset', fontsize=12)
    plt.ylabel('Vulnerability Rate (%)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 100)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'vulnerability_rate_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Static Analysis Issues Comparison (Grouped Bar Chart)
    plt.figure(figsize=(12, 6))
    static_metrics = combined_df.groupby('dataset').agg({
        'static_num_issues': 'mean',
        'static_high': 'mean',
        'static_medium': 'mean',
        'static_low': 'mean'
    })
    
    x = np.arange(len(static_metrics.index))
    width = 0.2
    
    plt.bar(x - 1.5*width, static_metrics['static_high'], width, label='High', color='#e74c3c')
    plt.bar(x - 0.5*width, static_metrics['static_medium'], width, label='Medium', color='#f39c12')
    plt.bar(x + 0.5*width, static_metrics['static_low'], width, label='Low', color='#3498db')
    plt.bar(x + 1.5*width, static_metrics['static_num_issues'], width, label='Total', color='#2ecc71')
    
    plt.xlabel('Dataset', fontsize=12)
    plt.ylabel('Average Number of Issues', fontsize=12)
    plt.title('Static Analysis Issues by Severity and Dataset', fontsize=14, fontweight='bold')
    plt.xticks(x, static_metrics.index, rotation=45, ha='right')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'static_analysis_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. LLM Issues Count Comparison
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=combined_df, x='dataset', y='llm_num_issues', palette='Set3')
    plt.title('LLM Detected Issues Count Distribution by Dataset', fontsize=14, fontweight='bold')
    plt.xlabel('Dataset', fontsize=12)
    plt.ylabel('Number of Issues', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_dir / 'llm_issues_count_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 5. Security Score vs Static Issues Scatter Plot
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    datasets = list(results_dict.keys())
    
    for idx, (ax, dataset) in enumerate(zip(axes, datasets)):
        df = results_dict[dataset]
        ax.scatter(df['static_num_issues'], df['llm_security_score'], 
                  alpha=0.6, s=50, color=plt.cm.Set2(idx))
        ax.set_xlabel('Static Analysis Issues Count', fontsize=11)
        ax.set_ylabel('LLM Security Score', fontsize=11)
        ax.set_title(f'{dataset}', fontsize=12, fontweight='bold')
        ax.grid(alpha=0.3)
    
    plt.suptitle('Security Score vs Static Analysis Issues', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(output_dir / 'security_score_vs_static_issues.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 6. Summary Statistics Table
    summary_stats = []
    for name, df in results_dict.items():
        summary_stats.append({
            'Dataset': name,
            'Total Samples': len(df),
            'Avg Security Score': df['llm_security_score'].mean(),
            'Vulnerability Rate (%)': df['llm_vulnerable'].mean() * 100,
            'Avg Static Issues': df['static_num_issues'].mean(),
            'Avg LLM Issues': df['llm_num_issues'].mean(),
            'Avg High Severity': df['static_high'].mean(),
            'Avg Medium Severity': df['static_medium'].mean(),
            'Avg Low Severity': df['static_low'].mean(),
        })
    
    summary_df = pd.DataFrame(summary_stats)
    summary_df.to_csv(output_dir / 'summary_statistics.csv', index=False)
    
    # Create a visual summary table
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=summary_df.round(2).values,
                     colLabels=summary_df.columns,
                     cellLoc='center',
                     loc='center',
                     bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2)
    
    # Style the header row
    for i in range(len(summary_df.columns)):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    plt.title('Summary Statistics Comparison', fontsize=14, fontweight='bold', pad=20)
    plt.savefig(output_dir / 'summary_statistics_table.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    logger.info(f"All graphs saved to: {output_dir}")
    logger.info(f"Summary statistics saved to: {output_dir / 'summary_statistics.csv'}")
    print(f"\nGraphs saved to: {output_dir}")
    print(f"Summary statistics saved to: {output_dir / 'summary_statistics.csv'}")


def main():
    """
    Main function to evaluate all three jsonl files and generate graphs.
    """
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Evaluate jsonl files and generate comparison graphs')
    parser.add_argument('--max-samples', type=int, default=None,
                        help='Maximum number of samples to evaluate per file (for testing)')
    args = parser.parse_args()
    
    # Ensure LLM is ready
    ensure_llm_ready()
    
    # Define paths
    base_dir = Path(__file__).parent
    jsonl_files = {
        'Plain': base_dir / 'generated_python_programs.jsonl',
        'Rule': base_dir / 'generated_python_programs_rule.jsonl',
        'Rule+RL': base_dir / 'generated_python_programs_rule_rl.jsonl'
    }
    
    # Check if files exist
    for name, path in jsonl_files.items():
        if not path.exists():
            print(f"Error: File not found: {path}")
            return
    
    # Run evaluation on all files
    results = {}
    output_dir = base_dir / 'evaluation_results'
    output_dir.mkdir(exist_ok=True)
    
    for name, jsonl_path in jsonl_files.items():
        try:
            df = run_evaluation(jsonl_path, max_samples=args.max_samples)
            results[name] = df
            # Save individual results
            csv_path = output_dir / f'{name.lower().replace("+", "_")}_results.csv'
            df.to_csv(csv_path, index=False)
            print(f"Saved results to: {csv_path}")
        except Exception as e:
            print(f"Error evaluating {name}: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    # Generate comparison graphs
    if results:
        print(f"\n{'='*60}")
        print("Generating comparison graphs...")
        print(f"{'='*60}")
        create_comparison_graphs(results, output_dir)
        print("\nEvaluation complete!")
    else:
        print("No results to visualize.")


if __name__ == "__main__":
    main()

