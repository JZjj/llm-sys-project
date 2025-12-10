def longest_consecutive_sequence(nums):
    """
    Finds the length of the longest consecutive elements sequence in the list.
    
    Args:
        nums (list of int): List of integers.
        
    Returns:
        int: Length of the longest consecutive sequence.
        
    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if any(not isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")
    
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Only start counting if 'num' is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Count upwards from current_num
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak


def main():
    try:
        example_list = [100, 4, 200, 1, 3, 2]
        result = longest_consecutive_sequence(example_list)
        print(f"Longest consecutive sequence length: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()