```python
from collections import Counter

def find_duplicates(lst):
    """
    Returns a list of elements that appear more than once in lst,
    preserving their original order of first occurrence.
    If no elements are repeated, returns an empty list.
    """
    counts = Counter(lst)
    seen = set()
    result = []

    for x in lst:
        if counts[x] > 1 and x not in seen:
            result.append(x)
            seen.add(x)

    return result


if __name__ == "__main__":
    # Example usage and simple tests
    test_cases = [
        ([1, 2, 3, 4, 5], []),
        ([1, 2, 2, 3, 4, 3, 5], [2, 3]),
        ([5, 5, 5, 5], [5]),
        ([10, 20, 10, 30, 20, 40], [10, 20]),
        ([], []),
        ([1, 1, 2, 2, 3, 3, 4, 4], [1, 2, 3, 4]),
        ([7], []),
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        output = find_duplicates(input_list)
        print(f"Test case {i}: input={input_list}")
        print(f"Expected output: {expected}")
        print(f"Actual output:   {output}")
        print(f"Test {'PASSED' if output == expected else 'FAILED'}\n")
```