```python
def longest_consecutive(nums):
    """
    Returns the length of the longest consecutive elements sequence.
    The sequence must consist of consecutive integers increasing by 1,
    but the input list can be in any order.
    Time complexity: O(n)
    """
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    example = [100, 4, 200, 1, 3, 2]
    print(f"Input list: {example}")
    result = longest_consecutive(example)
    print(f"Length of the longest consecutive elements sequence: {result}")


if __name__ == "__main__":
    main()
```