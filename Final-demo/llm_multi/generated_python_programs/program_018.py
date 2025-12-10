```python
def find_duplicates(nums):
    """
    Returns a list of elements that appear more than once in nums,
    preserving their original order of first occurrence.
    If no duplicates exist, returns an empty list.
    """
    seen = set()
    duplicates = set()
    result = []

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    for num in nums:
        if num in duplicates and num not in result:
            result.append(num)

    return result


if __name__ == "__main__":
    # Example usage and simple tests
    test_cases = [
        ([1, 2, 3, 2, 1, 5], [1, 2]),
        ([10, 20, 30, 40], []),
        ([5, 5, 5, 5], [5]),
        ([], []),
        ([1, 2, 3, 4, 4, 3, 2, 1], [1, 2, 3, 4]),
        ([7, 8, 7, 9, 8, 10], [7, 8]),
        ([1], []),
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        output = find_duplicates(input_list)
        print(f"Test case {i}: input: {input_list}")
        print(f"Expected: {expected}")
        print(f"Output:   {output}")
        print(f"Pass:     {output == expected}\n")
```