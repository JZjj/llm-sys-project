```python
def find_duplicates(nums):
    """
    Returns a list of elements that appear more than once in nums,
    preserving their original order of first occurrence.
    If no duplicates exist, returns an empty list.
    """
    counts = {}
    duplicates = []
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    seen = set()
    for num in nums:
        if counts[num] > 1 and num not in seen:
            duplicates.append(num)
            seen.add(num)

    return duplicates


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        [1, 2, 3, 2, 1, 5, 6, 3],
        [1, 2, 3, 4, 5],
        [],
        [10, 10, 10, 10],
        [5, 1, 5, 2, 2, 3, 3, 3],
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = find_duplicates(test_case)
        print(f"Test case {i}: {test_case}")
        print(f"Duplicates: {result}\n")
```