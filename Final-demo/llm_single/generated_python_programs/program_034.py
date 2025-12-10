import sys
from typing import List, Tuple


def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merge overlapping intervals.

    Args:
        intervals: A list of tuples where each tuple represents an interval (start, end).

    Returns:
        A new list of merged intervals sorted by their start time.

    Raises:
        ValueError: If any interval is not a tuple of two integers or if start > end in any interval.
    """
    if not isinstance(intervals, list):
        raise TypeError("Input must be a list of tuples.")

    # Validate intervals
    for interval in intervals:
        if (not isinstance(interval, tuple) or len(interval) != 2 or
                not all(isinstance(x, int) for x in interval)):
            raise ValueError("Each interval must be a tuple of two integers.")
        if interval[0] > interval[1]:
            raise ValueError(f"Interval start must not be greater than end: {interval}")

    # Sort intervals by the start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged = []
    for interval in sorted_intervals:
        if not merged or merged[-1][1] < interval[0]:
            # No overlap, add interval to merged list
            merged.append(interval)
        else:
            # Overlap detected, merge with the last interval
            last_start, last_end = merged[-1]
            merged[-1] = (last_start, max(last_end, interval[1]))

    return merged


def main():
    example_intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    try:
        merged_result = merge_intervals(example_intervals)
        print("Merged intervals:", merged_result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()