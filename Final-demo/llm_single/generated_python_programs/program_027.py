import sys
from typing import List

def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence in the list.
    
    Args:
        nums (List[int]): List of integers.
        
    Returns:
        int: Length of the longest consecutive subsequence.
    
    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")
    
    num_set = set(nums)  # For O(1) look-ups
    longest_streak = 0
    
    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak


def main():
    try:
        example_list = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_subsequence(example_list)
        print(f"The length of the longest consecutive subsequence is: {result}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()