#!/usr/bin/env python3
"""
Module to find the length of the longest consecutive integer subsequence in a list.

The subsequence does not need to be contiguous in the original list but must consist of consecutive integers.
"""

from typing import List


def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Find the length of the longest consecutive subsequence in the list.

    Args:
        nums (List[int]): List of integers.

    Returns:
        int: Length of the longest consecutive subsequence.

    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

    # Convert the list to a set for O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if num-1 is not in the set (start of a sequence)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers starting from current_num
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    """
    Example usage of longest_consecutive_subsequence function.
    """
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),            # sequence: 1,2,3,4
        ([0, -1, 1, 2, -2, -3], 4),             # sequence: -3,-2,-1,0,1,2 longest is 4 (example: -3,-2,-1,0)
        ([10, 30, 20, 40], 1),                   # no consecutive sequences longer than 1
        ([1, 2, 2, 3], 3),                       # duplicates handled properly
        ([], 0),                                 # empty list returns 0
        ([7], 1),                                # single element list
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7) # sequence: 3,4,5,6,7,8,9
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        try:
            result = longest_consecutive_subsequence(nums)
            print(f"Test case {i}: Input: {nums}")
            print(f"Expected: {expected}, Result: {result}")
            assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        except Exception as e:
            print(f"Test case {i} raised an exception: {e}")
        print("-" * 40)


if __name__ == "__main__":
    main()