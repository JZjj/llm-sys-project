def longest_consecutive_subsequence(nums):
    """
    Returns the length of the longest consecutive subsequence in the list of integers.
    A consecutive subsequence consists of numbers that appear consecutively numerically,
    but not necessarily adjacent in the list.

    :param nums: List[int] - list of integers
    :return: int - length of the longest consecutive subsequence
    :raises TypeError: if input is not a list or contains non-integers
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the list must be integers")

    num_set = set(nums)
    longest_length = 0

    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive numbers after current_num
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest_length = max(longest_length, current_length)

    return longest_length


def main():
    # Example usage
    example_list = [100, 4, 200, 1, 3, 2]
    try:
        length = longest_consecutive_subsequence(example_list)
        print(f"The length of the longest consecutive subsequence is: {length}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()