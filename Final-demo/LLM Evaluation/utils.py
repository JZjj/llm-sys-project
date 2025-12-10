"""
Data Structures and Type Definitions for Code Security Evaluation

This module defines all data classes used throughout the evaluation system,
providing a consistent structure for code samples, analysis results, and
combined evaluation outputs.

Author: LLM Systems Project
Date: 2024
License: MIT
"""

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class CodeSample:
    """
    Represents a code sample to be evaluated.
    
    Attributes:
        id: Unique identifier for the code sample
        source_type: Source of the code (e.g., "llm", "authentic", "llm_plain")
        language: Programming language (e.g., "python", "javascript")
        code: The actual source code to evaluate
        
    Example:
        >>> sample = CodeSample(
        ...     id="sample_1",
        ...     source_type="llm",
        ...     language="python",
        ...     code="print('hello')"
        ... )
    """
    id: str
    source_type: str
    language: str
    code: str


@dataclass
class StaticIssue:
    """
    Represents a single issue found by static analysis.
    
    Attributes:
        tool: Name of the static analysis tool (e.g., "bandit")
        test_id: Identifier for the test/rule that found the issue
        severity: Severity level ("HIGH", "MEDIUM", "LOW")
        confidence: Confidence level ("HIGH", "MEDIUM", "LOW")
        line_number: Line number where the issue was found
        description: Human-readable description of the issue
        
    Example:
        >>> issue = StaticIssue(
        ...     tool="bandit",
        ...     test_id="B602",
        ...     severity="HIGH",
        ...     confidence="HIGH",
        ...     line_number=10,
        ...     description="Use of subprocess detected"
        ... )
    """
    tool: str
    test_id: str
    severity: str
    confidence: str
    line_number: int
    description: str


@dataclass
class StaticAnalysisResult:
    """
    Results from static analysis of a code sample.
    
    Attributes:
        sample_id: Identifier of the code sample that was analyzed
        num_issues: Total number of issues found
        num_high: Number of high-severity issues
        num_medium: Number of medium-severity issues
        num_low: Number of low-severity issues
        issues: List of StaticIssue objects with detailed information
        
    Example:
        >>> result = StaticAnalysisResult(
        ...     sample_id="sample_1",
        ...     num_issues=3,
        ...     num_high=1,
        ...     num_medium=1,
        ...     num_low=1,
        ...     issues=[issue1, issue2, issue3]
        ... )
    """
    sample_id: str
    num_issues: int
    num_high: int
    num_medium: int
    num_low: int
    issues: List[StaticIssue]


@dataclass
class LLMIssue:
    """
    Represents a security issue identified by LLM evaluation.
    
    Attributes:
        type: Category of the issue (e.g., "Input Validation", "Injection")
        severity: Severity level ("critical", "high", "medium", "low")
        description: Detailed description of the security concern
        
    Example:
        >>> issue = LLMIssue(
        ...     type="Code Injection",
        ...     severity="critical",
        ...     description="Use of eval() allows arbitrary code execution"
        ... )
    """
    type: str
    severity: str
    description: str


@dataclass
class LLMEvalResult:
    """
    Results from LLM-based security evaluation of a code sample.
    
    Attributes:
        sample_id: Identifier of the code sample that was evaluated
        security_score: Security score from 1-5 (5 = most secure)
        vulnerable: Boolean flag indicating if the code is vulnerable
        issues: List of LLMIssue objects with detailed security concerns
        raw_response: Raw response from the LLM API for debugging
        
    Example:
        >>> result = LLMEvalResult(
        ...     sample_id="sample_1",
        ...     security_score=4.5,
        ...     vulnerable=False,
        ...     issues=[issue1, issue2],
        ...     raw_response={"content": "...", "parsed": {...}}
        ... )
    """
    sample_id: str
    security_score: float
    vulnerable: bool
    issues: List[LLMIssue]
    raw_response: Dict[str, Any]


@dataclass
class CombinedResult:
    """
    Combined results from both static analysis and LLM evaluation.
    
    This dataclass aggregates all evaluation metrics into a single structure
    suitable for storage in CSV format or further analysis.
    
    Attributes:
        sample_id: Identifier of the code sample
        source_type: Source of the code
        language: Programming language
        static_num_issues: Total static analysis issues
        static_high: Number of high-severity static issues
        static_medium: Number of medium-severity static issues
        static_low: Number of low-severity static issues
        llm_security_score: Security score from LLM (1-5)
        llm_vulnerable: Whether LLM flagged code as vulnerable
        llm_num_issues: Number of issues detected by LLM
        static_issues_json: JSON string of static analysis issues
        llm_issues_json: JSON string of LLM-detected issues
        
    Example:
        >>> result = CombinedResult(
        ...     sample_id="sample_1",
        ...     source_type="llm",
        ...     language="python",
        ...     static_num_issues=2,
        ...     static_high=0,
        ...     static_medium=1,
        ...     static_low=1,
        ...     llm_security_score=4.0,
        ...     llm_vulnerable=False,
        ...     llm_num_issues=1,
        ...     static_issues_json="[...]",
        ...     llm_issues_json="[...]"
        ... )
    """
    sample_id: str
    source_type: str
    language: str

    static_num_issues: int
    static_high: int
    static_medium: int
    static_low: int

    llm_security_score: float
    llm_vulnerable: bool
    llm_num_issues: int

    static_issues_json: str
    llm_issues_json: str
