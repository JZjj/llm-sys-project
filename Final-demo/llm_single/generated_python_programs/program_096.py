from typing import List


def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence in the list of integers.
    A consecutive subsequence consists of numbers that appear consecutively in increasing order,
    but not necessarily contiguous in the list.

    :param nums: List of integers
    :return: Length of the longest consecutive subsequence
    :raises TypeError: If input is not a list of integers
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count upwards from current_num
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    """
    Main function demonstrating example usage of longest_consecutive_subsequence().
    """
    examples = [
        [100, 4, 200, 1, 3, 2],
        [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
        [],
        [1],
        [10, 9, 8, 7, 6, 5],
    ]

    for i, example in enumerate(examples, 1):
        try:
            result = longest_consecutive_subsequence(example)
            print(f"Example {i}: Input: {example} -> Longest consecutive subsequence length: {result}")
        except Exception as e:
            print(f"Example {i}: Input: {example} -> Error: {e}")


if __name__ == "__main__":
    main()