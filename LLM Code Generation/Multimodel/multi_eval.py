import textwrap
import traceback
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable, Tuple, Optional

# =========================
# 1. TASK + TEST DEFINITION
# =========================

@dataclass
class TestCase:
    input_args: tuple
    input_kwargs: dict
    expected_output: Any
    description: str = ""

@dataclass
class CodingTask:
    name: str
    description: str
    function_name: str
    test_cases: List[TestCase] = field(default_factory=list)

# Example: you can add more tasks later
def sample_task() -> CodingTask:
    """
    Simple example: implement add(a, b) that returns a + b.
    """
    return CodingTask(
        name="add_two_numbers",
        description=(
            "Write a Python function `add(a, b)` that returns the sum of a and b. "
            "Assume a and b are integers."
        ),
        function_name="add",
        test_cases=[
            TestCase((1, 2), {}, 3, "1 + 2 = 3"),
            TestCase((-1, 5), {}, 4, "-1 + 5 = 4"),
            TestCase((0, 0), {}, 0, "0 + 0 = 0"),
            TestCase((100, 200), {}, 300, "100 + 200 = 300"),
        ],
    )

# =========================================
# 2. LLM CALL PLACEHOLDERS (YOU PLUG THESE)
# =========================================

def call_llm(model_name: str, system_prompt: str, user_prompt: str) -> str:
    """
    Placeholder function that actually calls the LLM.

    Replace this with real API call, e.g. OpenAI, DeepSeek, etc.

    Example with OpenAI's Chat Completions (pseudo-code):

    from openai import OpenAI
    client = OpenAI()

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content
    """
    # For now, raise to remind you to plug real LLM.
    raise NotImplementedError("Implement call_llm() with your LLM provider.")


def generate_code_with_tests(model_name: str, task: CodingTask) -> str:
    system_prompt = (
        "You are an expert Python programmer. "
        "You will be given a task description and unit tests. "
        "Write a single Python function that passes all the tests. "
        "Only output code, no explanation, no backticks."
    )

    test_descriptions = "\n".join(
        f"- {tc.description}: {task.function_name}{tc.input_args} -> {tc.expected_output}"
        for tc in task.test_cases
    )

    user_prompt = f"""
TASK:
{task.description}

TARGET FUNCTION NAME:
{task.function_name}

UNIT TESTS (ENGLISH DESCRIPTION):
{test_descriptions}

REQUIREMENTS:
- Implement a single function named {task.function_name}.
- Do not include any other top-level code (no prints, no I/O, no test-running code).
- Only output valid Python code with the function implementation.
"""

    return call_llm(model_name, system_prompt, textwrap.dedent(user_prompt))


def generate_code_without_tests(model_name: str, task: CodingTask) -> str:
    system_prompt = (
        "You are an expert Python programmer. "
        "You will be given a task description. "
        "Write a single Python function that solves the task. "
        "Only output code, no explanation, no backticks."
    )

    user_prompt = f"""
TASK:
{task.description}

REQUIREMENTS:
- Implement a single function named {task.function_name}.
- Do not include any other top-level code (no prints, no I/O, no test-running code).
- Only output valid Python code with the function implementation.
"""

    return call_llm(model_name, system_prompt, textwrap.dedent(user_prompt))


def repair_code_with_feedback(
    model_name: str,
    task: CodingTask,
    previous_code: str,
    test_report: str,
) -> str:
    system_prompt = (
        "You are an expert Python programmer and bug fixer. "
        "You will be given an existing function and a test failure report. "
        "Your job is to fix the code so that it passes all tests. "
        "Only output the corrected code, no explanation, no backticks."
    )

    user_prompt = f"""
TASK:
{task.description}

FUNCTION NAME: {task.function_name}

CURRENT CODE:
{previous_code}

TEST FAILURE REPORT:
{test_report}

REQUIREMENTS:
- Correct the code so that it passes all the tests implied by the failure report.
- Do not add any I/O or print statements.
- Only output the fixed function (valid Python code).
"""

    return call_llm(model_name, system_prompt, textwrap.dedent(user_prompt))

# ==========================
# 3. TEST RUNNING UTILITIES
# ==========================

@dataclass
class TestResult:
    passed: bool
    error: Optional[str] = None
    traceback: Optional[str] = None

@dataclass
class EvaluationResult:
    task_name: str
    model_name: str
    variant: str  # e.g. "with_tests_initial", "with_tests_repaired", "without_tests"
    code: str
    test_results: Dict[int, TestResult]

    @property
    def num_passed(self) -> int:
        return sum(1 for r in self.test_results.values() if r.passed)

    @property
    def num_failed(self) -> int:
        return sum(1 for r in self.test_results.values() if not r.passed)

def run_tests_on_code(task: CodingTask, code: str) -> Dict[int, TestResult]:
    """
    Dynamically defines the function from the generated code and runs test cases.
    WARNING: Uses exec(), so run in a sandbox / controlled environment.
    """
    global_namespace = {}
    local_namespace = {}

    try:
        exec(code, global_namespace, local_namespace)
    except Exception as e:
        tb = traceback.format_exc()
        return {
            i: TestResult(
                passed=False,
                error=f"Code execution error before running tests: {e}",
                traceback=tb,
            )
            for i, _ in enumerate(task.test_cases)
        }

    if task.function_name not in local_namespace:
        # Function not defined
        return {
            i: TestResult(
                passed=False,
                error=f"Function `{task.function_name}` not defined in generated code.",
            )
            for i, _ in enumerate(task.test_cases)
        }

    func = local_namespace[task.function_name]
    results: Dict[int, TestResult] = {}

    for idx, tc in enumerate(task.test_cases):
        try:
            output = func(*tc.input_args, **tc.input_kwargs)
            if output == tc.expected_output:
                results[idx] = TestResult(passed=True)
            else:
                results[idx] = TestResult(
                    passed=False,
                    error=f"Expected {tc.expected_output}, got {output}",
                )
        except Exception as e:
            tb = traceback.format_exc()
            results[idx] = TestResult(
                passed=False,
                error=f"Exception during execution: {e}",
                traceback=tb,
            )

    return results

