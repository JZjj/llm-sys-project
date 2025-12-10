def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list of integers.
    
    Args:
        nums (list of int): List of integers.
        
    Returns:
        int: Length of the longest consecutive subsequence.
        
    Raises:
        TypeError: If nums is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")
    
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
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
    try:
        example = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_subsequence(example)
        print(f"Longest consecutive subsequence length: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()