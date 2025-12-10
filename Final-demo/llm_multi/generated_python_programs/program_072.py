```python
from typing import List

def can_attend_all_meetings(intervals: List[List[int]]) -> bool:
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        # If current meeting starts before previous meeting ends, overlap exists
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

def main():
    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
        ([], True),
        ([[1, 5]], True),
        ([[1, 3], [3, 6]], True),
        ([[1, 3], [2, 4]], False),
    ]

    for i, (intervals, expected) in enumerate(test_cases, 1):
        # Use a copy of intervals to avoid side effects from sorting in the function
        result = can_attend_all_meetings(intervals.copy())
        print(f"Test case {i}: Input: {intervals} -> Output: {result} (Expected: {expected})")

if __name__ == "__main__":
    main()
```