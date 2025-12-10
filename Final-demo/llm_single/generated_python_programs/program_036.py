from typing import List

def longest_consecutive_increasing_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence of numbers
    that appear in strictly increasing order in the given list.

    :param nums: List of integers
    :return: Length of the longest strictly increasing consecutive subsequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements of the input list must be integers.")

    max_length = 0
    current_length = 0
    previous = None

    for num in nums:
        if previous is None or num > previous:
            current_length += 1
        else:
            current_length = 1
        previous = num
        if current_length > max_length:
            max_length = current_length

    return max_length


def main():
    # Example usage
    try:
        example_list = [1, 2, 2, 3, 4, 1, 2, 3]
        result = longest_consecutive_increasing_subsequence(example_list)
        print(f"Longest consecutive increasing subsequence length: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()