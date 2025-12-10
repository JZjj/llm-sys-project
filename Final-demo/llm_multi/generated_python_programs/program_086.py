```python
from collections import Counter

def find_duplicates(nums):
    """
    Returns a list of elements that appear more than once in the input list,
    preserving their original order of first occurrence.
    If no duplicates are found, returns an empty list.
    """
    counts = Counter(nums)
    seen = set()
    duplicates = []
    for num in nums:
        if counts[num] > 1 and num not in seen:
            duplicates.append(num)
            seen.add(num)
    return duplicates


if __name__ == "__main__":
    # Example usage and simple tests
    test_cases = [
        ([1, 2, 3, 2, 4, 5, 1], [1, 2]),
        ([1, 2, 3, 4, 5], []),
        ([5, 5, 5, 5], [5]),
        ([], []),
        ([10, 20, 10, 30, 20, 20], [10, 20]),
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        result = find_duplicates(input_list)
        print(f"Test case {i}: input={input_list}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print(f"Pass:     {result == expected}\n")
```