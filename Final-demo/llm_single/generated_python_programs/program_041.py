def longest_increasing_subsequence_length(nums):
    """
    Returns the length of the longest consecutive subsequence of strictly increasing numbers in the list.
    
    :param nums: List[int] - a list of integers
    :return: int - the length of the longest consecutive increasing subsequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")
    
    max_len = 0
    current_len = 0
    previous = None
    
    for num in nums:
        if previous is None or num > previous:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
        previous = num
    
    max_len = max(max_len, current_len)
    return max_len


def main():
    # Example usage
    test_cases = [
        ([1, 2, 2, 3, 4, 1], 3),
        ([5, 6, 7, 8, 1, 2], 4),
        ([1, 1, 1, 1], 1),
        ([10, 9, 8, 7], 1),
        ([1, 2, 3, 4, 5], 5),
        ([], 0),
    ]
    
    for i, (input_list, expected) in enumerate(test_cases, start=1):
        try:
            result = longest_increasing_subsequence_length(input_list)
            assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
            print(f"Test case {i} passed: input={input_list}, output={result}")
        except Exception as e:
            print(f"Test case {i} raised an exception: {e}")


if __name__ == "__main__":
    main()