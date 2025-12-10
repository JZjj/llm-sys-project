def longest_strictly_increasing_sublist(nums):
    """
    Finds the longest contiguous sublist where elements are strictly increasing.
    If multiple such sublists have the same maximum length, returns the first one.

    :param nums: List[int] - list of integers
    :return: List[int] - longest strictly increasing contiguous sublist
    :raises TypeError: if input is not a list or contains non-integers
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if any(not isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers.")

    max_start = 0
    max_length = 1 if nums else 0
    current_start = 0
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
        else:
            # Check if current sequence is longest so far
            if current_length > max_length:
                max_length = current_length
                max_start = current_start
            # Reset for new sequence
            current_start = i
            current_length = 1

    # Final check after loop ends
    if current_length > max_length:
        max_length = current_length
        max_start = current_start

    return nums[max_start:max_start + max_length]


def main():
    # Example usage
    example_lists = [
        [1, 2, 2, 3, 4, 5, 1, 2],
        [5, 4, 3, 2, 1],
        [],
        [10, 20, 30, 5, 6, 7, 8, 1, 2],
        [1, 3, 5, 4, 6, 8, 10]
    ]

    for idx, lst in enumerate(example_lists, 1):
        try:
            result = longest_strictly_increasing_sublist(lst)
            print(f"Example {idx}: Input: {lst}\nLongest strictly increasing sublist: {result}\n")
        except Exception as e:
            print(f"Example {idx}: Error processing list {lst} -> {e}\n")


if __name__ == "__main__":
    main()