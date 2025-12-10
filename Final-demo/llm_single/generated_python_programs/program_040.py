def longest_consecutive_subsequence(nums):
    """
    Finds the length of the longest consecutive subsequence (numbers increasing by 1)
    appearing in the same order within the list (not necessarily contiguous).

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: Length of the longest consecutive subsequence.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] will store the length of the longest consecutive subsequence ending with nums[i]
    dp = [1] * n

    # Map from number to list of indices where it appears (to optimize lookups)
    from collections import defaultdict
    positions = defaultdict(list)
    for i, num in enumerate(nums):
        positions[num].append(i)

    # For each index, try to extend subsequence by looking for nums[i] - 1
    for i in range(n):
        prev_num = nums[i] - 1
        if prev_num in positions:
            # Find the largest dp value among all indices of prev_num that come before i
            max_len = 0
            for idx in positions[prev_num]:
                if idx < i:
                    if dp[idx] > max_len:
                        max_len = dp[idx]
                else:
                    break  # positions are in ascending order, no need to check further
            dp[i] = max_len + 1

    return max(dp)


def main():
    try:
        example = [2, 6, 1, 3, 4, 5, 7]
        result = longest_consecutive_subsequence(example)
        print(f"Longest consecutive subsequence length: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()