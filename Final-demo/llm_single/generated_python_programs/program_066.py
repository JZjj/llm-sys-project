import sys
from typing import List

def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive sequence of integers in the input list.
    The sequence numbers do not need to be adjacent in the list.
    
    :param nums: List of integers
    :return: Length of the longest consecutive sequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the input list must be integers.")
    if not nums:
        return 0

    nums_set = set(nums)
    longest_streak = 0

    for num in nums_set:
        # Only start counting if 'num-1' is not in set to ensure start of sequence
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1

            # Count upwards from current_num until the consecutive sequence breaks
            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    """
    Main function demonstrating example usage of longest_consecutive_sequence.
    """
    try:
        example_list = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_sequence(example_list)
        print(f"Longest consecutive sequence length: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()