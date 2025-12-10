# Code Security Evaluation System

A comprehensive tool for evaluating and comparing code security across different code generation approaches using both static analysis (Bandit) and LLM-based evaluation (GPT-4.1-mini).

## Overview

This system evaluates code samples from three different generation approaches:
- **Plain**: Basic LLM code generation
- **Rule**: LLM with rule-based guidance  
- **Rule+RL**: LLM with rule-based guidance and reinforcement learning

It provides detailed security analysis through:
- **Static Analysis**: Pattern-based vulnerability detection using Bandit
- **LLM Evaluation**: Semantic security assessment using GPT-4.1-mini
- **Visualization**: Comprehensive comparison graphs and statistics

## Features

✅ **Dual Evaluation Methods**
- Static analysis for known vulnerability patterns
- LLM-based semantic understanding for contextual security assessment

✅ **Comprehensive Metrics**
- Security scores (1-5 scale)
- Vulnerability detection
- Issue categorization by severity
- Detailed issue descriptions

✅ **Rich Visualizations**
- Security score distributions
- Vulnerability rate comparisons
- Static analysis breakdowns
- Correlation analysis
- Summary statistics tables

✅ **Production Ready**
- Robust error handling
- Comprehensive logging
- Unit tests
- Well-documented code
- Performance optimized

## Quick Start

### Installation

```bash
# 1. Navigate to the project directory
cd llm_multi

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
# Evaluate all three JSONL files
python evaluate_and_visualize.py

# Quick test with limited samples
python evaluate_and_visualize.py --max-samples 10
```

### Output

Results are saved to `evaluation_results/`:
- CSV files with detailed results
- PNG graphs for visual comparison
- Summary statistics table

## Documentation

- **[TUTORIAL.md](TUTORIAL.md)**: Complete step-by-step guide
- **[EVALUATION_README.md](EVALUATION_README.md)**: Evaluation system overview
- **[RESULTS_INTERPRETATION.md](RESULTS_INTERPRETATION.md)**: How to interpret results
- **[LLM evaluation/LLM_EVALUATION_EXPLANATION.md](../LLM%20evaluation/LLM_EVALUATION_EXPLANATION.md)**: LLM evaluation details

## Project Structure

```
llm_multi/
├── evaluate_and_visualize.py    # Main evaluation script
├── test_evaluation.py            # Unit tests
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── TUTORIAL.md                    # Complete tutorial
├── EVALUATION_README.md           # Evaluation guide
├── RESULTS_INTERPRETATION.md     # Results analysis
├── generated_python_programs.jsonl      # Plain dataset
├── generated_python_programs_rule.jsonl # Rule dataset
├── generated_python_programs_rule_rl.jsonl # Rule+RL dataset
└── evaluation_results/           # Output directory
    ├── *.csv                      # Detailed results
    └── *.png                      # Visualization graphs
```

## Requirements

- Python 3.8+
- OpenAI API key
- See `requirements.txt` for full dependency list

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
- ✅ Comprehensive documentation and docstrings
- ✅ Type hints for better code clarity
- ✅ Error handling and validation
- ✅ Logging for debugging
- ✅ Unit tests for core functionality
- ✅ Clean and organized structure

## Evaluation Metrics

### Security Score (1-5)
- **5.0**: Excellent security
- **4.0-4.9**: Good security
- **3.0-3.9**: Moderate security
- **2.0-2.9**: Poor security
- **1.0-1.9**: Very poor security

### Static Analysis
- **High**: Critical vulnerabilities
- **Medium**: Significant security concerns
- **Low**: Minor warnings

### LLM Evaluation
- **Vulnerable**: Boolean flag indicating vulnerability
- **Issues**: List of security concerns with descriptions

## Example Results

Based on evaluation of 100 samples per dataset:

| Dataset | Avg Security Score | Vulnerability Rate | Avg Static Issues |
|---------|-------------------|-------------------|-------------------|
| Plain   | 4.98              | 0.0%              | 0.02             |
| Rule    | 4.97              | 0.0%              | 0.16             |
| Rule+RL | 4.96              | 0.0%              | 0.20             |

All approaches produce highly secure code with minimal security concerns.

## Troubleshooting

Common issues and solutions:

1. **Import errors**: Ensure `LLM evaluation` directory exists in parent directory
2. **API errors**: Verify OpenAI API key is set correctly
3. **Bandit not found**: Install with `pip install bandit`
4. **Memory issues**: Use `--max-samples` to limit evaluation

See [TUTORIAL.md](TUTORIAL.md) for detailed troubleshooting guide.

## Contributing

When contributing:
1. Follow existing code style
2. Add unit tests for new features
3. Update documentation
4. Run tests before submitting

## License

MIT License - See LICENSE file for details

## Citation

If you use this evaluation system in your research, please cite:

```
LLM Systems Project - Code Security Evaluation System
2024
```

## Support

For questions or issues:
1. Check the [TUTORIAL.md](TUTORIAL.md)
2. Review error messages and logs
3. Consult documentation files

## Authors

LLM Systems Project Team

---

**Last Updated**: 2024

