```python
#!/usr/bin/env python3
"""
This program defines a function to find the length of the longest strictly increasing subsequence
in a list of integers with time complexity O(n log n).
"""

from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    """
    Computes the length of the longest strictly increasing subsequence in nums.

    Args:
        nums (List[int]): The input list of integers.

    Returns:
        int: The length of the longest strictly increasing subsequence.
    """
    if not nums:
        return 0

    # tails[i] holds the smallest possible tail value for an increasing subsequence of length i+1
    tails = []

    for num in nums:
        # Find the insertion position to maintain sorted order in tails
        idx = bisect_left(tails, num)
        # If num is larger than any element in tails, append it
        if idx == len(tails):
            tails.append(num)
        else:
            # Replace tails[idx] with num to keep the smallest possible tail value
            tails[idx] = num

    return len(tails)


def main() -> None:
    # Example usage and simple test cases
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([], 0),
        ([1, 2, 3, 4, 5], 5),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = length_of_lis(nums)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    print("All test cases passed.")


if __name__ == "__main__":
    main()
```