def longest_consecutive_subsequence(nums):
    """
    Find the length of the longest consecutive subsequence in an unsorted list of integers.
    
    Args:
        nums (list[int]): List of integers.
        
    Returns:
        int: Length of the longest consecutive subsequence.
        
    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if any(not isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")
    
    num_set = set(nums)  # O(n) time to create
    longest_streak = 0
    
    for num in num_set:
        # Only start counting if 'num - 1' is not in the set (start of a sequence)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Increment sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak


def main():
    # Example usage
    examples = [
        [100, 4, 200, 1, 3, 2],
        [0, -1, 1, 2, 3, 5, 6],
        [],
        [10],
        [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
    ]
    
    for idx, example in enumerate(examples, 1):
        try:
            result = longest_consecutive_subsequence(example)
            print(f"Example {idx}: input={example}\nLongest consecutive subsequence length: {result}\n")
        except Exception as e:
            print(f"Example {idx}: input={example}\nError: {e}\n")

            
if __name__ == "__main__":
    main()