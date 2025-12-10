# llm_single - Summary

## Overview

The `llm_single` directory contains a simplified version of the code security evaluation system designed for evaluating a **single model/dataset** instead of comparing multiple models.

## Key Differences from llm_multi

| Feature | llm_multi | llm_single |
|---------|-----------|-------------|
| **Input** | Three JSONL files (Plain, Rule, Rule+RL) | Single JSONL file |
| **Visualizations** | Comparison graphs between datasets | Single dataset analysis |
| **Use Case** | Compare multiple code generation approaches | Evaluate one model/dataset |
| **Complexity** | More complex (comparisons) | Simpler (single analysis) |

## Files Created

1. **evaluate_single.py** - Main evaluation script
   - Evaluates a single JSONL file
   - Generates single-dataset visualizations
   - Same evaluation methods (Static Analysis + LLM)

2. **README.md** - Project overview and quick start guide

3. **TUTORIAL.md** - Complete step-by-step tutorial

4. **requirements.txt** - Python dependencies

5. **example_usage.py** - Example code for programmatic usage

## Usage

### Basic Command

```bash
python evaluate_single.py --dataset your_code_samples.jsonl
```

### With Options

```bash
python evaluate_single.py \
    --dataset data.jsonl \
    --output results/ \
    --name "MyModel" \
    --max-samples 10
```

## Output Files

The system generates:

- **CSV Results**: Detailed evaluation results for all samples
- **Summary Statistics**: Comprehensive statistics table
- **7 Visualization Graphs**:
  1. Security score distribution (histogram)
  2. Security score box plot
  3. Vulnerability summary
  4. Static analysis breakdown
  5. LLM issues distribution
  6. Security score vs static issues (scatter plot)
  7. Summary statistics table (visual)

## Evaluation Methods

Same as llm_multi:
- **Static Analysis (Bandit)**: Pattern-based vulnerability detection
- **LLM Evaluation (GPT-4.1-mini)**: Semantic security assessment

## When to Use llm_single vs llm_multi

**Use llm_single when:**
- You have one model/dataset to evaluate
- You want detailed analysis of a single approach
- You don't need comparisons
- You want simpler, focused results

**Use llm_multi when:**
- You have multiple models/datasets to compare
- You want to see relative performance
- You need comparison visualizations
- You're doing comparative research

## Integration

Both systems use the same underlying evaluation code from `LLM evaluation/`:
- Same static analysis (Bandit)
- Same LLM evaluation (GPT-4.1-mini)
- Same data structures and formats
- Compatible results format

## Next Steps

1. Prepare your JSONL file with code samples
2. Set up OpenAI API key
3. Run evaluation: `python evaluate_single.py --dataset your_file.jsonl`
4. Review results in `evaluation_results/` directory

---

**Created**: 2024
**Based on**: llm_multi evaluation system

