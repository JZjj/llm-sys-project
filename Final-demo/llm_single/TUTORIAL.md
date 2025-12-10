# Tutorial: Single Model Code Security Evaluation

This tutorial will guide you through using the single model code security evaluation system.

## Table of Contents

1. [Installation](#installation)
2. [Environment Setup](#environment-setup)
3. [Quick Start](#quick-start)
4. [Understanding Results](#understanding-results)
5. [Advanced Usage](#advanced-usage)
6. [Troubleshooting](#troubleshooting)

---

## Installation

### Prerequisites

- **Python 3.8 or higher** (Python 3.9+ recommended)
- **pip** (Python package installer)
- **OpenAI API key** (for LLM-based evaluation)

### Step 1: Navigate to Project Directory

```bash
cd llm_single
```

### Step 2: Create Virtual Environment (Recommended)

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
```

### Step 4: Verify Installation

```bash
# Check Python version
python --version  # Should be 3.8+

# Verify packages
python -c "import pandas, numpy, matplotlib, seaborn, openai; print('All packages installed!')"

# Verify Bandit
bandit --version
```

---

## Environment Setup

### Setting Up OpenAI API Key

The LLM evaluation requires an OpenAI API key. Set it up:

```bash
# On macOS/Linux:
export OPENAI_API_KEY="your-api-key-here"

# On Windows (Command Prompt):
set OPENAI_API_KEY=your-api-key-here

# On Windows (PowerShell):
$env:OPENAI_API_KEY="your-api-key-here"
```

### Verify API Key

```bash
python -c "from openai import OpenAI; client = OpenAI(); print('API key configured!')"
```

---

## Quick Start

### Step 1: Generate Code Samples

First, you need to generate code samples to evaluate:

```bash
# Generate 100 Python code samples
python generate_code.py
```

This will:
1. Generate 100 Python programs using GPT-4.1-mini
2. Save each program as a separate `.py` file in `generated_python_programs/`
3. Create `generated_python_programs.jsonl` file containing all samples for evaluation
4. Show progress for each generated program

**Note**: This step requires OpenAI API access and will make API calls. Ensure your API key is set.

### Step 2: Evaluate Generated Code

After generating code, evaluate it:

```bash
# Evaluate the generated code
python evaluate_single.py --dataset generated_python_programs.jsonl --name "SingleModel"
```

This will:
1. Load code samples from the JSONL file
2. Run static analysis (Bandit) on each sample
3. Run LLM evaluation (GPT-4.1-mini) on each sample
4. Generate visualizations
5. Save results to `evaluation_results/` directory

### Alternative: Evaluate Existing Code

If you already have a JSONL file with code samples:

```bash
# Evaluate a JSONL file
python evaluate_single.py --dataset your_code_samples.jsonl
```

### Quick Test (Limited Samples)

For testing with fewer samples (faster, lower cost):

```bash
# Generate only 10 samples (modify NUM_PROGRAMS in generate_code.py)
# Or evaluate only 5 samples from existing file
python evaluate_single.py --dataset data.jsonl --max-samples 5
```

---

## Understanding Results

### CSV Results Format

The results CSV contains the following columns:

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

1. **Security Score Distribution**: Histogram showing distribution of security scores
   - Higher scores = better security
   - Shows how many samples fall into each score range

2. **Security Score Box Plot**: Box plot showing quartiles and outliers
   - Median, quartiles, and range of security scores

3. **Vulnerability Summary**: Bar chart showing vulnerable vs safe samples
   - Shows count and percentage of vulnerable samples

4. **Static Analysis Breakdown**: Bar chart of issues by severity
   - Shows High, Medium, Low, and Total issues

5. **LLM Issues Distribution**: Histogram of LLM-detected issues
   - Shows how many samples have 0, 1, 2, etc. issues

6. **Security Score vs Static Issues**: Scatter plot showing correlation
   - Helps identify if static issues correlate with lower security scores

7. **Summary Statistics Table**: Comprehensive statistics table
   - All key metrics in one place

---

## Advanced Usage

### Custom Output Directory

```bash
python evaluate_single.py \
    --dataset data.jsonl \
    --output my_results/
```

### Custom Dataset Name

```bash
python evaluate_single.py \
    --dataset data.jsonl \
    --name "MyCustomModel"
```

### Using as a Python Module

You can import and use the evaluation functions:

```python
from pathlib import Path
from evaluate_single import (
    load_code_samples,
    run_evaluation,
    create_visualizations
)

# Load samples
samples = load_code_samples(Path("data.jsonl"))

# Run evaluation
results_df = run_evaluation(Path("data.jsonl"), max_samples=10)

# Create visualizations
create_visualizations(results_df, Path("output/"), "MyDataset")
```

---

## Troubleshooting

### Common Issues

#### 1. Import Errors

**Problem:**
```
ModuleNotFoundError: No module named 'utils'
```

**Solution:**
- Ensure you're in the `llm_single` directory
- Check that the `LLM evaluation` directory exists in the parent directory

#### 2. OpenAI API Errors

**Problem:**
```
RuntimeError: OpenAI client not initialized. Set OPENAI_API_KEY.
```

**Solution:**
- Verify your API key is set: `echo $OPENAI_API_KEY`
- Check API key format (should start with `sk-`)
- Ensure you have API credits available

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
Error: File not found: data.jsonl
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

---

## Best Practices

1. **Start Small**: Use `--max-samples` for initial testing
2. **Save Results**: Keep CSV files for later analysis
3. **Monitor Costs**: LLM API calls cost money - monitor usage
4. **Check Logs**: Review logs for any warnings or errors

---

## Next Steps

- Review the generated graphs in `evaluation_results/`
- Analyze the CSV file for detailed insights
- Compare results across different models or datasets
- Modify the code to suit your specific needs

---


