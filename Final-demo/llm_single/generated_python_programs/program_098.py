def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence where numbers follow each other
    in increasing order by 1. The subsequence does not need to be contiguous in the list,
    but the numbers must appear in order.

    :param nums: List[int] - list of integers
    :return: int - length of the longest consecutive subsequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the input list must be integers")

    # Dictionary to keep track of the length of the longest consecutive subsequence ending with key
    dp = {}
    max_length = 0

    for num in nums:
        # If previous number (num - 1) is in dp, extend the subsequence length by 1
        if num - 1 in dp:
            dp[num] = dp[num - 1] + 1
        else:
            dp[num] = 1
        max_length = max(max_length, dp[num])

    return max_length


def main():
    try:
        example_input = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_subsequence(example_input)
        print(f"Input: {example_input}")
        print(f"Output: {result}  (because the longest consecutive subsequence is [1, 2, 3, 4])")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()