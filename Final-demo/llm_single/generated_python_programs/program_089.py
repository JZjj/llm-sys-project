def longest_increasing_contiguous_subsequence(nums):
    """
    Returns the length of the longest strictly increasing contiguous subsequence in the list.

    :param nums: List[int] - The input list of integers.
    :return: int - Length of the longest increasing contiguous subsequence.
    :raises TypeError: if input is not a list of integers.
    """
    # Validate input type
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

    if not nums:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length


def main():
    # Example usage
    try:
        example_input = [2, 3, 5, 6, 7, 8, 1, 2]
        result = longest_increasing_contiguous_subsequence(example_input)
        print(f"Input: {example_input}")
        print(f"Output: {result} (Longest increasing contiguous subsequence length)")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()