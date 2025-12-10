"""
Static Analysis Module for Code Security Evaluation

This module provides static analysis functionality using Bandit, a security linter
for Python code. It identifies common security vulnerabilities through pattern
matching and rule-based analysis.

Author: LLM Systems Project
Date: 2024
License: MIT
"""

import tempfile
import subprocess
import json
import logging
from pathlib import Path
from typing import Optional
from utils import StaticIssue, StaticAnalysisResult, CodeSample

# Configure logging
logger = logging.getLogger(__name__)


def run_bandit(code: str, sample_id: str) -> StaticAnalysisResult:
    """
    Run Bandit static analysis on Python code.
    
    This function creates a temporary file with the provided code, runs Bandit
    analysis on it, and parses the results into a structured format.
    
    Args:
        code: Python source code to analyze
        sample_id: Unique identifier for the code sample (used for temp file naming)
        
    Returns:
        StaticAnalysisResult object containing:
            - Total number of issues found
            - Issues categorized by severity (high, medium, low)
            - List of detailed issue objects
            
    Raises:
        RuntimeError: If Bandit execution fails (return code not 0 or 1)
        FileNotFoundError: If Bandit is not installed or not in PATH
        
    Example:
        >>> code = "import os; os.system('rm -rf /')"
        >>> result = run_bandit(code, "sample_1")
        >>> print(f"Found {result.num_issues} issues")
    """
    # Create temporary file for Bandit analysis
    with tempfile.TemporaryDirectory() as tmp:
        # Sanitize sample_id for filename (remove special characters)
        safe_id = "".join(c for c in sample_id if c.isalnum() or c in ('-', '_'))[:50]
        tmp_file = Path(tmp) / f"{safe_id}.py"
        
        try:
            tmp_file.write_text(code, encoding="utf-8")
        except Exception as e:
            logger.error(f"Failed to write temporary file for {sample_id}: {e}")
            raise RuntimeError(f"Cannot create temporary file: {e}")
        
        # Run Bandit with JSON output format
        cmd = ["bandit", "-f", "json", "-q", str(tmp_file)]
        
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30  # 30 second timeout
            )
        except subprocess.TimeoutExpired:
            logger.warning(f"Bandit timeout for {sample_id}")
            return StaticAnalysisResult(sample_id, 0, 0, 0, 0, [])
        except FileNotFoundError:
            logger.error("Bandit not found. Please install with: pip install bandit")
            raise FileNotFoundError(
                "Bandit is not installed or not in PATH. "
                "Install with: pip install bandit"
            )
        
        # Bandit returns 0 (no issues) or 1 (issues found)
        # Other return codes indicate errors
        if proc.returncode not in (0, 1):
            error_msg = proc.stderr or proc.stdout or "Unknown error"
            logger.error(f"Bandit failed for {sample_id}: {error_msg}")
            raise RuntimeError(f"Bandit failed: {error_msg}")
        
        # Parse Bandit JSON output
        try:
            report = json.loads(proc.stdout)
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to parse Bandit JSON output for {sample_id}: {e}")
            report = {"results": []}
        
        # Process issues from Bandit report
        issues = []
        high = medium = low = 0
        
        for r in report.get("results", []):
            sev = r.get("issue_severity", "").upper()
            
            # Categorize by severity
            if sev == "HIGH":
                high += 1
            elif sev == "MEDIUM":
                medium += 1
            else:
                low += 1
            
            # Create StaticIssue object
            issues.append(
                StaticIssue(
                    tool="bandit",
                    test_id=r.get("test_id", ""),
                    severity=r.get("issue_severity", ""),
                    confidence=r.get("issue_confidence", ""),
                    line_number=r.get("line_number", 0),
                    description=r.get("issue_text", "")
                )
            )
        
        logger.debug(
            f"Bandit analysis for {sample_id}: {len(issues)} issues "
            f"(High: {high}, Medium: {medium}, Low: {low})"
        )
        
        return StaticAnalysisResult(
            sample_id=sample_id,
            num_issues=len(issues),
            num_high=high,
            num_medium=medium,
            num_low=low,
            issues=issues,
        )


def run_static_analysis(sample: CodeSample) -> StaticAnalysisResult:
    """
    Run static analysis on a code sample.
    
    This function checks the language of the code sample and runs appropriate
    static analysis tools. Currently supports Python via Bandit.
    
    Args:
        sample: CodeSample object containing code to analyze
        
    Returns:
        StaticAnalysisResult object with analysis results. For non-Python code,
        returns an empty result (no issues found).
        
    Example:
        >>> sample = CodeSample(id="test", source_type="llm", language="python", code="print('hello')")
        >>> result = run_static_analysis(sample)
        >>> print(f"Found {result.num_issues} issues")
    """
    # Currently only Python is supported via Bandit
    if sample.language.lower() != "python":
        logger.debug(
            f"Static analysis not supported for language: {sample.language}. "
            "Returning empty result."
        )
        return StaticAnalysisResult(
            sample_id=sample.id,
            num_issues=0,
            num_high=0,
            num_medium=0,
            num_low=0,
            issues=[],
        )
    
    try:
        return run_bandit(sample.code, sample.id)
    except Exception as e:
        logger.error(f"Static analysis failed for {sample.id}: {e}")
        # Return empty result on error to allow evaluation to continue
        return StaticAnalysisResult(
            sample_id=sample.id,
            num_issues=0,
            num_high=0,
            num_medium=0,
            num_low=0,
            issues=[],
        )
