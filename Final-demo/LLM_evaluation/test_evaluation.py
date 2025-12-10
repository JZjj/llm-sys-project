"""
Unit tests for the LLM evaluation system.

This module contains comprehensive unit tests for all major components
of the evaluation system, including:
- Code sample loading
- Static analysis
- LLM evaluation (mocked)
- Result combination
- Error handling

Run tests with: pytest test_evaluation.py -v
Run with coverage: pytest test_evaluation.py --cov=. --cov-report=html
"""

import pytest
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from utils import (
    CodeSample,
    StaticIssue,
    StaticAnalysisResult,
    LLMIssue,
    LLMEvalResult,
    CombinedResult
)
from static_analysis import run_static_analysis, run_bandit
from security_eval import load_code_samples, combine, run_experiment


class TestLoadCodeSamples:
    """Test cases for load_code_samples function."""
    
    def test_load_valid_jsonl(self):
        """Test loading a valid JSONL file with proper format."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            f.write(json.dumps({
                "id": "test_1",
                "source_type": "test",
                "language": "python",
                "code": "print('hello')"
            }) + "\n")
            f.write(json.dumps({
                "id": "test_2",
                "source_type": "test",
                "code": "x = 1"
            }) + "\n")
            temp_path = Path(f.name)
        
        try:
            samples = load_code_samples(temp_path)
            assert len(samples) == 2
            assert samples[0].id == "test_1"
            assert samples[1].id == "test_2"
            assert samples[0].language == "python"
            assert samples[1].language == "python"  # Default
        finally:
            temp_path.unlink()
    
    def test_load_empty_file(self):
        """Test loading an empty file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            temp_path = Path(f.name)
        
        try:
            samples = load_code_samples(temp_path)
            assert len(samples) == 0
        finally:
            temp_path.unlink()
    
    def test_load_missing_required_fields(self):
        """Test handling of missing required fields."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            f.write(json.dumps({"id": "test"}) + "\n")  # Missing source_type and code
            temp_path = Path(f.name)
        
        try:
            samples = load_code_samples(temp_path)
            assert len(samples) == 0  # Should skip invalid entries
        finally:
            temp_path.unlink()
    
    def test_load_invalid_json(self):
        """Test handling of invalid JSON lines."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            f.write("not valid json\n")
            f.write(json.dumps({
                "id": "test_1",
                "source_type": "test",
                "code": "x = 1"
            }) + "\n")
            temp_path = Path(f.name)
        
        try:
            samples = load_code_samples(temp_path)
            assert len(samples) == 1  # Should skip invalid line
        finally:
            temp_path.unlink()
    
    def test_file_not_found(self):
        """Test error handling for non-existent file."""
        with pytest.raises(FileNotFoundError):
            load_code_samples(Path("nonexistent.jsonl"))


class TestCombine:
    """Test cases for combine function."""
    
    def test_combine_valid_results(self):
        """Test combining valid static analysis and LLM results."""
        sample = CodeSample(
            id="test_1",
            source_type="test",
            language="python",
            code="print('hello')"
        )
        
        static_issue = StaticIssue(
            tool="bandit",
            test_id="B101",
            severity="LOW",
            confidence="HIGH",
            line_number=1,
            description="Use of assert detected"
        )
        
        sa_result = StaticAnalysisResult(
            sample_id="test_1",
            num_issues=1,
            num_high=0,
            num_medium=0,
            num_low=1,
            issues=[static_issue]
        )
        
        llm_issue = LLMIssue(
            type="Code Quality",
            severity="low",
            description="Minor issue"
        )
        
        llm_result = LLMEvalResult(
            sample_id="test_1",
            security_score=4.5,
            vulnerable=False,
            issues=[llm_issue],
            raw_response={}
        )
        
        combined = combine(sample, sa_result, llm_result)
        
        assert combined.sample_id == "test_1"
        assert combined.static_num_issues == 1
        assert combined.static_low == 1
        assert combined.llm_security_score == 4.5
        assert combined.llm_vulnerable == False
        assert combined.llm_num_issues == 1


class TestStaticAnalysis:
    """Test cases for static analysis functions."""
    
    @patch('subprocess.run')
    def test_run_bandit_success(self, mock_run):
        """Test successful Bandit execution."""
        # Mock Bandit output
        mock_output = {
            "results": [
                {
                    "test_id": "B101",
                    "issue_severity": "LOW",
                    "issue_confidence": "HIGH",
                    "line_number": 1,
                    "issue_text": "Use of assert detected"
                }
            ]
        }
        
        mock_proc = Mock()
        mock_proc.returncode = 1  # Bandit found issues
        mock_proc.stdout = json.dumps(mock_output)
        mock_proc.stderr = ""
        mock_run.return_value = mock_proc
        
        result = run_bandit("assert True", "test_1")
        
        assert result.num_issues == 1
        assert result.num_low == 1
        assert len(result.issues) == 1
    
    def test_run_static_analysis_non_python(self):
        """Test static analysis for non-Python code."""
        sample = CodeSample(
            id="test_1",
            source_type="test",
            language="javascript",
            code="console.log('hello')"
        )
        
        result = run_static_analysis(sample)
        
        assert result.num_issues == 0
        assert result.sample_id == "test_1"


class TestRunExperiment:
    """Test cases for run_experiment function."""
    
    @patch('security_eval.run_static_analysis')
    @patch('security_eval.run_llm_eval')
    @patch('security_eval.ensure_llm_ready')
    def test_run_experiment_success(self, mock_llm_ready, mock_llm, mock_static):
        """Test successful experiment execution."""
        # Setup mocks
        mock_static.return_value = StaticAnalysisResult(
            sample_id="test_1",
            num_issues=0,
            num_high=0,
            num_medium=0,
            num_low=0,
            issues=[]
        )
        
        mock_llm.return_value = LLMEvalResult(
            sample_id="test_1",
            security_score=5.0,
            vulnerable=False,
            issues=[],
            raw_response={}
        )
        
        # Create temporary JSONL file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            f.write(json.dumps({
                "id": "test_1",
                "source_type": "test",
                "code": "print('hello')"
            }) + "\n")
            temp_path = Path(f.name)
        
        # Create temporary output file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            output_path = Path(f.name)
        
        try:
            df = run_experiment(temp_path, output_path, max_samples=1)
            assert len(df) == 1
            assert df.iloc[0]['sample_id'] == "test_1"
            assert df.iloc[0]['llm_security_score'] == 5.0
            assert output_path.exists()
        finally:
            temp_path.unlink()
            if output_path.exists():
                output_path.unlink()
    
    def test_run_experiment_negative_max_samples(self):
        """Test error handling for negative max_samples."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            f.write(json.dumps({
                "id": "test_1",
                "source_type": "test",
                "code": "x = 1"
            }) + "\n")
            temp_path = Path(f.name)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            output_path = Path(f.name)
        
        try:
            with pytest.raises(ValueError):
                run_experiment(temp_path, output_path, max_samples=-1)
        finally:
            temp_path.unlink()
            if output_path.exists():
                output_path.unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

