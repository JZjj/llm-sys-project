from typing import List


def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence where elements appear in order
    and are consecutive integers, but not necessarily contiguous in the list.

    Args:
        nums (List[int]): List of integers.

    Returns:
        int: Length of the longest consecutive subsequence.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")
    if not nums:
        return 0

    # Dictionary to store the length of the longest consecutive subsequence ending with key
    subseq_lengths = {}

    max_length = 0
    for num in nums:
        # Check if there is a subsequence ending with num - 1
        prev_length = subseq_lengths.get(num - 1, 0)
        # Current subsequence length ending with num
        subseq_lengths[num] = prev_length + 1
        if subseq_lengths[num] > max_length:
            max_length = subseq_lengths[num]

    return max_length


def main():
    # Example usage with provided example and additional test cases
    try:
        examples = [
            [10, 4, 20, 1, 3, 2, 5],
            [],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [100, 4, 200, 1, 3, 2],
            [1, 3, 5, 7],
        ]
        for example in examples:
            length = longest_consecutive_subsequence(example)
            print(f"Input: {example}\nLongest consecutive subsequence length: {length}\n")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()