def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence
    in the list of integers nums.
    The subsequence numbers are consecutive integers but do not have
    to be contiguous in the list.

    :param nums: List[int] - list of integers
    :return: int - length of longest consecutive subsequence
    :raises TypeError: if input is not a list or contains non-integers
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All items in the list must be integers.")

    num_set = set(nums)  # Use a set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only check for the start of a sequence
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
    examples = [
        [100, 4, 200, 1, 3, 2],
        [],
        [10, 5, 12, 3, 55, 30, 4, 11, 2],
        [1, 2, 2, 3],
        [7],
        [9, 8, 7, 6, 5],
    ]

    for i, example in enumerate(examples, 1):
        try:
            result = longest_consecutive_subsequence(example)
            print(f"Example {i}: Input: {example} -> Longest consecutive subsequence length: {result}")
        except Exception as e:
            print(f"Example {i}: Input: {example} -> Error: {e}")


if __name__ == "__main__":
    main()