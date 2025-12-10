```python
def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main():
    user_input = input("Enter a list of integers separated by spaces: ")
    try:
        nums = list(map(int, user_input.strip().split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    length = longest_increasing_subsequence(nums)
    print(f"Length of the longest increasing subsequence: {length}")


if __name__ == "__main__":
    main()
```