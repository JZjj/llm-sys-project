import csv
import sys
from collections import defaultdict
from typing import Dict, List, Tuple


def read_grades_from_csv(file_path: str) -> Dict[str, List[float]]:
    """
    Reads student grades from a CSV file.

    :param file_path: Path to the CSV file
    :return: Dictionary mapping student names to lists of their grades
    """
    grades = defaultdict(list)
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for line_number, row in enumerate(reader, start=1):
                if len(row) != 2:
                    print(f"Warning: Skipping malformed line {line_number}: {row}", file=sys.stderr)
                    continue
                name, grade_str = row
                name = name.strip()
                grade_str = grade_str.strip()
                if not name:
                    print(f"Warning: Empty student name on line {line_number}", file=sys.stderr)
                    continue
                try:
                    grade = float(grade_str)
                except ValueError:
                    print(f"Warning: Invalid grade '{grade_str}' on line {line_number}", file=sys.stderr)
                    continue
                grades[name].append(grade)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error: I/O error({e.errno}): {e.strerror}", file=sys.stderr)
        sys.exit(1)
    return grades


def calculate_average_grades(grades: Dict[str, List[float]]) -> Dict[str, float]:
    """
    Calculates the average grade for each student.

    :param grades: Dictionary mapping student names to lists of grades
    :return: Dictionary mapping student names to their average grade
    """
    average_grades = {}
    for student, grade_list in grades.items():
        if grade_list:
            average = sum(grade_list) / len(grade_list)
            average_grades[student] = average
    return average_grades


def print_average_grades(average_grades: Dict[str, float]) -> None:
    """
    Prints the average grade for each student.

    :param average_grades: Dictionary mapping student names to their average grade
    """
    if not average_grades:
        print("No grades to display.")
        return
    for student in sorted(average_grades.keys()):
        avg = average_grades[student]
        print(f"{student}: {avg:.2f}")


def main() -> None:
    """
    Main function to demonstrate program usage.
    Expects a CSV file path as the first command-line argument.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <grades_csv_file>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    grades = read_grades_from_csv(file_path)
    average_grades = calculate_average_grades(grades)
    print_average_grades(average_grades)


if __name__ == "__main__":
    main()