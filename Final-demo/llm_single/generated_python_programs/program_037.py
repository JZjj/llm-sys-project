import sys

def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list of integers.
    A consecutive subsequence consists of numbers that appear consecutively in value,
    but not necessarily adjacent in the list.

    :param nums: List[int] - list of integers
    :return: int - length of the longest consecutive subsequence
    :raises TypeError: if input is not a list of integers
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only try to build sequences from numbers that are the start of a sequence
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
    try:
        example_input = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_subsequence(example_input)
        print(f"Longest consecutive subsequence length: {result}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()