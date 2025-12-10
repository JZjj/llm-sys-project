```python
from collections import Counter

def find_duplicates(nums):
    """
    Returns a sorted list of elements that appear more than once in the input list.

    Args:
        nums (list of int): The list of integers to check.

    Returns:
        list of int: Sorted list of integers appearing more than once, without duplicates.
    """
    counts = Counter(nums)
    duplicates = [num for num, count in counts.items() if count > 1]
    return sorted(duplicates)


def main():
    # Example usage
    test_input = [4, 5, 6, 5, 4, 3]
    result = find_duplicates(test_input)
    print("Input:", test_input)
    print("Duplicates appearing more than once:", result)


if __name__ == "__main__":
    main()
```