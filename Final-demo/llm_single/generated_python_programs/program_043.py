def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list.
    The subsequence numbers must appear in increasing order by 1 but do not need to be contiguous.
    
    :param nums: List[int] - List of integers to process
    :return: int - Length of the longest consecutive subsequence
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")
    
    # Dictionary to store the length of longest subsequence ending with key
    subseq_lengths = {}
    max_length = 0

    for num in nums:
        # Length of subsequence ending with num is length of subsequence ending with num-1 plus one
        prev_length = subseq_lengths.get(num - 1, 0)
        curr_length = prev_length + 1
        # Update the length for current number if it's greater than existing
        if curr_length > subseq_lengths.get(num, 0):
            subseq_lengths[num] = curr_length
            max_length = max(max_length, curr_length)

    return max_length


def main():
    # Example usage and demonstration
    example_lists = [
        [4, 2, 1, 6, 5],
        [10, 9, 4, 5, 6, 7],
        [],
        [1, 3, 5, 7],
        [1, 2, 3, 4, 5],
        [2, 2, 3, 4, 3, 4, 5]
    ]

    for i, lst in enumerate(example_lists, 1):
        try:
            length = longest_consecutive_subsequence(lst)
            print(f"Example {i}: List = {lst}")
            print(f"Longest consecutive subsequence length: {length}\n")
        except (TypeError, ValueError) as e:
            print(f"Example {i}: List = {lst} -> Error: {e}\n")


if __name__ == "__main__":
    main()