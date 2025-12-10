import tempfile
import subprocess
import json
from pathlib import Path
from utils import StaticIssue, StaticAnalysisResult, CodeSample

def run_bandit(code: str, sample_id: str) -> StaticAnalysisResult:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_file = Path(tmp) / f"{sample_id}.py"
        tmp_file.write_text(code, encoding="utf-8")

        cmd = ["bandit", "-f", "json", "-q", str(tmp_file)]
        proc = subprocess.run(cmd, capture_output=True, text=True)

        if proc.returncode not in (0, 1):
            raise RuntimeError(f"Bandit failed: {proc.stderr}")

        try:
            report = json.loads(proc.stdout)
        except:
            report = {"results": []}

        issues = []
        high = medium = low = 0

        for r in report.get("results", []):
            sev = r.get("issue_severity", "").upper()
            if sev == "HIGH":
                high += 1
            elif sev == "MEDIUM":
                medium += 1
            else:
                low += 1

            issues.append(
                StaticIssue(
                    tool="bandit",
                    test_id=r.get("test_id", ""),
                    severity=r.get("issue_severity", ""),
                    confidence=r.get("issue_confidence", ""),
                    line_number=r.get("line_number", 0),
                    description=r.get("issue_text", "")
                )
            )

        return StaticAnalysisResult(
            sample_id=sample_id,
            num_issues=len(issues),
            num_high=high,
            num_medium=medium,
            num_low=low,
            issues=issues,
        )


def run_static_analysis(sample: CodeSample) -> StaticAnalysisResult:
    if sample.language.lower() != "python":
        return StaticAnalysisResult(sample.id, 0, 0, 0, 0, [])
    return run_bandit(sample.code, sample.id)