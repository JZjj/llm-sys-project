# Single Model Code Security Evaluation

A comprehensive tool for evaluating code security of a single model/dataset using both static analysis (Bandit) and LLM-based evaluation (GPT-4.1-mini).

## Overview

This system evaluates code samples from a single code generation approach and provides detailed security analysis through:
- **Static Analysis**: Pattern-based vulnerability detection using Bandit
- **LLM Evaluation**: Semantic security assessment using GPT-4.1-mini
- **Visualization**: Comprehensive graphs and statistics for the single dataset

## Features

**Dual Evaluation Methods**
- Static analysis for known vulnerability patterns
- LLM-based semantic understanding for contextual security assessment

**Comprehensive Metrics**
- Security scores (1-5 scale)
- Vulnerability detection
- Issue categorization by severity
- Detailed issue descriptions

**Rich Visualizations**
- Security score distributions (histogram and box plot)
- Vulnerability summary
- Static analysis breakdown
- LLM issues distribution
- Correlation analysis
- Summary statistics table

**Production Ready**
- Robust error handling
- Comprehensive logging
- Well-documented code
- Performance optimized

## Quick Start

### Installation

```bash
# 1. Navigate to the project directory
cd llm_single

# 2. Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
```

### Step 1: Generate Code Samples

First, generate 100 Python code samples:

```bash
# Generate 100 code samples
python generate_code.py
```

This will:
- Generate 100 Python programs using GPT-4.1-mini
- Save programs to `generated_python_programs/` directory
- Create `generated_python_programs.jsonl` file for evaluation

### Step 2: Evaluate Generated Code

After generating code, evaluate it:

```bash
# Evaluate the generated code
python evaluate_single.py --dataset generated_python_programs.jsonl --name "SingleModel"
```

### Alternative: Evaluate Existing Code

If you already have a JSONL file with code samples:

```bash
# Evaluate a single JSONL file
python evaluate_single.py --dataset your_code_samples.jsonl

# With custom output directory and dataset name
python evaluate_single.py --dataset data.jsonl --output results/ --name "MyModel"

# Quick test with limited samples
python evaluate_single.py --dataset data.jsonl --max-samples 10
```

### Output

Results are saved to `evaluation_results/` (or custom output directory):
- CSV file with detailed results
- PNG graphs for visual analysis
- Summary statistics table

## Project Structure

```
llm_single/
├── generate_code.py            # Code generation script (generates 100 samples)
├── evaluate_single.py          # Main evaluation script
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── TUTORIAL.md                 # Complete tutorial
├── generated_python_programs/  # Generated Python files (created by generate_code.py)
├── generated_python_programs.jsonl  # JSONL file for evaluation (created by generate_code.py)
└── evaluation_results/         # Output directory (created by evaluate_single.py)
    ├── *_results.csv           # Detailed results
    ├── summary_statistics.csv  # Summary table
    └── *.png                   # Visualization graphs
```

## Requirements

- Python 3.8+
- OpenAI API key
- See `requirements.txt` for full dependency list

## Command-Line Options

```bash
python evaluate_single.py [OPTIONS]

Required:
  --dataset PATH    Path to the JSONL file containing code samples

Optional:
  --output PATH     Output directory (default: evaluation_results/)
  --name NAME       Dataset name for labeling (default: filename)
  --max-samples N   Maximum number of samples to evaluate (for testing)
```

## Input File Format

Your JSONL file should have the following format (one JSON object per line):

```json
{"id": "sample_1", "source_type": "llm", "language": "python", "code": "print('hello')"}
{"id": "sample_2", "source_type": "llm", "language": "python", "code": "x = 1 + 2"}
```

**Required fields:**
- `id`: Unique identifier for the code sample
- `source_type`: Source of the code (e.g., "llm", "llm_plain")
- `code`: The actual source code to evaluate

**Optional fields:**
- `language`: Programming language (defaults to "python")

## Output Files

After running the evaluation, you'll find:

```
evaluation_results/
├── dataset_results.csv              # Detailed results for all samples
├── summary_statistics.csv           # Summary statistics table
├── security_score_distribution.png  # Security score histogram
├── security_score_boxplot.png       # Security score box plot
├── vulnerability_summary.png         # Vulnerability count chart
├── static_analysis_breakdown.png    # Static analysis issues by severity
├── llm_issues_distribution.png       # LLM-detected issues histogram
├── security_score_vs_static_issues.png  # Correlation scatter plot
└── summary_statistics_table.png     # Visual summary table
```

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

## Example Usage

### Basic Evaluation
```bash
python evaluate_single.py --dataset generated_code.jsonl
```

### Custom Output
```bash
python evaluate_single.py \
    --dataset my_code.jsonl \
    --output my_results/ \
    --name "GPT-4-Generated"
```

### Quick Test
```bash
python evaluate_single.py --dataset data.jsonl --max-samples 5
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure `LLM evaluation` directory exists in parent directory
2. **API errors**: Verify OpenAI API key is set correctly
3. **Bandit not found**: Install with `pip install bandit`
4. **File not found**: Check the path to your JSONL file

## Code Quality

The codebase follows best practices:
- Comprehensive documentation and docstrings
- Type hints for better code clarity
- Error handling and validation
- Logging for debugging
- Clean and organized structure

## License

MIT License

## Support

For questions or issues:
1. Check the error messages and logs
2. Verify all dependencies are installed
3. Ensure API key is configured correctly

---

**Last Updated**: 2024

