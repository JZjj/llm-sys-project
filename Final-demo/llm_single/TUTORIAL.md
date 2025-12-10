# Complete Workflow: Code Generation and Evaluation

This document describes the complete workflow for using `llm_single` to generate and evaluate code.

## Overview

The `llm_single` system has two main components:

1. **Code Generation** (`generate_code.py`): Generates 100 Python code samples
2. **Code Evaluation** (`evaluate_single.py`): Evaluates code security using dual methods

## Complete Workflow

### Step 1: Setup Environment

```bash
# Navigate to directory
cd llm_single

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
```

### Step 2: Generate Code Samples

```bash
# Generate 100 Python programs
python generate_code.py
```

**What this does:**
- Uses GPT-4.1-mini to generate 100 unique Python programming tasks
- For each task, generates complete Python code
- Saves each program as `generated_python_programs/program_001.py` through `program_100.py`
- Creates `generated_python_programs.jsonl` with all samples in JSONL format

**Output:**
- `generated_python_programs/` - Directory with 100 Python files
- `generated_python_programs.jsonl` - JSONL file for evaluation

**Time:** Approximately 10-30 minutes (depending on API response times)

**Cost:** ~$0.50-$2.00 (depending on code length and API pricing)

### Step 3: Evaluate Generated Code

```bash
# Evaluate all generated samples
python evaluate_single.py --dataset generated_python_programs.jsonl --name "SingleModel"
```

**What this does:**
- Loads all code samples from the JSONL file
- Runs static analysis (Bandit) on each sample
- Runs LLM evaluation (GPT-4.1-mini) on each sample
- Generates comprehensive visualizations
- Saves detailed results to CSV

**Output:**
- `evaluation_results/singlemodel_results.csv` - Detailed results
- `evaluation_results/summary_statistics.csv` - Summary statistics
- `evaluation_results/*.png` - 7 visualization graphs

**Time:** Approximately 20-60 minutes (depending on API response times)

**Cost:** ~$1.00-$3.00 (depending on code length and API pricing)

### Step 4: Analyze Results

Review the generated visualizations and CSV files in `evaluation_results/`:

- **Security Score Distribution**: How secure are the generated programs?
- **Vulnerability Summary**: Are there any vulnerable samples?
- **Static Analysis Breakdown**: What issues did Bandit find?
- **LLM Issues Distribution**: What security concerns did the LLM identify?

## Quick Test Workflow

For faster testing with fewer samples:

### Option 1: Generate Fewer Samples

Edit `generate_code.py`:
```python
NUM_PROGRAMS = 10  # Change from 100 to 10
```

Then run:
```bash
python generate_code.py
python evaluate_single.py --dataset generated_python_programs.jsonl --name "Test"
```

### Option 2: Evaluate Limited Samples

Generate all 100, but evaluate only a subset:
```bash
python generate_code.py  # Generate 100
python evaluate_single.py --dataset generated_python_programs.jsonl --max-samples 10
```

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────┐
│ Step 1: Setup                                            │
│ - Install dependencies                                   │
│ - Set API key                                            │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ Step 2: Generate Code                                    │
│ python generate_code.py                                  │
│                                                          │
│ ┌──────────────┐    ┌──────────────┐                   │
│ │ GPT-4.1-mini │───▶│ 100 Python   │                   │
│ │ (Task Gen)   │    │ Programs     │                   │
│ └──────────────┘    └──────┬───────┘                   │
│                            │                            │
│                            ▼                            │
│                  ┌──────────────────┐                   │
│                  │ JSONL File       │                   │
│                  │ (for evaluation) │                   │
│                  └──────────────────┘                   │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ Step 3: Evaluate Code                                    │
│ python evaluate_single.py --dataset ...                  │
│                                                          │
│ ┌──────────────┐    ┌──────────────┐                   │
│ │ Static       │───▶│ Combined    │                   │
│ │ Analysis     │    │ Results     │                   │
│ │ (Bandit)     │    │             │                   │
│ └──────────────┘    └──────┬──────┘                   │
│                            │                            │
│ ┌──────────────┐          │                            │
│ │ LLM          │──────────┘                            │
│ │ Evaluation   │                                       │
│ │ (GPT-4.1)    │                                       │
│ └──────────────┘                                       │
│                            │                            │
│                            ▼                            │
│                  ┌──────────────────┐                   │
│                  │ Visualizations   │                   │
│                  │ & CSV Results    │                   │
│                  └──────────────────┘                   │
└─────────────────────────────────────────────────────────┘
```

## File Flow

```
generate_code.py
    │
    ├─▶ generated_python_programs/
    │   ├── program_001.py
    │   ├── program_002.py
    │   └── ... (100 files)
    │
    └─▶ generated_python_programs.jsonl
            │
            ▼
    evaluate_single.py
            │
            └─▶ evaluation_results/
                ├── singlemodel_results.csv
                ├── summary_statistics.csv
                ├── security_score_distribution.png
                ├── vulnerability_summary.png
                └── ... (7 graphs total)
```

## Troubleshooting

### Generation Issues

**Problem**: API errors during generation
- **Solution**: Check API key, ensure sufficient credits, wait and retry

**Problem**: Generation stops partway
- **Solution**: Script saves progress incrementally, you can resume or restart

### Evaluation Issues

**Problem**: JSONL file not found
- **Solution**: Ensure `generate_code.py` completed successfully

**Problem**: Evaluation too slow
- **Solution**: Use `--max-samples` to limit evaluation

## Best Practices

1. **Generate First**: Always generate code before evaluating
2. **Save API Costs**: Use `--max-samples` for testing
3. **Check Results**: Review generated code quality before evaluation
4. **Backup Data**: Keep JSONL files for reproducibility
5. **Monitor Costs**: Track API usage during generation and evaluation

## Next Steps

After completing the workflow:

1. Review the visualization graphs
2. Analyze the CSV results
3. Compare with other models/approaches
4. Use insights to improve code generation prompts

---

**Complete Workflow Time**: ~30-90 minutes
**Total Cost**: ~$1.50-$5.00 (depending on code complexity)

