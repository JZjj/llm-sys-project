import sys

def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list.
    
    Args:
        nums (list of int): List of integers to evaluate.
        
    Returns:
        int: Length of the longest consecutive subsequence.
        
    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")
    
    num_set = set(nums)  # Using a set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only start counting if num-1 is not in set, meaning start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            if current_streak > longest_streak:
                longest_streak = current_streak

    return longest_streak


def main():
    # Example usage with error handling
    example_lists = [
        [100, 4, 200, 1, 3, 2],
        [10, 5, 6, 7, 20, 21, 22],
        [],
        [1],
        [9, 8, 7, 6, 5],
        ["a", 1, 2],  # Invalid input example
    ]

    for i, lst in enumerate(example_lists, start=1):
        try:
            result = longest_consecutive_subsequence(lst)
            print(f"Example {i}: Input: {lst} -> Longest consecutive subsequence length: {result}")
        except Exception as e:
            print(f"Example {i}: Input: {lst} -> Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()