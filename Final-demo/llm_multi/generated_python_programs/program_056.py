```python
def find_duplicates(nums):
    """
    Returns a list of elements that appear more than once in nums,
    preserving their order of first occurrence.
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


def main():
    # Example usage
    test_cases = [
        [1, 2, 3, 2, 1, 5],
        [10, 20, 30, 40],
        [4, 4, 4, 4],
        [],
        [7, 8, 9, 7, 8, 9, 10],
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"Test case {i}: {case}")
        print(f"Duplicates: {find_duplicates(case)}\n")


if __name__ == "__main__":
    main()
```