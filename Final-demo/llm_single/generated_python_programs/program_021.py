from typing import List

def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence in increasing order by 1.
    The subsequence does not need to be contiguous but must appear in the original order.

    Args:
        nums (List[int]): The list of integers.

    Returns:
        int: The length of the longest consecutive subsequence.

    Raises:
        TypeError: If the input is not a list or contains non-integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if any(not isinstance(x, int) for x in nums):
        raise TypeError("All elements must be integers.")

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] will store the length of the longest consecutive subsequence ending with nums[i]
    dp = [1] * n
    max_length = 1

    # For each element, look backwards for nums[j] such that nums[j] + 1 == nums[i]
    for i in range(1, n):
        for j in range(i):
            if nums[j] + 1 == nums[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    if dp[i] > max_length:
                        max_length = dp[i]

    return max_length


def main():
    # Example usage
    examples = [
        [4, 2, 1, 6, 5],
        [1, 2, 3, 4, 5],
        [10, 9, 8, 7],
        [1, 3, 5, 7],
        [],
        [100],
        [1, 2, 2, 3, 4],
    ]

    for example in examples:
        try:
            length = longest_consecutive_subsequence(example)
            print(f"Input: {example}\nLongest consecutive subsequence length: {length}\n")
        except Exception as e:
            print(f"Input: {example}\nError: {e}\n")


if __name__ == "__main__":
    main()