import sys
from typing import List

def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence in the list.
    The subsequence numbers must appear in increasing order without gaps,
    but do not need to be contiguous in the list.

    Args:
        nums (List[int]): List of integers.

    Returns:
        int: Length of the longest consecutive subsequence.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")

    num_set = set(nums)  # O(n) space for quick look-ups
    max_length = 0

    for num in num_set:
        # Only start counting when num-1 is not in set to avoid redundant work
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

def main():
    # Example usage
    example_list = [2, 6, 1, 9, 4, 5, 3]
    try:
        result = longest_consecutive_subsequence(example_list)
        print(f"Longest consecutive subsequence length: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()