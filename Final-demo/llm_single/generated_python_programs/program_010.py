def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list.
    A consecutive subsequence consists of numbers that appear in increasing order by 1,
    not necessarily contiguous in the list.
    
    :param nums: List[int] - list of integers
    :return: int - length of the longest consecutive subsequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")
    
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # If num - 1 is not in set, then num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
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
        print(f"The length of the longest consecutive subsequence is: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()