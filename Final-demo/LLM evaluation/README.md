# Code Security Evaluation System

A comprehensive framework for evaluating code security using both static analysis (Bandit) and LLM-based evaluation (GPT-4.1-mini).

## Overview

This system provides a dual-method approach to code security evaluation:

1. **Static Analysis (Bandit)**: Rule-based pattern matching for known vulnerabilities
2. **LLM Evaluation (GPT-4.1-mini)**: Semantic understanding of code security

The framework combines both methods to provide comprehensive security assessment with detailed metrics and issue reporting.

## Features

**Dual Evaluation Methods**
- Static analysis for known vulnerability patterns
- LLM-based semantic understanding for contextual security assessment

**Comprehensive Metrics**
- Security scores (1-5 scale)
- Vulnerability detection
- Issue categorization by severity
- Detailed issue descriptions

**Production Ready**
- Robust error handling
- Comprehensive logging
- Unit tests
- Well-documented code
- Performance optimized

## Quick Start

### Installation

```bash
# 1. Navigate to the project directory
cd "LLM evaluation"

# 2. Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
```

### Basic Usage

```bash
# Evaluate a JSONL file
python security_eval.py --dataset data.jsonl --out results.csv

# Quick test with limited samples
python security_eval.py --dataset data.jsonl --out results.csv --max-samples 10
```

## Project Structure

```
LLM evaluation/
├── security_eval.py      # Main experiment driver
├── static_analysis.py    # Static analysis (Bandit)
├── llm_eval.py          # LLM-based security evaluator
├── utils.py             # Shared dataclasses & types
├── test_evaluation.py   # Unit tests
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── TUTORIAL.md         # Complete tutorial
```

## Requirements

- Python 3.8+
- OpenAI API key
- See `requirements.txt` for full dependency list

## Command-Line Options

```bash
python security_eval.py [OPTIONS]

Required:
  --dataset PATH    Path to the JSONL file containing code samples
  --out PATH       Path to output CSV file for results

Optional:
  --max-samples N  Maximum number of samples to evaluate (for testing)
```

## Input File Format

Your JSONL file should have the following format (one JSON object per line):

```json
{"id": "ex1", "source_type": "llm", "language": "python", "code": "def foo(x): return eval(x)"}
{"id": "ex2", "source_type": "authentic", "language": "python", "code": "def add(a,b): return a+b"}
```

**Required fields:**
- `id`: Unique identifier for the code sample
- `source_type`: Source of the code (e.g., "llm", "authentic")
- `code`: The actual source code to evaluate

**Optional fields:**
- `language`: Programming language (defaults to "python")

## Output Format

The output CSV file contains the following columns:

- `sample_id`: Unique identifier for the code sample
- `source_type`: Source of the code
- `language`: Programming language
- `static_num_issues`: Total number of static analysis issues
- `static_high`: Number of high-severity issues
- `static_medium`: Number of medium-severity issues
- `static_low`: Number of low-severity issues
- `llm_security_score`: Security score from LLM (1-5, higher is better)
- `llm_vulnerable`: Boolean flag indicating if code is vulnerable
- `llm_num_issues`: Number of issues detected by LLM
- `static_issues_json`: JSON string with detailed static analysis issues
- `llm_issues_json`: JSON string with detailed LLM-detected issues

## Evaluation Metrics

### Security Score (1-5)
- **5.0**: Excellent security, no issues detected
- **4.0-4.9**: Good security, minor issues
- **3.0-3.9**: Moderate security, some concerns
- **2.0-2.9**: Poor security, significant issues
- **1.0-1.9**: Very poor security, critical vulnerabilities

### Static Analysis
- **High**: Critical vulnerabilities
- **Medium**: Significant security concerns
- **Low**: Minor warnings

### LLM Evaluation
- **Vulnerable**: Boolean flag indicating vulnerability
- **Issues**: List of security concerns with descriptions

## Testing

Run unit tests:
```bash
pytest test_evaluation.py -v
```

Run with coverage:
```bash
pytest test_evaluation.py --cov=. --cov-report=html
```

## Code Quality

The codebase follows best practices:
- Comprehensive documentation and docstrings
- Type hints for better code clarity
- Error handling and validation
- Logging for debugging
- Unit tests for core functionality
- Clean and organized structure

## Example Usage

### Basic Evaluation
```bash
python security_eval.py --dataset test.jsonl --out results.csv
```

### Limited Samples (for testing)
```bash
python security_eval.py --dataset test.jsonl --out results.csv --max-samples 5
```

### Using as a Python Module
```python
from pathlib import Path
from security_eval import run_experiment

# Run evaluation
results_df = run_experiment(
    Path("data.jsonl"),
    Path("results.csv"),
    max_samples=10
)

# Analyze results
print(f"Evaluated {len(results_df)} samples")
print(f"Average security score: {results_df['llm_security_score'].mean():.2f}")
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure all dependencies are installed
2. **API errors**: Verify OpenAI API key is set correctly
3. **Bandit not found**: Install with `pip install bandit`
4. **File not found**: Check the path to your JSONL file

## Documentation

- **[TUTORIAL.md](TUTORIAL.md)**: Complete step-by-step guide
- **[LLM_EVALUATION_EXPLANATION.md](LLM_EVALUATION_EXPLANATION.md)**: Detailed explanation of LLM evaluation

## License

MIT License

## Support

For questions or issues:
1. Check the [TUTORIAL.md](TUTORIAL.md)
2. Review error messages and logs
3. Verify all dependencies are installed
4. Ensure API key is configured correctly

---

**Last Updated**: 2025

