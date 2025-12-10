```python
def longest_consecutive(nums):
    """
    Finds the length of the longest consecutive elements sequence in the list.
    The sequence must consist of consecutive integers in increasing order without gaps.

    Args:
        nums (List[int]): List of integers, unsorted.

    Returns:
        int: Length of the longest consecutive elements sequence.
    """
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    # Example test cases
    test_cases = [
        [100, 4, 200, 1, 3, 2],
        [0, -1, 1, 2, -2, 3, 4],
        [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
        [],
        [10],
        [1, 2, 2, 3],
        [5, 6, 7, 8, 1, 2, 3, 4],
    ]

    for i, nums in enumerate(test_cases, 1):
        result = longest_consecutive(nums)
        print(f"Test case {i}: Input: {nums}")
        print(f"Longest consecutive sequence length: {result}\n")


if __name__ == "__main__":
    main()
```