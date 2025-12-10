```python
def longest_sublist_with_diff_one(nums):
    if not nums:
        return []

    max_start = 0
    max_len = 1
    current_start = 0
    current_len = 1

    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) == 1:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start = current_start
            current_start = i
            current_len = 1

    if current_len > max_len:
        max_len = current_len
        max_start = current_start

    return nums[max_start:max_start + max_len]


def main():
    print("Enter a list of integers separated by spaces:")
    try:
        nums = list(map(int, input().strip().split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    result = longest_sublist_with_diff_one(nums)
    print("Longest contiguous sublist where the absolute difference between consecutive elements is 1:")
    print(result)


if __name__ == "__main__":
    main()
```