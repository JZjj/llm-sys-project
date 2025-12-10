def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the given list of integers.
    
    Args:
        nums (list of int): The input list of integers.
        
    Returns:
        int: Length of the longest consecutive subsequence.
        
    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")
    
    num_set = set(nums)  # Use a set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only start counting if num-1 is not in set (to ensure start of sequence)
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
        example_input = [100, 4, 200, 1, 3, 2]
        print(f"Input: {example_input}")
        result = longest_consecutive_subsequence(example_input)
        print(f"Length of the longest consecutive subsequence: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()