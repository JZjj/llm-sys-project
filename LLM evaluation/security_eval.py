import argparse
import json
from pathlib import Path
from dataclasses import asdict
import pandas as pd

from utils import CodeSample, CombinedResult
from static_analysis import run_static_analysis
from llm_eval import run_llm_eval, ensure_llm_ready


# Dataset Loader

def load_code_samples(path: Path):
    samples = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            samples.append(
                CodeSample(
                    id=obj["id"],
                    source_type=obj["source_type"],
                    language=obj.get("language", "python"),
                    code=obj["code"],
                )
            )
    return samples


# Combine Results

def combine(sample, sa, llm):
    return CombinedResult(
        sample_id=sample.id,
        source_type=sample.source_type,
        language=sample.language,

        static_num_issues=sa.num_issues,
        static_high=sa.num_high,
        static_medium=sa.num_medium,
        static_low=sa.num_low,

        llm_security_score=llm.security_score,
        llm_vulnerable=llm.vulnerable,
        llm_num_issues=len(llm.issues),

        static_issues_json=json.dumps([asdict(i) for i in sa.issues]),
        llm_issues_json=json.dumps([asdict(i) for i in llm.issues]),
    )


# Experiment Runner

def run_experiment(dataset: Path, out_csv: Path, max_samples=None):
    ensure_llm_ready()

    samples = load_code_samples(dataset)
    if max_samples:
        samples = samples[:max_samples]

    combined_results = []

    for idx, sample in enumerate(samples, 1):
        print(f"[{idx}/{len(samples)}] Evaluating sample {sample.id}...")

        sa_res = run_static_analysis(sample)
        llm_res = run_llm_eval(sample)

        combined_results.append(combine(sample, sa_res, llm_res))

    df = pd.DataFrame([asdict(r) for r in combined_results])
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_csv, index=False)

    print(f"\nSaved results to: {out_csv}")


# CLI

def parse_args():
    parser = argparse.ArgumentParser(description="Part 1 Security Evaluation")
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--out", type=str, required=True)
    parser.add_argument("--max-samples", type=int, default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    run_experiment(Path(args.dataset), Path(args.out), args.max_samples)


if __name__ == "__main__":
    main()
