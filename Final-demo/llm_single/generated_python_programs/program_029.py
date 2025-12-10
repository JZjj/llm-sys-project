def longest_consecutive_subsequence(nums):
    """
    Finds the length of the longest consecutive subsequence in the list.
    A consecutive subsequence consists of numbers appearing in increasing order by 1,
    not necessarily contiguous in the original list.

    :param nums: List[int] - list of integers
    :return: int - length of the longest consecutive subsequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the input list must be integers.")

    num_set = set(nums)
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
    """
    Example usage of longest_consecutive_subsequence function.
    """
    test_lists = [
        [100, 4, 200, 1, 3, 2],
        [10, 5, 12, 3, 55, 30, 4, 11, 2],
        [],
        [1],
        [1, 2, 2, 3],
        [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    ]

    for idx, test_list in enumerate(test_lists, 1):
        try:
            result = longest_consecutive_subsequence(test_list)
            print(f"Test case {idx}: Input: {test_list}")
            print(f"Longest consecutive subsequence length: {result}\n")
        except (TypeError, ValueError) as e:
            print(f"Test case {idx} failed with error: {e}\n")


if __name__ == "__main__":
    main()