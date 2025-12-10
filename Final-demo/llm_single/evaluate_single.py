"""
Code Security Evaluation Tool for Single Model

This module provides functionality to evaluate code security using both static analysis
(Bandit) and LLM-based evaluation (GPT-4.1-mini). It processes a single JSONL file
containing code samples and generates comprehensive visualizations and statistics.

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
from typing import List, Optional
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


def create_visualizations(df: pd.DataFrame, output_dir: Path, dataset_name: str = "Dataset") -> None:
    """
    Create comprehensive visualizations for a single dataset evaluation results.
    
    This function generates multiple visualization graphs showing security metrics
    for the evaluated code samples. It creates:
    - Security score distribution (histogram and box plot)
    - Vulnerability rate summary
    - Static analysis issues breakdown
    - LLM-detected issues distribution
    - Correlation plots
    - Summary statistics table
    
    All graphs are saved as high-resolution PNG files (300 DPI) suitable for
    presentations and publications.
    
    Args:
        df: pandas DataFrame containing evaluation results
        output_dir: Directory path where graphs will be saved. Will be created if
                   it doesn't exist.
        dataset_name: Name of the dataset for labeling (default: "Dataset")
        
    Raises:
        ValueError: If DataFrame is empty or contains invalid data
        OSError: If output directory cannot be created or written to
        
    Example:
        >>> create_visualizations(results_df, Path("output/"), "MyModel")
    """
    if df.empty:
        raise ValueError("DataFrame cannot be empty")
    
    # Validate that DataFrame has required columns
    required_columns = [
        'llm_security_score', 'llm_vulnerable', 'llm_num_issues',
        'static_num_issues', 'static_high', 'static_medium', 'static_low'
    ]
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"DataFrame missing required columns: {missing}")
    
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
    
    # 1. Security Score Distribution (Histogram)
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(df['llm_security_score'], bins=20, edgecolor='black', alpha=0.7, color='#4ecdc4')
        plt.title(f'Security Score Distribution - {dataset_name}', fontsize=14, fontweight='bold')
        plt.xlabel('Security Score (1-5)', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / 'security_score_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Created security_score_distribution.png")
    except Exception as e:
        logger.error(f"Error creating security score distribution: {e}")
    
    # 2. Security Score Box Plot
    try:
        plt.figure(figsize=(8, 6))
        sns.boxplot(y=df['llm_security_score'], color='#45b7d1')
        plt.title(f'Security Score Distribution - {dataset_name}', fontsize=14, fontweight='bold')
        plt.ylabel('Security Score (1-5)', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / 'security_score_boxplot.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Created security_score_boxplot.png")
    except Exception as e:
        logger.error(f"Error creating security score box plot: {e}")
    
    # 3. Vulnerability Summary
    try:
        plt.figure(figsize=(8, 6))
        vuln_count = df['llm_vulnerable'].sum()
        safe_count = len(df) - vuln_count
        vuln_rate = (vuln_count / len(df)) * 100 if len(df) > 0 else 0
        
        plt.bar(['Vulnerable', 'Safe'], [vuln_count, safe_count], 
                color=['#ff6b6b', '#4ecdc4'], edgecolor='black')
        plt.title(f'Vulnerability Summary - {dataset_name}', fontsize=14, fontweight='bold')
        plt.ylabel('Number of Samples', fontsize=12)
        plt.text(0, vuln_count, f'{vuln_count}\n({vuln_rate:.1f}%)', 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
        plt.text(1, safe_count, f'{safe_count}\n({100-vuln_rate:.1f}%)', 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / 'vulnerability_summary.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Created vulnerability_summary.png")
    except Exception as e:
        logger.error(f"Error creating vulnerability summary: {e}")
    
    # 4. Static Analysis Issues Breakdown
    try:
        plt.figure(figsize=(10, 6))
        issue_counts = {
            'High': df['static_high'].sum(),
            'Medium': df['static_medium'].sum(),
            'Low': df['static_low'].sum(),
            'Total': df['static_num_issues'].sum()
        }
        
        colors = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71']
        bars = plt.bar(issue_counts.keys(), issue_counts.values(), 
                      color=colors, edgecolor='black')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        plt.title(f'Static Analysis Issues Breakdown - {dataset_name}', fontsize=14, fontweight='bold')
        plt.xlabel('Severity Level', fontsize=12)
        plt.ylabel('Number of Issues', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / 'static_analysis_breakdown.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Created static_analysis_breakdown.png")
    except Exception as e:
        logger.error(f"Error creating static analysis breakdown: {e}")
    
    # 5. LLM Issues Count Distribution
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(df['llm_num_issues'], bins=range(int(df['llm_num_issues'].max()) + 2), 
                edgecolor='black', alpha=0.7, color='#9b59b6')
        plt.title(f'LLM Detected Issues Distribution - {dataset_name}', fontsize=14, fontweight='bold')
        plt.xlabel('Number of Issues', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xticks(range(int(df['llm_num_issues'].max()) + 1))
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / 'llm_issues_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Created llm_issues_distribution.png")
    except Exception as e:
        logger.error(f"Error creating LLM issues distribution: {e}")
    
    # 6. Security Score vs Static Issues Scatter Plot
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(df['static_num_issues'], df['llm_security_score'], 
                   alpha=0.6, s=50, color='#e67e22')
        plt.xlabel('Static Analysis Issues Count', fontsize=12)
        plt.ylabel('LLM Security Score', fontsize=12)
        plt.title(f'Security Score vs Static Analysis Issues - {dataset_name}', 
                 fontsize=14, fontweight='bold')
        plt.grid(alpha=0.3)
        
        # Add correlation coefficient
        correlation = df['static_num_issues'].corr(df['llm_security_score'])
        plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
                transform=plt.gca().transAxes, fontsize=11,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        plt.savefig(output_dir / 'security_score_vs_static_issues.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Created security_score_vs_static_issues.png")
    except Exception as e:
        logger.error(f"Error creating scatter plot: {e}")
    
    # 7. Summary Statistics Table
    try:
        summary_stats = {
            'Metric': [
                'Total Samples',
                'Avg Security Score',
                'Median Security Score',
                'Min Security Score',
                'Max Security Score',
                'Vulnerability Rate (%)',
                'Vulnerable Samples',
                'Safe Samples',
                'Avg Static Issues',
                'Total Static Issues',
                'Avg High Severity',
                'Avg Medium Severity',
                'Avg Low Severity',
                'Avg LLM Issues',
                'Total LLM Issues'
            ],
            'Value': [
                len(df),
                f"{df['llm_security_score'].mean():.2f}",
                f"{df['llm_security_score'].median():.2f}",
                f"{df['llm_security_score'].min():.2f}",
                f"{df['llm_security_score'].max():.2f}",
                f"{(df['llm_vulnerable'].mean() * 100):.2f}",
                int(df['llm_vulnerable'].sum()),
                int((~df['llm_vulnerable']).sum()),
                f"{df['static_num_issues'].mean():.2f}",
                int(df['static_num_issues'].sum()),
                f"{df['static_high'].mean():.2f}",
                f"{df['static_medium'].mean():.2f}",
                f"{df['static_low'].mean():.2f}",
                f"{df['llm_num_issues'].mean():.2f}",
                int(df['llm_num_issues'].sum())
            ]
        }
        
        summary_df = pd.DataFrame(summary_stats)
        summary_df.to_csv(output_dir / 'summary_statistics.csv', index=False)
        
        # Create a visual summary table
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=summary_df.values,
                         colLabels=summary_df.columns,
                         cellLoc='left',
                         loc='center',
                         bbox=[0, 0, 1, 1])
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.5)
        
        # Style the header row
        for i in range(len(summary_df.columns)):
            table[(0, i)].set_facecolor('#4CAF50')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # Style alternating rows
        for i in range(1, len(summary_df) + 1):
            if i % 2 == 0:
                for j in range(len(summary_df.columns)):
                    table[(i, j)].set_facecolor('#f0f0f0')
        
        plt.title(f'Summary Statistics - {dataset_name}', fontsize=14, fontweight='bold', pad=20)
        plt.savefig(output_dir / 'summary_statistics_table.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Created summary_statistics_table.png")
    except Exception as e:
        logger.error(f"Error creating summary statistics: {e}")
    
    logger.info(f"All visualizations saved to: {output_dir}")
    print(f"\nVisualizations saved to: {output_dir}")
    print(f"Summary statistics saved to: {output_dir / 'summary_statistics.csv'}")


def main():
    """
    Main function to evaluate a single JSONL file and generate visualizations.
    """
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Evaluate a single JSONL file and generate security analysis visualizations'
    )
    parser.add_argument(
        '--dataset',
        type=str,
        required=True,
        help='Path to the JSONL file containing code samples to evaluate'
    )
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Output directory for results (default: evaluation_results/)'
    )
    parser.add_argument(
        '--name',
        type=str,
        default=None,
        help='Name of the dataset for labeling (default: filename)'
    )
    parser.add_argument(
        '--max-samples',
        type=int,
        default=None,
        help='Maximum number of samples to evaluate (for testing)'
    )
    args = parser.parse_args()
    
    # Ensure LLM is ready
    try:
        ensure_llm_ready()
    except Exception as e:
        logger.error(f"Failed to initialize LLM: {e}")
        print("Error: Make sure OPENAI_API_KEY is set correctly")
        return
    
    # Define paths
    base_dir = Path(__file__).parent
    jsonl_path = Path(args.dataset)
    
    # Check if file exists
    if not jsonl_path.exists():
        logger.error(f"File not found: {jsonl_path}")
        print(f"Error: File not found: {jsonl_path}")
        return
    
    # Determine output directory
    if args.output:
        output_dir = Path(args.output)
    else:
        output_dir = base_dir / 'evaluation_results'
    
    # Determine dataset name
    if args.name:
        dataset_name = args.name
    else:
        dataset_name = jsonl_path.stem
    
    # Run evaluation
    try:
        print(f"\n{'='*60}")
        print(f"Evaluating: {jsonl_path.name}")
        print(f"Dataset Name: {dataset_name}")
        print(f"{'='*60}")
        
        df = run_evaluation(jsonl_path, max_samples=args.max_samples)
        
        if df.empty:
            print("No results to visualize.")
            return
        
        # Save results CSV
        csv_path = output_dir / f'{dataset_name}_results.csv'
        output_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(csv_path, index=False)
        print(f"\nSaved detailed results to: {csv_path}")
        
        # Generate visualizations
        print(f"\n{'='*60}")
        print("Generating visualizations...")
        print(f"{'='*60}")
        create_visualizations(df, output_dir, dataset_name)
        
        print("\n" + "="*60)
        print("Evaluation complete!")
        print("="*60)
        print(f"\nResults saved to: {output_dir}")
        print(f"  - Detailed results: {csv_path}")
        print(f"  - Summary statistics: {output_dir / 'summary_statistics.csv'}")
        print(f"  - Visualizations: {output_dir}/*.png")
        
    except Exception as e:
        logger.error(f"Error during evaluation: {e}")
        print(f"Error: {e}")
        traceback.print_exc()
        return


if __name__ == "__main__":
    main()

