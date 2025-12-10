```python
def longest_consecutive_diff_one_subsequence(arr):
    """
    Finds the length of the longest subsequence where the difference between
    consecutive elements is exactly 1. The subsequence elements do not need
    to be contiguous in the original list but must appear in the same order.
    """
    if not arr:
        return 0

    n = len(arr)
    # dp[i] will store the length of the longest valid subsequence ending at index i
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    # Example test case
    example_list = [3, 4, 2, 3, 4, 5, 6]
    result = longest_consecutive_diff_one_subsequence(example_list)
    print(f"Input list: {example_list}")
    print(f"Length of longest subsequence with consecutive difference 1: {result}")

    # Additional test cases
    tests = [
        ([1, 2, 3, 4, 5], 5),
        ([10, 9, 8, 7, 6], 5),
        ([1, 3, 5, 7], 1),
        ([1, 2, 2, 3, 4], 4),  # subsequence like [1,2,3,4]
        ([], 0),
        ([5], 1),
        ([1, 2, 3, 2, 1, 0], 4),  # subsequence like [1,2,3,2] or [2,3,2,1]
    ]

    for i, (test_input, expected) in enumerate(tests, 1):
        res = longest_consecutive_diff_one_subsequence(test_input)
        print(f"Test case {i}: input={test_input} -> output={res} (expected {expected})")
```