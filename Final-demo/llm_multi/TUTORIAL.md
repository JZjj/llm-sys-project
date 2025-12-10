# Complete Tutorial: Code Security Evaluation System

This comprehensive tutorial will guide you through installing, setting up, and using the code security evaluation system to evaluate and compare different code generation approaches.

---

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
- **Git** (optional, for cloning the repository)
- **OpenAI API key** (for LLM-based evaluation)

### Step 1: Clone or Navigate to the Project

```bash
# If you have the project in a repository
git clone <repository-url>
cd llm-sys-project-main/llm_multi

# Or navigate to the existing project directory
cd /path/to/llm-sys-project-main/llm_multi
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
pip install pandas numpy matplotlib seaborn openai bandit pytest
```

### Step 4: Verify Installation

```bash
# Check Python version
python --version  # Should be 3.8+

# Verify packages
python -c "import pandas, numpy, matplotlib, seaborn, openai; print('All packages installed!')"

# Verify Bandit (static analysis tool)
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

Create a `.env` file in the `llm_multi` directory:

```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

Then install python-dotenv and load it in your script:
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
# Evaluate all three JSONL files with default settings
python evaluate_and_visualize.py
```

This will:
1. Load code samples from three JSONL files
2. Run static analysis (Bandit) on each sample
3. Run LLM evaluation (GPT-4.1-mini) on each sample
4. Generate comparison graphs
5. Save results to `evaluation_results/` directory

### Quick Test (Limited Samples)

For testing with fewer samples (faster, lower cost):

```bash
# Evaluate only 5 samples from each file
python evaluate_and_visualize.py --max-samples 5
```

---

## Detailed Usage

### Command-Line Options

```bash
python evaluate_and_visualize.py [OPTIONS]

Options:
  --max-samples N    Maximum number of samples to evaluate per file
                     (default: None, evaluates all samples)
                     Example: --max-samples 10
```

### Input File Format

Your JSONL files should have the following format (one JSON object per line):

```json
{"id": "sample_1", "source_type": "llm_plain", "language": "python", "code": "print('hello')"}
{"id": "sample_2", "source_type": "llm_rule", "language": "python", "code": "x = 1 + 2"}
```

**Required fields:**
- `id`: Unique identifier for the code sample
- `source_type`: Source of the code (e.g., "llm_plain", "llm_rule", "llm_rule_rl")
- `code`: The actual source code to evaluate

**Optional fields:**
- `language`: Programming language (defaults to "python")

### Output Structure

After running the evaluation, you'll find:

```
evaluation_results/
├── plain_results.csv              # Detailed results for Plain dataset
├── rule_results.csv               # Detailed results for Rule dataset
├── rule_rl_results.csv            # Detailed results for Rule+RL dataset
├── summary_statistics.csv         # Summary comparison table
├── security_score_comparison.png   # Security score distribution
├── vulnerability_rate_comparison.png  # Vulnerability rate chart
├── static_analysis_comparison.png  # Static analysis issues breakdown
├── llm_issues_count_comparison.png # LLM-detected issues distribution
├── security_score_vs_static_issues.png  # Correlation scatter plots
└── summary_statistics_table.png   # Visual summary table
```

---

## Understanding Results

### CSV Results Format

Each results CSV contains the following columns:

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

### Interpreting Security Scores

- **5.0**: Excellent security, no issues detected
- **4.0-4.9**: Good security, minor issues
- **3.0-3.9**: Moderate security, some concerns
- **2.0-2.9**: Poor security, significant issues
- **1.0-1.9**: Very poor security, critical vulnerabilities

### Understanding Graphs

1. **Security Score Comparison**: Box plot showing distribution of security scores
   - Higher scores = better security
   - Box shows quartiles, whiskers show range

2. **Vulnerability Rate**: Percentage of samples flagged as vulnerable
   - Lower is better (0% is ideal)

3. **Static Analysis Comparison**: Breakdown of issues by severity
   - Shows High, Medium, Low, and Total issues
   - Lower numbers are better

4. **LLM Issues Count**: Distribution of issues detected by LLM
   - Lower numbers indicate fewer security concerns

5. **Security Score vs Static Issues**: Scatter plot showing correlation
   - Helps identify if static issues correlate with lower security scores

---

## Advanced Features

### Using as a Python Module

You can import and use the evaluation functions in your own scripts:

```python
from pathlib import Path
from evaluate_and_visualize import (
    load_code_samples,
    run_evaluation,
    create_comparison_graphs
)

# Load samples
samples = load_code_samples(Path("data.jsonl"))

# Run evaluation
results_df = run_evaluation(Path("data.jsonl"), max_samples=10)

