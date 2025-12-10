from typing import List

def longest_consecutive_subsequence(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive subsequence of integers in the list.
    
    A consecutive subsequence is a set of numbers that form a sequence of consecutive integers,
    regardless of their order or position in the original list.
    
    Args:
        nums (List[int]): The list of integers to analyze.
    
    Returns:
        int: The length of the longest consecutive subsequence.
        
    Raises:
        TypeError: If nums is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")
    
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

def main():
    # Example usage
    example_list = [100, 4, 200, 1, 3, 2]
    try:
        result = longest_consecutive_subsequence(example_list)
        print(f"Longest consecutive subsequence length: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()