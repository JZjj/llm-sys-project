 # Complete Tutorial: Code Security Evaluation System

This comprehensive tutorial will guide you through installing, setting up, and using the code security evaluation system.

## Table of Contents

1. [Installation](#installation)
2. [Environment Setup](#environment-setup)
3. [Quick Start](#quick-start)
4. [Detailed Usage](#detailed-usage)
5. [Understanding Results](#understanding-results)
6. [Advanced Features](#advanced-features)
7. [Troubleshooting](#troubleshooting)
8. [Examples](#examples)

---

## Installation

### Prerequisites

Before installing, ensure you have:
- **Python 3.8 or higher** (Python 3.9+ recommended)
- **pip** (Python package installer)
- **OpenAI API key** (for LLM-based evaluation)

### Step 1: Navigate to Project Directory

```bash
cd "LLM evaluation"
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Or install individually:
pip install pandas openai bandit pytest
```

### Step 4: Verify Installation

```bash
# Check Python version
python --version  # Should be 3.8+

# Verify packages
python -c "import pandas, openai; print('All packages installed!')"

# Verify Bandit
bandit --version
```

---

## Environment Setup

### Setting Up OpenAI API Key

The LLM evaluation requires an OpenAI API key. Set it up using one of these methods:

#### Method 1: Environment Variable (Recommended)

```bash
# On macOS/Linux:
export OPENAI_API_KEY="your-api-key-here"

# On Windows (Command Prompt):
set OPENAI_API_KEY=your-api-key-here

# On Windows (PowerShell):
$env:OPENAI_API_KEY="your-api-key-here"
```

#### Method 2: .env File

Create a `.env` file in the `LLM evaluation` directory:

```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

Then install python-dotenv and load it:
```bash
pip install python-dotenv
```

#### Method 3: Direct Configuration

You can also set it directly in Python (not recommended for production):
```python
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'
```

### Verify API Key

```bash
python -c "from openai import OpenAI; client = OpenAI(); print('API key configured!')"
```

---

## Quick Start

### Basic Evaluation

The simplest way to evaluate your code samples:

```bash
# Evaluate a JSONL file
python security_eval.py --dataset data.jsonl --out results.csv
```

This will:
1. Load code samples from the JSONL file
2. Run static analysis (Bandit) on each sample
3. Run LLM evaluation (GPT-4.1-mini) on each sample
4. Combine results and save to CSV

### Quick Test (Limited Samples)

For testing with fewer samples (faster, lower cost):

```bash
# Evaluate only 5 samples
python security_eval.py --dataset data.jsonl --out results.csv --max-samples 5
```

---

## Detailed Usage

### Command-Line Options

```bash
python security_eval.py [OPTIONS]

Required:
  --dataset PATH    Path to the JSONL file containing code samples
  --out PATH       Path to output CSV file for results

Optional:
  --max-samples N  Maximum number of samples to evaluate (for testing)
```

### Input File Format

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

### Output Format

The output CSV file contains detailed evaluation results:

- `sample_id`: Unique identifier
- `source_type`: Source of the code
- `language`: Programming language
- `static_num_issues`: Total static analysis issues
- `static_high`: High-severity issues
- `static_medium`: Medium-severity issues
- `static_low`: Low-severity issues
- `llm_security_score`: Security score (1-5)
- `llm_vulnerable`: Vulnerability flag
- `llm_num_issues`: Number of LLM-detected issues
- `static_issues_json`: Detailed static analysis issues (JSON)
- `llm_issues_json`: Detailed LLM-detected issues (JSON)

---

## Understanding Results

### Security Scores

- **5.0**: Excellent security, no issues detected
- **4.0-4.9**: Good security, minor issues
- **3.0-3.9**: Moderate security, some concerns
- **2.0-2.9**: Poor security, significant issues
- **1.0-1.9**: Very poor security, critical vulnerabilities

### Static Analysis Issues

- **High**: Critical vulnerabilities requiring immediate attention
- **Medium**: Significant security concerns
- **Low**: Minor warnings or best practice violations

### LLM-Detected Issues

The LLM evaluator provides:
- **Issue Type**: Category of vulnerability (e.g., "Input Validation", "Injection")
- **Severity**: How serious the issue is (critical, high, medium, low)
- **Description**: Detailed explanation of the security concern

### Analyzing Results

```python
import pandas as pd

# Load results
df = pd.read_csv("results.csv")

# Filter vulnerable samples
vulnerable = df[df['llm_vulnerable'] == True]
print(f"Vulnerable samples: {len(vulnerable)}")

# Get high security samples
high_security = df[df['llm_security_score'] >= 4.5]
print(f"High security samples: {len(high_security)}")

# Calculate statistics
print(f"Average security score: {df['llm_security_score'].mean():.2f}")
print(f"Vulnerability rate: {(df['llm_vulnerable'].mean() * 100):.2f}%")
```

---

## Advanced Features

### Using as a Python Module

You can import and use the evaluation functions in your own scripts:

```python
from pathlib import Path
from security_eval import run_experiment, load_code_samples, combine
from static_analysis import run_static_analysis
from llm_eval import run_llm_eval

# Load samples
samples = load_code_samples(Path("data.jsonl"))

# Run evaluation
results_df = run_experiment(
    Path("data.jsonl"),
    Path("results.csv"),
    max_samples=10
)

# Custom evaluation
sample = samples[0]
static_result = run_static_analysis(sample)
llm_result = run_llm_eval(sample)
combined = combine(sample, static_result, llm_result)
```

### Batch Processing

For processing multiple files:

```python
from pathlib import Path
from security_eval import run_experiment

jsonl_files = ["file1.jsonl", "file2.jsonl", "file3.jsonl"]

for file_path in jsonl_files:
    output_path = Path(file_path).stem + "_results.csv"
    run_experiment(Path(file_path), output_path)
```

---

## Troubleshooting

### Common Issues

#### 1. Import Errors

**Problem:**
```
ModuleNotFoundError: No module named 'openai'
```

**Solution:**
```bash
pip install -r requirements.txt
```

#### 2. OpenAI API Errors

**Problem:**
```
RuntimeError: OpenAI client not initialized. Set OPENAI_API_KEY.
```

**Solution:**
- Verify your API key is set: `echo $OPENAI_API_KEY`
- Check API key format (should start with `sk-`)
- Ensure you have API credits available
- Try setting it again: `export OPENAI_API_KEY="your-key"`

#### 3. Bandit Not Found

**Problem:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'bandit'
```

**Solution:**
```bash
pip install bandit
bandit --version
```

#### 4. File Not Found

**Problem:**
```
FileNotFoundError: JSONL file not found: data.jsonl
```

**Solution:**
- Check the file path is correct
- Use absolute path if needed: `--dataset /full/path/to/data.jsonl`

#### 5. Memory Issues

**Problem:**
Script runs out of memory with large files

**Solution:**
- Use `--max-samples` to limit evaluation
- Process files in batches
- Increase system memory

#### 6. Slow Performance

**Problem:**
Evaluation takes too long

**Solutions:**
- Use `--max-samples` for testing
- Process files in parallel (modify script)
- Use faster LLM model (modify `MODEL` in `llm_eval.py`)

### Getting Help

If you encounter issues not covered here:

1. Check the error message carefully
2. Review the logs (logging is enabled)
3. Verify all dependencies are installed
4. Check file permissions and paths
5. Review the code documentation

---

## Examples

### Example 1: Basic Evaluation

```bash
python security_eval.py --dataset test.jsonl --out results.csv
```

### Example 2: Limited Samples

```bash
python security_eval.py --dataset test.jsonl --out results.csv --max-samples 10
```

### Example 3: Python Script Usage

```python
#!/usr/bin/env python3
"""Example: Custom evaluation script."""

from pathlib import Path
from security_eval import run_experiment

# Run evaluation
results_df = run_experiment(
    Path("my_code_samples.jsonl"),
    Path("my_results.csv"),
    max_samples=20
)

# Analyze results
print(f"Evaluated {len(results_df)} samples")
print(f"Average security score: {results_df['llm_security_score'].mean():.2f}")
```

### Example 4: Analyzing Results

```python
import pandas as pd
import json

# Load results
df = pd.read_csv("results.csv")

# Filter vulnerable samples
vulnerable = df[df['llm_vulnerable'] == True]
print(f"Found {len(vulnerable)} vulnerable samples")

# Get samples with high security scores
high_security = df[df['llm_security_score'] >= 4.5]
print(f"Found {len(high_security)} high-security samples")

# Analyze static issues
with_issues = df[df['static_num_issues'] > 0]
print(f"Samples with static analysis issues: {len(with_issues)}")

# Parse JSON issues for a specific sample
sample_issues = json.loads(df.iloc[0]['llm_issues_json'])
for issue in sample_issues:
    print(f"  - {issue['type']}: {issue['description']}")
```

---

## Best Practices

1. **Start Small**: Use `--max-samples` for initial testing
2. **Save Results**: Keep CSV files for later analysis
3. **Monitor Costs**: LLM API calls cost money - monitor usage
4. **Version Control**: Track changes to evaluation code
5. **Documentation**: Document any custom modifications
6. **Testing**: Run unit tests before major changes: `pytest test_evaluation.py`

---

## Next Steps

- Review the generated CSV files
- Analyze the results for security insights
- Read `LLM_EVALUATION_EXPLANATION.md` to understand LLM evaluation
- Modify the code to suit your specific needs

---

## Support

For questions or issues:
1. Review this tutorial
2. Check the code documentation
3. Review error messages and logs
4. Consult the project README files


