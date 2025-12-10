```python
from collections import Counter

def find_duplicates(nums):
    """
    Returns a list of elements that appear more than once in nums,
    preserving the original order of their first occurrence.
    If no elements are repeated, returns an empty list.
    """
    counts = Counter(nums)
    seen = set()
    result = []

    for num in nums:
        if counts[num] > 1 and num not in seen:
            result.append(num)
            seen.add(num)

    return result


if __name__ == "__main__":
    # Example usage and simple tests
    test_cases = [
        ([1, 2, 2, 3, 4, 4, 5], [2, 4]),
        ([1, 2, 3, 4, 5], []),
        ([5, 5, 5, 5], [5]),
        ([], []),
        ([10, 20, 10, 30, 20, 40, 50, 50], [10, 20, 50]),
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        output = find_duplicates(input_list)
        print(f"Test case {i}: input={input_list}")
        print(f"Expected: {expected}, Got: {output}")
        assert output == expected, f"Test case {i} failed"
    print("All test cases passed.")
```