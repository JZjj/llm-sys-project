"""
Code Security Evaluation System - Main Experiment Driver

This module provides the main entry point for running security evaluations on code samples.
It combines static analysis (Bandit) and LLM-based evaluation (GPT-4.1-mini) to provide
comprehensive security assessment.

Author: LLM Systems Project
Date: 2024
License: MIT
"""

import argparse
import json
import logging
import traceback
from pathlib import Path
from dataclasses import asdict
from typing import List, Optional
import pandas as pd

from utils import CodeSample, CombinedResult
from static_analysis import run_static_analysis
from llm_eval import run_llm_eval, ensure_llm_ready

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_code_samples(path: Path) -> List[CodeSample]:
    """
    Load code samples from a JSONL file.
    
    This function reads a JSONL (JSON Lines) file where each line contains a JSON object
    representing a code sample. It validates the required fields and creates CodeSample
    objects for each valid entry.
    
    Args:
        path: Path to the JSONL file containing code samples
        
    Returns:
        List of CodeSample objects, one for each line in the file
        
    Raises:
        FileNotFoundError: If the specified file does not exist
        json.JSONDecodeError: If a line contains invalid JSON
        KeyError: If required fields ('id', 'source_type', 'code') are missing
        
    Example:
        >>> samples = load_code_samples(Path("data.jsonl"))
        >>> print(f"Loaded {len(samples)} samples")
    """
    if not path.exists():
        raise FileNotFoundError(f"JSONL file not found: {path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")
    
    samples = []
    line_number = 0
    
    try:
        with path.open("r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    obj = json.loads(line)
                    
                    # Validate required fields
                    required_fields = ["id", "source_type", "code"]
                    missing_fields = [field for field in required_fields if field not in obj]
                    if missing_fields:
                        logger.warning(
                            f"Line {line_number}: Missing required fields {missing_fields}, skipping"
                        )
                        continue
                    
                    # Create CodeSample object with validated data
                    sample = CodeSample(
                        id=str(obj["id"]),
                        source_type=str(obj["source_type"]),
                        language=obj.get("language", "python").lower(),
                        code=str(obj["code"]),
                    )
                    samples.append(sample)
                    
                except json.JSONDecodeError as e:
                    logger.warning(f"Line {line_number}: Invalid JSON, skipping - {e}")
                    continue
                except Exception as e:
                    logger.warning(f"Line {line_number}: Error processing sample - {e}")
                    continue
        
        logger.info(f"Successfully loaded {len(samples)} code samples from {path.name}")
        return samples
        
    except IOError as e:
        logger.error(f"Error reading file {path}: {e}")
        raise


def combine(sample: CodeSample, sa, llm) -> CombinedResult:
    """
    Combine static analysis and LLM evaluation results into a single result object.
    
    This function aggregates results from both static analysis (Bandit) and LLM-based
    evaluation into a unified CombinedResult object that can be easily stored and analyzed.
    
    Args:
        sample: CodeSample object containing the original code sample metadata
        sa: StaticAnalysisResult from Bandit static analysis
        llm: LLMEvalResult from LLM-based security evaluation
        
    Returns:
        CombinedResult object containing all evaluation metrics
        
    Raises:
        TypeError: If any of the input objects are not of the expected type
        json.JSONEncodeError: If serialization of issues fails
        
    Example:
        >>> result = combine(code_sample, static_result, llm_result)
        >>> print(f"Security score: {result.llm_security_score}")
    """
    try:
        # Serialize issues to JSON for storage
        static_issues_json = json.dumps([asdict(issue) for issue in sa.issues])
        llm_issues_json = json.dumps([asdict(issue) for issue in llm.issues])
        
        return CombinedResult(
            sample_id=sample.id,
            source_type=sample.source_type,
            language=sample.language,
            static_num_issues=sa.num_issues,
            static_high=sa.num_high,
            static_medium=sa.num_medium,
            static_low=sa.num_low,
            llm_security_score=float(llm.security_score),
            llm_vulnerable=bool(llm.vulnerable),
            llm_num_issues=len(llm.issues),
            static_issues_json=static_issues_json,
            llm_issues_json=llm_issues_json,
        )
    except (TypeError, AttributeError) as e:
        logger.error(f"Error combining results for sample {sample.id}: {e}")
        raise
    except json.JSONEncodeError as e:
        logger.error(f"Error serializing issues for sample {sample.id}: {e}")
        raise


def run_experiment(
    dataset: Path, 
    out_csv: Path, 
    max_samples: Optional[int] = None
) -> pd.DataFrame:
    """
    Run comprehensive security evaluation experiment on a dataset.
    
    This function processes each code sample in the dataset through two evaluation
    methods:
    1. Static Analysis (Bandit): Rule-based pattern matching for known vulnerabilities
    2. LLM Evaluation (GPT-4.1-mini): Semantic understanding of code security
    
    The function handles errors gracefully, continuing evaluation even if individual
    samples fail, and provides progress feedback.
    
    Args:
        dataset: Path to the JSONL file containing code samples to evaluate
        out_csv: Path where the results CSV file will be saved
        max_samples: Maximum number of samples to evaluate (None for all samples).
                    Useful for testing or quick evaluations.
        
    Returns:
        pandas.DataFrame containing evaluation results for all successfully processed
        samples. Columns include security scores, vulnerability flags, issue counts,
        and detailed issue information.
        
    Raises:
        FileNotFoundError: If the dataset file does not exist
        ValueError: If max_samples is negative
        RuntimeError: If LLM client cannot be initialized
        
    Example:
        >>> results_df = run_experiment(
        ...     Path("data.jsonl"), 
        ...     Path("results.csv"), 
        ...     max_samples=10
        ... )
        >>> print(f"Evaluated {len(results_df)} samples")
    """
    if max_samples is not None and max_samples < 0:
        raise ValueError("max_samples must be non-negative")
    
    # Ensure LLM is ready
    try:
        ensure_llm_ready()
    except Exception as e:
        logger.error(f"Failed to initialize LLM: {e}")
        raise RuntimeError(f"LLM initialization failed: {e}")
    
    logger.info(f"Starting evaluation experiment on {dataset.name}")
    print(f"\n{'='*60}")
    print(f"Evaluating: {dataset.name}")
    print(f"{'='*60}")
    
    # Load code samples with error handling
    try:
        samples = load_code_samples(dataset)
    except Exception as e:
        logger.error(f"Failed to load samples from {dataset}: {e}")
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
        
        # Save results to CSV
        out_csv.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(out_csv, index=False)
        
        logger.info(
            f"Evaluation complete: {success_count} successful, {error_count} errors"
        )
        logger.info(f"Results saved to: {out_csv}")
        print(f"\nSaved results to: {out_csv}")
        print(f"Successfully evaluated: {success_count}/{len(samples)} samples")
        
        return df
    except Exception as e:
        logger.error(f"Error creating DataFrame or saving results: {e}")
        raise


def parse_args():
    """
    Parse command-line arguments for the security evaluation script.
    
    Returns:
        argparse.Namespace object containing parsed arguments
        
    Example:
        >>> args = parse_args()
        >>> print(args.dataset)
    """
    parser = argparse.ArgumentParser(
        description="Code Security Evaluation System - Part 1",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Evaluate all samples
  python security_eval.py --dataset data.jsonl --out results.csv
  
  # Evaluate first 10 samples (for testing)
  python security_eval.py --dataset data.jsonl --out results.csv --max-samples 10
        """
    )
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Path to JSONL file containing code samples to evaluate"
    )
    parser.add_argument(
        "--out",
        type=str,
        required=True,
        help="Path to output CSV file for results"
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        default=None,
        help="Maximum number of samples to evaluate (for testing, default: all)"
    )
    return parser.parse_args()


def main():
    """
    Main entry point for the security evaluation script.
    
    This function parses command-line arguments and runs the evaluation experiment.
    It handles errors gracefully and provides user-friendly error messages.
    """
    try:
        args = parse_args()
        run_experiment(Path(args.dataset), Path(args.out), args.max_samples)
    except KeyboardInterrupt:
        print("\n\nEvaluation interrupted by user. Exiting...")
        logger.info("Evaluation interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"\nError: {e}")
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
