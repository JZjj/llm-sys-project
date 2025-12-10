import sys

def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list of integers.
    A consecutive subsequence consists of numbers that appear consecutively in increasing order,
    but not necessarily contiguous in the list.

    Args:
        nums (list of int): The input list of integers.

    Returns:
        int: Length of the longest consecutive subsequence.

    Raises:
        TypeError: If nums is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if any(not isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

    num_set = set(nums)  # For O(1) lookups
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
    example_lists = [
        [100, 4, 200, 1, 3, 2],
        [],
        [10, 9, 8, 7],
        [1, 2, 0, 1],
        [5, 6, 7, 8, 1, 2, 3],
    ]

    for i, lst in enumerate(example_lists, 1):
        try:
            result = longest_consecutive_subsequence(lst)
            print(f"Example {i}: Input: {lst} -> Longest consecutive subsequence length: {result}")
        except Exception as e:
            print(f"Example {i}: Input: {lst} -> Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()