def format_test_report(task: CodingTask, test_results: Dict[int, TestResult]) -> str:
    lines = []
    for idx, tc in enumerate(task.test_cases):
        r = test_results[idx]
        status = "PASSED" if r.passed else "FAILED"
        line = f"Test {idx}: {status} - {tc.description}"
        if not r.passed and r.error:
            line += f" | Error: {r.error}"
        lines.append(line)
    return "\n".join(lines)

# ==========================
# 4. MAIN EXPERIMENT DRIVER
# ==========================

def experiment_for_task(
    task: CodingTask,
    models: List[str],
    max_repair_rounds: int = 3,
) -> List[EvaluationResult]:
    all_results: List[EvaluationResult] = []

    for model_name in models:
        print(f"\n=== MODEL: {model_name} | TASK: {task.name} ===")

        # ----- Variant 1: with tests & repair loop -----
        print("Generating code WITH tests...")
        code_with_tests = generate_code_with_tests(model_name, task)
        initial_results = run_tests_on_code(task, code_with_tests)
        eval_initial = EvaluationResult(
            task_name=task.name,
            model_name=model_name,
            variant="with_tests_initial",
            code=code_with_tests,
            test_results=initial_results,
        )
        all_results.append(eval_initial)

        current_code = code_with_tests
        current_results = initial_results

        for repair_round in range(1, max_repair_rounds + 1):
            if all(r.passed for r in current_results.values()):
                print(f"All tests passed after {repair_round - 1} repair rounds.")
                break

            print(f"Repair round {repair_round}...")
            report = format_test_report(task, current_results)
            repaired_code = repair_code_with_feedback(
                model_name=model_name,
                task=task,
                previous_code=current_code,
                test_report=report,
            )
            repaired_results = run_tests_on_code(task, repaired_code)

            eval_repaired = EvaluationResult(
                task_name=task.name,
                model_name=model_name,
                variant=f"with_tests_repair_round_{repair_round}",
                code=repaired_code,
                test_results=repaired_results,
            )
            all_results.append(eval_repaired)

            current_code = repaired_code
            current_results = repaired_results

        # ----- Variant 2: without tests / no repair -----
        print("Generating code WITHOUT tests...")
        code_without_tests = generate_code_without_tests(model_name, task)
        results_without_tests = run_tests_on_code(task, code_without_tests)
        eval_without = EvaluationResult(
            task_name=task.name,
            model_name=model_name,
            variant="without_tests",
            code=code_without_tests,
            test_results=results_without_tests,
        )
        all_results.append(eval_without)

    return all_results

# ==========================
# 5. SUMMARY / BUG METRICS
# ==========================

def summarize_results(results: List[EvaluationResult]) -> None:
    """
    Print comparison table:
    - For each model:
      - initial with-tests pass/fail
      - best with-tests (after repair) pass/fail
      - without-tests pass/fail
      - "bugs dissolved" = failed_tests_initial - failed_tests_best
    """
    summary: Dict[Tuple[str, str], Dict[str, Any]] = {}

    for res in results:
        key = (res.task_name, res.model_name)
        if key not in summary:
            summary[key] = {
                "initial": None,
                "best_with_tests": None,
                "without_tests": None,
            }

        if res.variant == "with_tests_initial":
            summary[key]["initial"] = res
        elif res.variant.startswith("with_tests_repair_round_"):
            # Track best (fewest failures)
            current_best = summary[key]["best_with_tests"]
            if current_best is None or res.num_failed < current_best.num_failed:
                summary[key]["best_with_tests"] = res
        elif res.variant == "without_tests":
            summary[key]["without_tests"] = res

    print("\n===== SUMMARY =====")
    for (task_name, model_name), data in summary.items():
        initial = data["initial"]
        best = data["best_with_tests"] or initial
        without = data["without_tests"]

        initial_fail = initial.num_failed if initial else None
        best_fail = best.num_failed if best else None
        without_fail = without.num_failed if without else None

        bugs_dissolved = None
        if initial_fail is not None and best_fail is not None:
            bugs_dissolved = initial_fail - best_fail

        print(f"\nTask: {task_name} | Model: {model_name}")
        print(f"- With tests (initial):    passed {initial.num_passed}/{len(initial.test_results)}, failed {initial_fail}")
        print(f"- With tests (best):       passed {best.num_passed}/{len(best.test_results)}, failed {best_fail}")
        print(f"- Without tests:           passed {without.num_passed}/{len(without.test_results)}, failed {without_fail}")
        if bugs_dissolved is not None:
            print(f"- Bugs dissolved by repair loop: {bugs_dissolved}")

# ==========================
# 6. ENTRY POINT
# ==========================

if __name__ == "__main__":
    # Define tasks (you can add more later)
    task = sample_task()

    # List of models (multi-LLM)
    models = [
        "gpt-4.1-mini",    # example
        "gpt-4.1"          # example
        # add your other models here
    ]

    results = experiment_for_task(task, models, max_repair_rounds=3)
    summarize_results(results)
