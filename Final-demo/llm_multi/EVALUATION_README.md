# Evaluation and Visualization Script

This script evaluates three jsonl files using the evaluation code from `LLM evaluation` and generates comparison graphs.

## Files Evaluated

1. `generated_python_programs.jsonl` (Plain)
2. `generated_python_programs_rule.jsonl` (Rule)
3. `generated_python_programs_rule_rl.jsonl` (Rule+RL)

## Requirements

Make sure you have the following packages installed:
```bash
pip install pandas matplotlib seaborn numpy openai bandit
```

Also ensure you have your OpenAI API key set:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

Run the evaluation script:
```bash
cd llm_multi
python evaluate_and_visualize.py
```

For testing with a limited number of samples:
```bash
python evaluate_and_visualize.py --max-samples 10
```

## Output

The script will generate:

1. **CSV files** with detailed results for each dataset:
   - `plain_results.csv`
   - `rule_results.csv`
   - `rule_rl_results.csv`

2. **Graphs** comparing the three datasets:
   - `security_score_comparison.png` - Box plot of security scores
   - `vulnerability_rate_comparison.png` - Bar chart of vulnerability rates
   - `static_analysis_comparison.png` - Grouped bar chart of static analysis issues
   - `llm_issues_count_comparison.png` - Box plot of LLM-detected issues
   - `security_score_vs_static_issues.png` - Scatter plots showing correlation
   - `summary_statistics_table.png` - Summary table visualization

3. **Summary statistics**:
   - `summary_statistics.csv` - Detailed comparison table

All outputs are saved in the `evaluation_results/` directory.

## Evaluation Metrics

The script evaluates each code sample using:

1. **Static Analysis** (Bandit):
   - Total number of issues
   - Issues by severity (High, Medium, Low)

2. **LLM Evaluation**:
   - Security score (1-5 scale)
   - Vulnerability flag (True/False)
   - Number of security issues detected

## Notes

- The evaluation may take some time as it processes all samples and makes LLM API calls
- You can modify the script to limit the number of samples by adding a `max_samples` parameter in the `main()` function
- Make sure `bandit` is installed and available in your PATH for static analysis

