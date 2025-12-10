```python
def longest_consecutive_subsequence(nums):
    if not nums:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current_length += 1
        else:
            current_length = 1
        if current_length > max_length:
            max_length = current_length

    return max_length


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ([1, 2, 2, 3, 4, 1, 2, 3], 3),
        ([], 0),
        ([5, 6, 7, 8, 9], 5),
        ([1, 3, 5, 7], 1),
        ([10, 11, 12, 2, 3, 4, 5, 6], 5),
        ([1], 1),
        ([1, 2, 3, 2, 3, 4, 5, 1, 2], 4),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = longest_consecutive_subsequence(nums)
        print(f"Test case {i}: input = {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 40)
```