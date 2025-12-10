def longest_zero_sum_sublist(nums):
    """
    Find the longest contiguous sublist with sum zero.
    
    Args:
        nums (list of int): List of integers.
        
    Returns:
        list of int: The longest zero-sum contiguous sublist.
                     Returns empty list if none found.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements of the input list must be integers.")
    
    prefix_sum_index = {0: -1}  # Maps prefix_sum to earliest index
    prefix_sum = 0
    max_len = 0
    start_index = -1
    
    for i, num in enumerate(nums):
        prefix_sum += num
        
        if prefix_sum in prefix_sum_index:
            prev_index = prefix_sum_index[prefix_sum]
            length = i - prev_index
            if length > max_len:
                max_len = length
                start_index = prev_index + 1
        else:
            prefix_sum_index[prefix_sum] = i
    
    if max_len == 0:
        return []
    return nums[start_index:start_index + max_len]


def main():
    # Example usages
    examples = [
        [1, 2, -3, 3, -1, -2, 2, -2],
        [1, 2, 3, 4, 5],
        [0, 0, 0, 0],
        [-1, 1],
        [],
        [3, 4, -7, 1, 3, 3, 1, -4, -2, -2]
    ]
    
    for i, example in enumerate(examples, 1):
        try:
            result = longest_zero_sum_sublist(example)
            print(f"Example {i}: Input: {example}")
            print(f"Longest zero-sum sublist: {result}\n")
        except (TypeError, ValueError) as e:
            print(f"Example {i}: Input: {example} -> Error: {e}\n")


if __name__ == "__main__":
    main()