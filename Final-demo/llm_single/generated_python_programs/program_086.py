def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the input list.
    
    Args:
        nums (list of int): List of integers to analyze.
        
    Returns:
        int: Length of the longest consecutive subsequence.
        
    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")
    
    num_set = set(nums)  # Using a set for O(1) lookups
    max_length = 0
    
    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length


def main():
    # Example usage and simple test cases
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([1, 2, 2, 3], 3),
        ([10], 1),
        ([], 0),
        ([5, 6, 7, 8, 1, 2, 3], 4),
        ([9, 1, 4, 7, 3, 2, 6, 8], 6)
    ]
    
    for i, (input_list, expected) in enumerate(test_cases, 1):
        try:
            result = longest_consecutive_subsequence(input_list)
            assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
            print(f"Test case {i} passed: got {result}")
        except AssertionError as ae:
            print(ae)
        except Exception as e:
            print(f"Test case {i} raised an unexpected exception: {e}")


if __name__ == "__main__":
    main()