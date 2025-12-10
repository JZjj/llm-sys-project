```python
def longest_subsequence_diff_one(nums):
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] holds the length of the longest subsequence ending at index i
    # with consecutive elements differing by exactly 1
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if abs(nums[i] - nums[j]) == 1 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    return max(dp)


def main():
    input_str = input("Enter a list of integers separated by spaces: ")
    try:
        nums = list(map(int, input_str.strip().split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    print(longest_subsequence_diff_one(nums))


if __name__ == "__main__":
    main()
```