def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list of integers.

    Args:
        nums (list of int): The input list of integers.

    Returns:
        int: The length of the longest consecutive subsequence.

    Raises:
        TypeError: If nums is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")
    
    num_set = set(nums)
    longest_length = 0

    for num in num_set:
        # Only try to build sequences from numbers that are the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest_length = max(longest_length, current_length)

    return longest_length


def main():
    # Example usage
    try:
        example_list = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_subsequence(example_list)
        print(f"The length of the longest consecutive subsequence is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()