import sys
from typing import List

def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence in the list.
    A consecutive subsequence consists of numbers appearing in increasing order by 1,
    not necessarily contiguous in the list.
    
    :param nums: List of integers.
    :return: Length of the longest consecutive subsequence.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(n, int) for n in nums):
        raise ValueError("All elements in the list must be integers.")
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count upwards for consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

def main():
    try:
        example = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_subsequence(example)
        print(f"Longest consecutive subsequence length: {result}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()