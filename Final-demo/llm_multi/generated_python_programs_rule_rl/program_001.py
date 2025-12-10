def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list nums.
    A consecutive subsequence consists of numbers that differ by exactly 1,
    appearing in sorted order (not necessarily contiguous in the original list).

    Args:
        nums (list of int): The input list of integers.

    Returns:
        int: The length of the longest consecutive subsequence.
    """
    if not nums:
        return 0

    num_set = set(nums)  # O(n) time to build set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count upwards while consecutive numbers exist
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            if current_streak > longest_streak:
                longest_streak = current_streak

    return longest_streak


if __name__ == "__main__":
    # Example usage and simple test cases
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([1, 2, 0, 1], 3),
        ([], 0),
        ([10], 1),
        ([5, 6, 7, 8, 9, 10], 6),
        ([1, 3, 5, 7], 1),
        ([9, 1, 4, 7, 3, 2, 6, 8, 5], 9),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = longest_consecutive_subsequence(nums)
        print(f"Test case {i}: Input: {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 40)