# Create custom graphs
results_dict = {"MyDataset": results_df}
create_comparison_graphs(results_dict, Path("output/"))
```

### Custom Evaluation

You can customize the evaluation process:

```python
from evaluate_and_visualize import run_evaluation
from static_analysis import run_static_analysis
from llm_eval import run_llm_eval
from utils import CodeSample

# Create a custom code sample
sample = CodeSample(
    id="custom_1",
    source_type="custom",
    language="python",
    code="your_code_here"
)

# Run individual evaluations
static_result = run_static_analysis(sample)
llm_result = run_llm_eval(sample)

# Process results
print(f"Security score: {llm_result.security_score}")
print(f"Static issues: {static_result.num_issues}")
```

### Batch Processing

For processing multiple files:

```python
from pathlib import Path
from evaluate_and_visualize import run_evaluation

jsonl_files = [
    "file1.jsonl",
    "file2.jsonl",
    "file3.jsonl"
]

results = {}
for file_path in jsonl_files:
    df = run_evaluation(Path(file_path))
    results[Path(file_path).stem] = df
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. **Import Errors**

**Problem:**
```
ModuleNotFoundError: No module named 'utils'
```

**Solution:**
- Ensure you're in the `llm_multi` directory
- Check that the `LLM evaluation` directory exists in the parent directory
- Verify Python path includes the parent directory

#### 2. **OpenAI API Errors**

**Problem:**
```
RuntimeError: OpenAI client not initialized. Set OPENAI_API_KEY.
```

**Solution:**
- Verify your API key is set: `echo $OPENAI_API_KEY`
- Check API key format (should start with `sk-`)
- Ensure you have API credits available
- Try setting it again: `export OPENAI_API_KEY="your-key"`

#### 3. **Bandit Not Found**

**Problem:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'bandit'
```

**Solution:**
```bash
# Install Bandit
pip install bandit

# Verify installation
bandit --version
```

#### 4. **Memory Issues with Large Files**

**Problem:**
Script runs out of memory with large JSONL files

**Solution:**
- Use `--max-samples` to limit evaluation
- Process files in batches
- Increase system memory or use a machine with more RAM

#### 5. **Graph Generation Errors**

**Problem:**
```
ValueError: Dataset missing required columns
```

**Solution:**
- Ensure all evaluation steps completed successfully
- Check that CSV files contain expected columns
- Re-run evaluation if data is corrupted

#### 6. **Slow Performance**

**Problem:**
Evaluation takes too long

**Solutions:**
- Use `--max-samples` for testing
- Process files in parallel (modify script)
- Use faster LLM model (modify `MODEL` in `llm_eval.py`)
- Cache results to avoid re-evaluation

### Getting Help

If you encounter issues not covered here:

1. Check the error message carefully
2. Review the logs (logging is enabled)
3. Verify all dependencies are installed
4. Check file permissions and paths
5. Review the code documentation

---

## Examples

### Example 1: Quick Evaluation

```bash
# Evaluate 10 samples from each dataset
python evaluate_and_visualize.py --max-samples 10
```

### Example 2: Full Evaluation

```bash
# Evaluate all samples (may take time and cost API credits)
python evaluate_and_visualize.py
```

### Example 3: Python Script Usage

```python
#!/usr/bin/env python3
"""Example: Custom evaluation script."""

from pathlib import Path
from evaluate_and_visualize import run_evaluation, create_comparison_graphs

# Evaluate a single file
results = run_evaluation(
    Path("my_code_samples.jsonl"),
    max_samples=20
)

# Save results
results.to_csv("my_results.csv", index=False)

# Create graphs
create_comparison_graphs(
    {"MyDataset": results},
    Path("my_output/")
)
```

### Example 4: Analyzing Results

```python
import pandas as pd

# Load results
df = pd.read_csv("evaluation_results/plain_results.csv")

# Filter vulnerable samples
vulnerable = df[df['llm_vulnerable'] == True]
print(f"Found {len(vulnerable)} vulnerable samples")

# Get samples with high security scores
high_security = df[df['llm_security_score'] >= 4.5]
print(f"Found {len(high_security)} high-security samples")

# Analyze static analysis issues
high_issues = df[df['static_num_issues'] > 0]
print(f"Found {len(high_issues)} samples with static analysis issues")
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

- Review the generated graphs in `evaluation_results/`
- Analyze the CSV files for detailed insights
- Read `RESULTS_INTERPRETATION.md` for result analysis
- Check `LLM_EVALUATION_EXPLANATION.md` to understand LLM evaluation
- Modify the code to suit your specific needs

---

## Support

For questions or issues:
1. Review this tutorial
2. Check the code documentation
3. Review error messages and logs
4. Consult the project README files

Happy evaluating! 🚀

