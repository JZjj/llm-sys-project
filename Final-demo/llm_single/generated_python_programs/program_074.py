def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list `nums`.
    Consecutive subsequence means numbers that appear consecutively in value,
    but not necessarily consecutively in the list.

    :param nums: List[int] - list of integers
    :return: int - length of the longest consecutive subsequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in the list must be integers.")

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers after `num`
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    # Example usage
    example = [100, 4, 200, 1, 3, 2]
    try:
        length = longest_consecutive_subsequence(example)
        print(f"Longest consecutive subsequence length: {length}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()