```python
def longest_zero_sum_subarray(arr):
    """
    Finds the longest contiguous subarray whose elements sum to zero.

    Parameters:
        arr (list of int): The input list of integers.

    Returns:
        tuple: (start_index, end_index) of the longest zero-sum subarray.
               If multiple such subarrays exist, returns the first one.
               Returns None if no such subarray exists.
    """
    prefix_sum_indices = {0: -1}  # Maps prefix_sum to earliest index
    prefix_sum = 0
    max_length = 0
    start_index = None
    end_index = None

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum in prefix_sum_indices:
            prev_index = prefix_sum_indices[prefix_sum]
            current_length = i - prev_index
            if current_length > max_length:
                max_length = current_length
                start_index = prev_index + 1
                end_index = i
        else:
            prefix_sum_indices[prefix_sum] = i

    if max_length == 0:
        return None
    return (start_index, end_index)


def main():
    # Example usage and testing
    test_cases = [
        ([1, 2, -3, 3, -1, -2, 4, -4], (0, 2)),
        ([1, 2, 3, 4, 5], None),
        ([0, 0, 0, 0], (0, 3)),
        ([3, 4, -7, 1, 3, 3, 1, -4], (0, 2)),
        ([1, -1, 2, -2, 3, -3, 4], (0, 5)),
        ([], None),
        ([1, -1], (0, 1)),
        ([6, -1, -3, 4, -2, 2, 4, 6, -12, -7], (1, 8)),
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = longest_zero_sum_subarray(arr)
        print(f"Test case {i}: Input: {arr}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 40)


if __name__ == "__main__":
    main()
```