def longest_consecutive_subsequence(nums):
    """
    Finds the length of the longest consecutive subsequence in a list of integers.

    Args:
        nums (list): List of integers.

    Returns:
        int: Length of the longest consecutive subsequence.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only try to build sequences from numbers that are the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


def main():
    # Example usage
    try:
        example_list = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_subsequence(example_list)
        print(f"Longest consecutive subsequence length: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()