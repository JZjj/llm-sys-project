from dataclasses import dataclass
from typing import List, Dict, Any


# Code Samples

@dataclass
class CodeSample:
    id: str
    source_type: str
    language: str
    code: str


# Static Analysis

@dataclass
class StaticIssue:
    tool: str
    test_id: str
    severity: str
    confidence: str
    line_number: int
    description: str


@dataclass
class StaticAnalysisResult:
    sample_id: str
    num_issues: int
    num_high: int
    num_medium: int
    num_low: int
    issues: List[StaticIssue]


# LLM Results

@dataclass
class LLMIssue:
    type: str
    severity: str
    description: str


@dataclass
class LLMEvalResult:
    sample_id: str
    security_score: float
    vulnerable: bool
    issues: List[LLMIssue]
    raw_response: Dict[str, Any]


# Combined Output

@dataclass
class CombinedResult:s
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
