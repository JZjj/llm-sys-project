def longest_consecutive_subsequence_length(nums):
    """
    Returns the length of the longest consecutive subsequence 
    (numbers increasing by 1) in the list nums.
    The subsequence does not need to be contiguous but order must be maintained.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] will store the length of the longest consecutive subsequence
    # ending with nums[i]
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            # Check if nums[i] continues the consecutive sequence after nums[j]
            if nums[i] == nums[j] + 1:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    return max(dp)


def main():
    try:
        example = [3, 10, 2, 1, 20]
        length = longest_consecutive_subsequence_length(example)
        print(f"Longest consecutive subsequence length for {example} is {length}")

        # Additional tests
        test_cases = [
            ([1, 2, 3, 4, 5], 5),
            ([10, 9, 8, 7], 1),
            ([5, 6, 3, 4, 7, 8], 4),
            ([100, 4, 200, 1, 3, 2], 4),
            ([], 0),
            ([1], 1),
            ([1, 3, 5, 6, 7, 8, 9], 5)
        ]
        for arr, expected in test_cases:
            result = longest_consecutive_subsequence_length(arr)
            assert result == expected, f"Test failed for input {arr}: expected {expected}, got {result}"
        print("All tests passed successfully.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()