"""
Unit tests for the code security evaluation system.

This module contains comprehensive unit tests for all major components
of the evaluation system, including:
- Code sample loading
- Result combination
- Error handling
- Data validation

Run tests with: pytest test_evaluation.py -v
Run with coverage: pytest test_evaluation.py --cov=. --cov-report=html
"""

import pytest
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import pandas as pd
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "LLM evaluation"))

from evaluate_and_visualize import (
    load_code_samples,
    combine,
    run_evaluation,
    create_comparison_graphs
)
from utils import CodeSample, CombinedResult
from static_analysis import StaticAnalysisResult, StaticIssue
from llm_eval import LLMEvalResult, LLMIssue


class TestLoadCodeSamples:
    """Test cases for load_code_samples function."""
    
    def test_load_valid_jsonl(self):
        """Test loading a valid JSONL file with proper format."""
        # Create temporary JSONL file
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


class TestRunEvaluation:
    """Test cases for run_evaluation function."""
    
    @patch('evaluate_and_visualize.run_static_analysis')
    @patch('evaluate_and_visualize.run_llm_eval')
    def test_run_evaluation_success(self, mock_llm, mock_static):
        """Test successful evaluation of code samples."""
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
        
        try:
            df = run_evaluation(temp_path, max_samples=1)
            assert len(df) == 1
            assert df.iloc[0]['sample_id'] == "test_1"
            assert df.iloc[0]['llm_security_score'] == 5.0
        finally:
            temp_path.unlink()
    
    def test_run_evaluation_max_samples(self):
        """Test limiting number of samples."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            for i in range(5):
                f.write(json.dumps({
                    "id": f"test_{i}",
                    "source_type": "test",
                    "code": f"x = {i}"
                }) + "\n")
            temp_path = Path(f.name)
        
        try:
            with patch('evaluate_and_visualize.run_static_analysis') as mock_static, \
                 patch('evaluate_and_visualize.run_llm_eval') as mock_llm:
                mock_static.return_value = StaticAnalysisResult(
                    sample_id="test", num_issues=0, num_high=0, num_medium=0, num_low=0, issues=[]
                )
                mock_llm.return_value = LLMEvalResult(
                    sample_id="test", security_score=5.0, vulnerable=False, issues=[], raw_response={}
                )
                
                df = run_evaluation(temp_path, max_samples=2)
                assert len(df) == 2
        finally:
            temp_path.unlink()
    
    def test_run_evaluation_negative_max_samples(self):
        """Test error handling for negative max_samples."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            f.write(json.dumps({
                "id": "test_1",
                "source_type": "test",
                "code": "x = 1"
            }) + "\n")
            temp_path = Path(f.name)
        
        try:
            with pytest.raises(ValueError):
                run_evaluation(temp_path, max_samples=-1)
        finally:
            temp_path.unlink()


class TestCreateComparisonGraphs:
    """Test cases for create_comparison_graphs function."""
    
    def test_create_graphs_valid_data(self, tmp_path):
        """Test graph creation with valid data."""
        # Create sample data
        df1 = pd.DataFrame({
            'llm_security_score': [4.5, 5.0, 4.8],
            'llm_vulnerable': [False, False, False],
            'llm_num_issues': [0, 0, 1],
            'static_num_issues': [0, 1, 0],
            'static_high': [0, 0, 0],
            'static_medium': [0, 1, 0],
            'static_low': [0, 0, 0]
        })
        
        df2 = pd.DataFrame({
            'llm_security_score': [4.7, 4.9, 5.0],
            'llm_vulnerable': [False, False, False],
            'llm_num_issues': [0, 0, 0],
            'static_num_issues': [0, 0, 1],
            'static_high': [0, 0, 0],
            'static_medium': [0, 0, 0],
            'static_low': [0, 0, 1]
        })
        
        results_dict = {
            'Dataset1': df1,
            'Dataset2': df2
        }
        
        output_dir = tmp_path / "graphs"
        create_comparison_graphs(results_dict, output_dir)
        
        # Check that files were created
        assert (output_dir / 'security_score_comparison.png').exists()
        assert (output_dir / 'vulnerability_rate_comparison.png').exists()
        assert (output_dir / 'static_analysis_comparison.png').exists()
        assert (output_dir / 'summary_statistics.csv').exists()
    
    def test_create_graphs_empty_dict(self):
        """Test error handling for empty results dictionary."""
        with pytest.raises(ValueError):
            create_comparison_graphs({}, Path("output"))
    
    def test_create_graphs_missing_columns(self):
        """Test error handling for missing required columns."""
        df = pd.DataFrame({'wrong_column': [1, 2, 3]})
        results_dict = {'Dataset1': df}
        
        with pytest.raises(ValueError):
            create_comparison_graphs(results_dict, Path("output"))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

