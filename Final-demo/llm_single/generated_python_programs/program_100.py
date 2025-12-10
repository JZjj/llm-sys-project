import sys

def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list nums.
    The subsequence does not need to be contiguous, but the numbers must be consecutive integers.
    
    :param nums: List[int] - a list of integers
    :return: int - length of the longest consecutive subsequence
    :raises TypeError: if input is not a list or contains non-integers
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")
    
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if `num` is the start of a sequence
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
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()