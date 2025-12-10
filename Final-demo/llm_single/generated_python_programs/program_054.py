import csv
import sys
from collections import defaultdict

def calculate_average_scores(filename):
    """
    Reads a CSV file with student names and scores,
    calculates the average score per student,
    and returns a list of tuples (name, average_score) sorted by average_score descending.
    """
    scores = defaultdict(list)

    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row_num, row in enumerate(reader, start=1):
                if len(row) != 2:
                    print(f"Warning: Skipping invalid row {row_num}: {row}", file=sys.stderr)
                    continue
                name, score_str = row
                name = name.strip()
                score_str = score_str.strip()
                if not name:
                    print(f"Warning: Skipping row {row_num} with empty name: {row}", file=sys.stderr)
                    continue
                try:
                    score = float(score_str)
                except ValueError:
                    print(f"Warning: Invalid score '{score_str}' at row {row_num}. Skipping.", file=sys.stderr)
                    continue
                scores[name].append(score)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    # Calculate averages
    averages = []
    for name, score_list in scores.items():
        if score_list:
            avg = sum(score_list) / len(score_list)
            averages.append((name, avg))

    # Sort by average descending, name ascending for tie-breaker
    averages.sort(key=lambda x: (-x[1], x[0]))

    return averages

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Calculate average test scores per student from a CSV file.")
    parser.add_argument('csvfile', help="Path to the CSV file with format 'Name,Score' per line")

    args = parser.parse_args()

    averages = calculate_average_scores(args.csvfile)

    if not averages:
        print("No valid student scores found.")
        return

    print(f"{'Student':<20} {'Average Score':>15}")
    print("-" * 35)
    for name, avg in averages:
        print(f"{name:<20} {avg:15.2f}")

if __name__ == "__main__":
    main()