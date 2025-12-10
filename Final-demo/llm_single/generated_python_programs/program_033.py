#!/usr/bin/env python3

from typing import List


def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence in the list nums.

    A consecutive subsequence consists of numbers that appear consecutively in value,
    but not necessarily contiguous in the list.

    Args:
        nums (List[int]): List of integers.

    Returns:
        int: Length of the longest consecutive subsequence.

    Raises:
        TypeError: If nums is not a list of integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if any(not isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

    num_set = set(nums)  # For O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers after current_num
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    """
    Main function demonstrating the usage of longest_consecutive_subsequence().
    """
    example_lists = [
        [100, 4, 200, 1, 3, 2],
        [1, 9, 3, 10, 4, 20, 2],
        [],
        [7, 7, 7, 7],
        [10, 5, 12, 3, 55, 30, 4, 11, 2],
    ]

    for i, nums in enumerate(example_lists, 1):
        try:
            result = longest_consecutive_subsequence(nums)
            print(f"Example {i}: Input: {nums}")
            print(f"Longest consecutive subsequence length: {result}\n")
        except Exception as e:
            print(f"Example {i}: Error processing input {nums}: {e}\n")


if __name__ == "__main__":
    main()