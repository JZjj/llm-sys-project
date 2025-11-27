

# Single-Model Code Generation Evaluation

This repository implements **Part 1 of our LLM Code Generation framework**.
We study how different prompting strategies influence vulnerability removal and code quality when improving C programs from the **CASTLE Benchmark**.

---

## Overview

This project evaluates three prompting strategies for secure code refinement using a *single* LLM backend (Groq API):

* **Zero-shot prompting**
* **Few-shot prompting**
* **Evaluation-metric-based prompting** (e.g., combining outputs with vulnerability metrics)

All methods take original C files from CASTLE, send them to an LLM for security improvement, and save the rewritten code.
We then compare the outputs across prompting methods to evaluate their security effectiveness.

---

## Project Structure

```
.
├── single_model.py          # Main script for running all experiments
├── improved_c_code/         # Output from zero-shot prompting
├── improved_c_code_few_shot/ # Output from few-shot prompting
├── improved_c_code_metric/  # Output from evaluation-metric-based prompting
├── data/
│   └── CASTLE-Benchmark/    # Automatically cloned CASTLE repository
│   └── file_listing.txt     # List of C files used in experiments
└── README.md                # This file
```

---

## Prompting Methods

### 1. **Zero-shot secure code refinement**

The LLM is directly asked to:

* identify vulnerabilities (buffer overflow, format string bugs, integer overflow, memory issues)
* rewrite the code securely
* output only improved C code

### 2. **Few-shot prompting**

We provide examples of insecure → secure rewrites:

* use of `gets` → `fgets`
* off-by-one loop → safe loop
  The model must follow these styles to rewrite CASTLE code.

### 3. **Evaluation-metric-based prompting**
TBD.



---
## How to Run

### Install dependencies

```bash
pip install groq
```

### Set environment variable

```bash
export GROQ_API_KEY="your_api_key"
```

### Run the full pipeline

```bash
python single_model.py
```

The script will:

1. Clone CASTLE Benchmark
2. Extract all C files
3. Run Zero-shot, Few-shot, and Metric-based prompting
4. Save all refined C code into separate directories

---

## Results & Comparison

TBD.

We compare:

| Method       | Vulnerability Reduction | Code Quality | Consistency | Notes                    |
| ------------ | ----------------------- | ------------ | ----------- | ------------------------ |
| Zero-shot    | TBD                     | TBD          | TBD         | Baseline                 |
| Few-shot     | TBD                     | TBD          | TBD         | More stable rewrites     |
| Metric-based | TBD                     | TBD          | TBD         | Best-performing strategy |

---

## Dataset

This project uses the **CASTLE-Benchmark** for vulnerable C source code.
The repository is automatically cloned when you run `single_model.py`.

---

## Notes

* This project is part of a larger work evaluating LLM code security.
* Only the **single-model generation pipeline** is implemented here.
* Multi-model evaluation are handled in `Multimodel`.



