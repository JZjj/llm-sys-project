```python
def longest_plus_minus_one_subsequence(arr):
    """
    Returns the length of the longest subsequence where the difference between
    consecutive elements is either +1 or -1.
    The subsequence elements appear in the original order but do not need to be contiguous.
    """
    if not arr:
        return 0

    # dp[i] will hold the length of the longest valid subsequence ending at index i
    n = len(arr)
    dp = [1] * n

    # Map from value to the max dp for that value encountered so far
    value_to_dp = {}

    max_len = 1
    for i, val in enumerate(arr):
        prev_len_1 = value_to_dp.get(val - 1, 0)
        prev_len_2 = value_to_dp.get(val + 1, 0)

        dp[i] = 1 + max(prev_len_1, prev_len_2, 0)

        # Update the value_to_dp for this val with the best dp found
        if val not in value_to_dp or dp[i] > value_to_dp[val]:
            value_to_dp[val] = dp[i]

        if dp[i] > max_len:
            max_len = dp[i]

    return max_len


def main():
    # Example test case
    example = [1, 2, 3, 2, 3, 4, 3]
    print("Example input:", example)
    print("Longest subsequence length:", longest_plus_minus_one_subsequence(example))

    # Additional test cases
    test_cases = [
        ([], 0),
        ([5], 1),
        ([1, 3, 5, 7], 1),
        ([1, 2, 1, 2, 1, 2], 6),
        ([10, 9, 8, 9, 10, 11, 12], 7),
        ([1, 1, 2, 3, 2, 2, 3, 4, 3], 8),
        ([10000 - i for i in range(10000)], 10000),
        ([1] * 5000 + [2] * 5000, 10000),
    ]

    for i, (input_arr, expected) in enumerate(test_cases, 1):
        result = longest_plus_minus_one_subsequence(input_arr)
        print(f"Test case {i}: Expected {expected}, Got {result}, {'PASS' if result == expected else 'FAIL'}")


if __name__ == "__main__":
    main()
```