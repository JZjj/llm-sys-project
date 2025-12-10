def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list.
    A consecutive subsequence consists of numbers that appear consecutively in increasing order,
    but not necessarily contiguous in the list.

    :param nums: List[int] - List of integers
    :return: int - Length of the longest consecutive subsequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers")

    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only start counting if 'num - 1' is not in set, meaning start of sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers following current_num
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    # Example usage
    examples = [
        [100, 4, 200, 1, 3, 2],
        [10, 5, 12, 3, 55, 30, 4, 11, 2],
        [],
        [1],
        [9, 8, 7, 6, 5],
        [1, 2, 2, 3],
    ]

    for idx, example in enumerate(examples, 1):
        try:
            result = longest_consecutive_subsequence(example)
            print(f"Example {idx}: Input: {example} -> Longest consecutive subsequence length: {result}")
        except (TypeError, ValueError) as e:
            print(f"Example {idx}: Input: {example} -> Error: {e}")


if __name__ == "__main__":
    main()