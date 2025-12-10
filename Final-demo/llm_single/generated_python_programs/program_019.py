import sys

def longest_consecutive_subsequence(nums):
    """
    Finds the length of the longest consecutive subsequence from the given list of integers.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: Length of the longest consecutive subsequence.

    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

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
    # Example usages and basic tests
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),          # Sequence: 1,2,3,4
        ([0, -1, 1, 2, -2, 3], 6),            # Sequence: -2,-1,0,1,2,3
        ([10, 5, 12, 3, 55, 30, 4, 11], 4),   # Sequence: 3,4,5
        ([1, 2, 0, 1], 3),                     # Sequence: 0,1,2
        ([], 0),                              # Empty list
        ([7], 1),                            # Single element
    ]

    for idx, (input_list, expected) in enumerate(test_cases, 1):
        try:
            result = longest_consecutive_subsequence(input_list)
            assert result == expected, f"Test case {idx} failed: expected {expected}, got {result}"
            print(f"Test case {idx} passed: longest consecutive subsequence length is {result}")
        except Exception as e:
            print(f"Test case {idx} raised an exception: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()