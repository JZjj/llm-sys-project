```python
def longest_consecutive(nums):
    if not nums:
        return 0

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
    example_list = [100, 4, 200, 1, 3, 2]
    print("Input list:", example_list)
    print("Length of longest consecutive sequence:", longest_consecutive(example_list))


if __name__ == "__main__":
    main()
```