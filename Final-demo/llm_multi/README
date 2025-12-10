# Complete Workflow: Code Generation and Evaluation

This document describes the complete workflow for using `llm_multi` to generate and evaluate code across three different approaches.

## Overview

The `llm_multi` system has two main components:

1. **Code Generation**: Three scripts that generate 100 Python code samples each using different approaches:
   - `main_plain.py`: Basic LLM code generation (Plain)
   - `main.py`: LLM with rule-based guidance (Rule)
   - `main_reinforcement.py`: LLM with rule-based guidance and reinforcement learning (Rule+RL)
2. **Code Evaluation** (`evaluate_and_visualize.py`): Evaluates all three datasets and generates comparison visualizations

## Complete Workflow

### Step 1: Setup Environment

```bash
# Navigate to directory
cd llm_multi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
```

### Step 2: Generate Code Samples

Generate code using all three approaches:

#### 2a. Generate Plain Code

```bash
# Generate 100 Python programs using plain approach
python main_plain.py
```

**What this does:**
- Uses multi-agent framework (planner, coder, reviewer) to generate 100 unique Python programming tasks
- For each task, generates complete Python code
- Saves each program as `generated_python_programs/program_001.py` through `program_100.py`
- Creates `generated_python_programs.jsonl` with all samples in JSONL format

**Output:**
- `generated_python_programs/` - Directory with 100 Python files
- `generated_python_programs.jsonl` - JSONL file for evaluation

#### 2b. Generate Rule-Based Code

```bash
# Generate 100 Python programs using rule-based approach
python main.py
```

**What this does:**
- Same multi-agent framework, but with security-focused rules and criteria
- Agents are guided to generate code with high security scores
- Saves each program as `generated_python_programs_rule/program_001.py` through `program_100.py`
- Creates `generated_python_programs_rule.jsonl` with all samples in JSONL format

**Output:**
- `generated_python_programs_rule/` - Directory with 100 Python files
- `generated_python_programs_rule.jsonl` - JSONL file for evaluation

#### 2c. Generate Rule+RL Code

```bash
# Generate 100 Python programs using rule-based + reinforcement learning approach
python main_reinforcement.py
```

**What this does:**
- Uses multi-agent framework with rule-based guidance AND reinforcement learning
- RL controller selects optimal coder configurations based on security evaluation feedback
- Saves each program as `generated_python_programs_rule_rl/program_001.py` through `program_100.py`
- Creates `generated_python_programs_rule_rl.jsonl` with all samples in JSONL format

**Output:**
- `generated_python_programs_rule_rl/` - Directory with 100 Python files
- `generated_python_programs_rule_rl.jsonl` - JSONL file for evaluation

**Time:** Approximately 30-90 minutes per approach (depending on API response times)

**Cost:** ~$1.50-$5.00 per approach (depending on code length and API pricing)

### Step 3: Evaluate Generated Code

After generating all three datasets, evaluate and compare them:

```bash
# Evaluate all three JSONL files and generate comparison graphs
python evaluate_and_visualize.py
```

**What this does:**
- Loads all code samples from the three JSONL files
- Runs static analysis (Bandit) on each sample
- Runs LLM evaluation (GPT-4.1-mini) on each sample
- Generates comprehensive comparison visualizations
- Saves detailed results to CSV files

**Output:**
- `evaluation_results/plain_results.csv` - Detailed results for Plain approach
- `evaluation_results/rule_results.csv` - Detailed results for Rule approach
- `evaluation_results/rule_rl_results.csv` - Detailed results for Rule+RL approach
- `evaluation_results/summary_statistics.csv` - Summary statistics table
- `evaluation_results/*.png` - 6 comparison visualization graphs

**Time:** Approximately 60-180 minutes (depending on API response times)

**Cost:** ~$3.00-$9.00 (depending on code length and API pricing)

### Step 4: Analyze Results

Review the generated visualizations and CSV files in `evaluation_results/`:

- **Security Score Comparison**: How do the three approaches compare in security scores?
- **Vulnerability Rate Comparison**: Which approach has the lowest vulnerability rate?
- **Static Analysis Comparison**: What issues did Bandit find in each approach?
- **LLM Issues Count Comparison**: How many security concerns did the LLM identify?
- **Security Score vs Static Issues**: Correlation analysis
- **Summary Statistics Table**: Comprehensive comparison table

## Quick Test Workflow

For faster testing with fewer samples:

### Option 1: Generate Fewer Samples

Edit each generation script:
```python
num_programs = 10  # Change from 100 to 10
```

