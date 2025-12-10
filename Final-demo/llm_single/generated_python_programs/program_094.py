import sys
from collections import deque
from typing import List


def longest_subarray_with_diff_at_most_one(nums: List[int]) -> int:
    """
    Returns the length of the longest contiguous subarray where the difference
    between the maximum and minimum elements is at most 1.

    Args:
        nums (List[int]): List of integers.

    Returns:
        int: Length of the longest valid subarray.

    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")
    if not nums:
        return 0

    max_dq = deque()  # Will store elements in decreasing order for max
    min_dq = deque()  # Will store elements in increasing order for min
    left = 0
    max_length = 0

    for right, num in enumerate(nums):
        # Maintain max_dq for maximum elements
        while max_dq and num > max_dq[-1]:
            max_dq.pop()
        max_dq.append(num)

        # Maintain min_dq for minimum elements
        while min_dq and num < min_dq[-1]:
            min_dq.pop()
        min_dq.append(num)

        # Shrink window if condition violated
        while max_dq[0] - min_dq[0] > 1:
            # Remove elements going out of the window from deques
            if nums[left] == max_dq[0]:
                max_dq.popleft()
            if nums[left] == min_dq[0]:
                min_dq.popleft()
            left += 1

        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length


def main():
    example_lists = [
        [1, 2, 2, 3, 4, 2, 2, 1],
        [4, 6, 5, 3, 3, 1],
        [10, 10, 10, 10],
        [],
        [1],
        [3, 4, 5, 6, 5, 4, 3, 2, 1]
    ]

    for idx, lst in enumerate(example_lists, 1):
        try:
            result = longest_subarray_with_diff_at_most_one(lst)
            print(f"Example {idx}: Input: {lst} -> Longest subarray length: {result}")
        except Exception as e:
            print(f"Example {idx}: Input: {lst} -> Error: {str(e)}", file=sys.stderr)


if __name__ == "__main__":
    main()