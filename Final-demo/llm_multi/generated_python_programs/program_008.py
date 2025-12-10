```python
def longest_increasing_subsequence_length(nums):
    if not nums:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 1

    return max_len


if __name__ == "__main__":
    # Example usage
    test_list = [1, 2, 2, 3, 4, 1, 2, 3]
    print(f"Input list: {test_list}")
    result = longest_increasing_subsequence_length(test_list)
    print(f"Length of longest increasing contiguous subsequence: {result}")
```