```python
#!/usr/bin/env python3
"""
Module to compute the length of the longest increasing subsequence in a list of integers.

The subsequence does not need to be contiguous.

This implementation uses a dynamic programming approach with binary search
to achieve O(n log n) time complexity.

Author: Senior Python Engineer
Date: 2024-06-02
"""

from typing import List


def length_of_lis(nums: List[int]) -> int:
    """
    Calculate the length of the longest strictly increasing subsequence.

    Parameters:
        nums (List[int]): A list of integers.

    Returns:
        int: Length of the longest increasing subsequence.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if any(not isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

    # tails[i] holds the smallest tail of all increasing subsequences of length i+1
    tails = []

    for num in nums:
        # Binary search for the insertion point of num in tails
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        # If num is larger than any element in tails, append it
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num

    return len(tails)


def main():
    # Example usage and simple test cases
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([], 0),
        ([1], 1),
        ([4, 10, 4, 3, 8, 9], 3),
    ]

    for idx, (nums, expected) in enumerate(test_cases, 1):
        try:
            result = length_of_lis(nums)
            assert result == expected, f"Test case {idx} failed: expected {expected}, got {result}"
            print(f"Test case {idx} passed: length_of_lis({nums}) == {result}")
        except Exception as e:
            print(f"Test case {idx} raised an exception: {e}")

    # Demonstrate error handling
    invalid_inputs = [
        None,
        [1, 2, "3"],
        "not a list",
        [1.5, 2, 3],
        [{'a': 1}, 2, 3],
    ]
    for i, invalid_input in enumerate(invalid_inputs, 1):
        try:
            length_of_lis(invalid_input)
        except TypeError as e:
            print(f"Invalid input test {i} correctly raised TypeError: {e}")
        except Exception as e:
            print(f"Invalid input test {i} raised unexpected exception type: {type(e).__name__}: {e}")
        else:
            print(f"Invalid input test {i} failed to raise TypeError")


if __name__ == "__main__":
    main()
```