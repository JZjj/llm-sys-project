from typing import List

def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence (numbers increasing by 1)
    within the list, maintaining the original order but not necessarily contiguous.

    Args:
        nums (List[int]): List of integers to process.

    Returns:
        int: Length of the longest consecutive subsequence.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if any(not isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")

    # Dictionary to store the length of longest consecutive subsequence ending with the key number
    dp = {}
    max_length = 0

    for num in nums:
        # The length of consecutive subsequence ending with num is 1 + length ending with num-1 (if any)
        prev_length = dp.get(num - 1, 0)
        dp[num] = prev_length + 1
        if dp[num] > max_length:
            max_length = dp[num]

    return max_length


def main():
    try:
        # Example usage
        examples = [
            [4, 2, 1, 6, 5],            # Expected: 3 ([4,5,6])
            [1, 9, 3, 10, 4, 20, 2],   # Expected: 4 ([1,2,3,4])
            [],                         # Expected: 0 (empty list)
            [7, 7, 7, 7],               # Expected: 1 (all same)
            [10, 9, 8, 7],              # Expected: 1 (decreasing order)
            [1, 2, 3, 4, 5],            # Expected: 5 (all consecutive)
        ]

        for i, example in enumerate(examples, 1):
            result = longest_consecutive_subsequence(example)
            print(f"Example {i}: Input: {example} -> Longest consecutive subsequence length: {result}")

    except (TypeError, ValueError) as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()