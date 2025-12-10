```python
#!/usr/bin/env python3
"""
This program defines a function to find the length of the longest strictly increasing subsequence
in a list of integers using an efficient O(n log n) dynamic programming approach.
It includes input validation and handles edge cases gracefully.
"""

import sys
from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    """
    Returns the length of the longest strictly increasing subsequence in nums.
    Uses a dynamic programming approach with binary search to achieve O(n log n) time complexity.

    Parameters:
        nums (List[int]): A list of integers.

    Returns:
        int: Length of the longest strictly increasing subsequence.

    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    for i, num in enumerate(nums):
        if not isinstance(num, int):
            raise TypeError(f"All elements must be integers. Element at index {i} is not an integer.")

    if not nums:
        return 0

    tails: List[int] = []

    for num in nums:
        idx = bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num

    return len(tails)


def main() -> None:
    """
    Main function to demonstrate usage of length_of_lis function.
    It reads a list of integers from standard input and prints the length of the LIS.
    """
    print("Enter a list of integers separated by spaces:")
    try:
        line = sys.stdin.readline()
        str_nums = line.strip().split()

        if not str_nums:
            print("Input is empty. Length of LIS is 0.")
            return

        nums = []
        for i, s in enumerate(str_nums):
            try:
                num = int(s)
                nums.append(num)
            except ValueError:
                print(f"Invalid integer input at position {i}: '{s}'")
                return

        result = length_of_lis(nums)
        print(f"Length of the longest strictly increasing subsequence is: {result}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```