Then run:
```bash
python main_plain.py
python main.py
python main_reinforcement.py
python evaluate_and_visualize.py --max-samples 10
```

### Option 2: Evaluate Limited Samples

Generate all 100, but evaluate only a subset:
```bash
python main_plain.py  # Generate 100
python main.py  # Generate 100
python main_reinforcement.py  # Generate 100
python evaluate_and_visualize.py --max-samples 10
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
│ Step 2: Generate Code (3 approaches)                    │
│                                                          │
│ ┌──────────────┐    ┌──────────────┐                   │
│ │ main_plain   │───▶│ Plain        │                   │
│ │ .py          │    │ Programs     │                   │
│ └──────────────┘    └──────┬───────┘                   │
│                            │                            │
│ ┌──────────────┐          │                            │
│ │ main.py      │───▶      │                            │
│ │ (Rule)       │    ┌─────▼──────┐                    │
│ └──────────────┘    │ Rule        │                    │
│                     │ Programs    │                    │
│ ┌──────────────┐    └──────┬──────┘                   │
│ │ main_        │          │                            │
│ │ reinforcement│───▶      │                            │
│ │ .py          │    ┌─────▼──────┐                    │
│ └──────────────┘    │ Rule+RL     │                    │
│                     │ Programs    │                    │
│                     └──────┬──────┘                   │
│                            │                            │
│                            ▼                            │
│                  ┌──────────────────┐                   │
│                  │ 3 JSONL Files   │                   │
│                  │ (for evaluation) │                   │
│                  └──────────────────┘                   │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ Step 3: Evaluate Code                                   │
│ python evaluate_and_visualize.py                        │
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
│                  │ Comparison       │                   │
│                  │ Visualizations   │                   │
│                  │ & CSV Results    │                   │
│                  └──────────────────┘                   │
└─────────────────────────────────────────────────────────┘
```

## File Flow

```
main_plain.py
    │
    ├─▶ generated_python_programs/
    │   ├── program_001.py
    │   ├── program_002.py
    │   └── ... (100 files)
    │
    └─▶ generated_python_programs.jsonl
            │
main.py
    │
    ├─▶ generated_python_programs_rule/
    │   ├── program_001.py
    │   ├── program_002.py
    │   └── ... (100 files)
    │
    └─▶ generated_python_programs_rule.jsonl
            │
main_reinforcement.py
    │
    ├─▶ generated_python_programs_rule_rl/
    │   ├── program_001.py
    │   ├── program_002.py
    │   └── ... (100 files)
    │
    └─▶ generated_python_programs_rule_rl.jsonl
            │
            ▼
    evaluate_and_visualize.py
            │
            └─▶ evaluation_results/
                ├── plain_results.csv
                ├── rule_results.csv
                ├── rule_rl_results.csv
                ├── summary_statistics.csv
                ├── security_score_comparison.png
                ├── vulnerability_rate_comparison.png
                ├── static_analysis_comparison.png
                ├── llm_issues_count_comparison.png
                ├── security_score_vs_static_issues.png
                └── summary_statistics_table.png
```

## Troubleshooting

### Generation Issues

**Problem**: API errors during generation
- **Solution**: Check API key, ensure sufficient credits, wait and retry

**Problem**: Generation stops partway
- **Solution**: Scripts save progress incrementally, you can resume or restart

**Problem**: JSONL file not created
- **Solution**: Ensure generation scripts completed successfully and check file permissions

### Evaluation Issues

**Problem**: JSONL files not found
- **Solution**: Ensure all three generation scripts (`main_plain.py`, `main.py`, `main_reinforcement.py`) completed successfully

**Problem**: Evaluation too slow
- **Solution**: Use `--max-samples` to limit evaluation

**Problem**: Missing one of the three JSONL files
- **Solution**: The evaluation script requires all three files. Generate the missing one using the appropriate script.

## Best Practices

1. **Generate All Three First**: Always generate all three approaches before evaluating
2. **Save API Costs**: Use `--max-samples` for testing
3. **Check Results**: Review generated code quality before evaluation
4. **Backup Data**: Keep JSONL files for reproducibility
5. **Monitor Costs**: Track API usage during generation and evaluation
6. **Run Sequentially**: Run generation scripts one at a time to avoid API rate limits

## Next Steps

After completing the workflow:

1. Review the comparison visualization graphs
2. Analyze the CSV results for each approach
3. Compare security metrics across the three approaches
4. Use insights to improve code generation prompts and strategies

---

**Complete Workflow Time**: ~90-270 minutes (30-90 min per generation + 60-180 min evaluation)
**Total Cost**: ~$7.50-$24.00 (depending on code complexity and API pricing)

