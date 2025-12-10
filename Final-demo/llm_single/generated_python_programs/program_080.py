import csv
import sys
from typing import List, Tuple


def read_scores(input_file: str) -> List[Tuple[str, List[float]]]:
    """
    Read student scores from a CSV file.
    Returns a list of tuples: (student_name, [scores])
    Raises ValueError if scores cannot be converted to float.
    """
    students = []
    try:
        with open(input_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader, None)
            if headers is None or len(headers) < 2:
                raise ValueError("CSV must have at least two columns: name and one score.")
            for row_num, row in enumerate(reader, start=2):
                if len(row) < 2:
                    # Skip rows with insufficient columns
                    continue
                name = row[0].strip()
                if not name:
                    # Skip rows with empty student name
                    continue
                scores = []
                for i, score_str in enumerate(row[1:], start=2):
                    score_str = score_str.strip()
                    if score_str == '':
                        # Treat empty scores as zero or skip? Here we skip row for data integrity
                        raise ValueError(f"Empty score found at row {row_num} column {i}")
                    try:
                        score = float(score_str)
                    except ValueError:
                        raise ValueError(f"Invalid score '{score_str}' at row {row_num} column {i}")
                    scores.append(score)
                students.append((name, scores))
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_file}' not found.")
    except IOError as e:
        raise IOError(f"Error reading file '{input_file}': {e}")
    return students


def calculate_averages(students: List[Tuple[str, List[float]]]) -> List[Tuple[str, float]]:
    """
    Calculate average scores for each student.
    Returns a list of tuples: (student_name, average_score)
    """
    averages = []
    for name, scores in students:
        if not scores:
            avg = 0.0
        else:
            avg = sum(scores) / len(scores)
        averages.append((name, avg))
    return sorted(averages, key=lambda x: x[1], reverse=True)


def write_averages(output_file: str, averages: List[Tuple[str, float]]) -> None:
    """
    Write student averages to a CSV file.
    Columns: Name, Average
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Average'])
            for name, avg in averages:
                writer.writerow([name, f'{avg:.2f}'])
    except IOError as e:
        raise IOError(f"Error writing to file '{output_file}': {e}")


def main():
    """
    Example usage of the program.
    Reads 'students_scores.csv' and writes 'students_averages.csv'.
    """
    input_file = 'students_scores.csv'
    output_file = 'students_averages.csv'
    try:
        students = read_scores(input_file)
        averages = calculate_averages(students)
        write_averages(output_file, averages)
        print(f"Averages calculated and saved to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()