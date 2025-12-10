import sys

def longest_consecutive_subsequence(nums):
    """
    Finds the length of the longest consecutive subsequence in an unsorted list of integers.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: Length of the longest consecutive subsequence.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if any(not isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

    num_set = set(nums)  # For O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only start counting if 'num' is the start of a sequence
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
    example_lists = [
        [100, 4, 200, 1, 3, 2],
        [],
        [1],
        [9, 8, 7, 6, 5],
        [10, 5, 12, 3, 55, 30, 4, 11, 2],
    ]

    for idx, lst in enumerate(example_lists, 1):
        try:
            result = longest_consecutive_subsequence(lst)
            print(f"Example {idx}: Input: {lst} -> Longest consecutive subsequence length: {result}")
        except Exception as e:
            print(f"Example {idx}: Error processing input {lst}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()