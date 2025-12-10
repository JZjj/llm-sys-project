def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list of integers.

    Args:
        nums (list of int): The input list of integers.

    Returns:
        int: Length of the longest consecutive subsequence.

    Raises:
        TypeError: If the input is not a list of integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")

    num_set = set(nums)  # Use a set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


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