```python
from collections import Counter

def find_duplicates(nums):
    """
    Returns a sorted list of elements that appear more than once in the input list,
    with no duplicates in the result.
    """
    counts = Counter(nums)
    duplicates = [num for num, count in counts.items() if count > 1]
    return sorted(duplicates)

def main():
    # Example usage:
    example_list = [4, 5, 6, 4, 7, 5, 8, 9, 6, 6]
    result = find_duplicates(example_list)
    print(f"Input list: {example_list}")
    print(f"Elements appearing more than once (sorted): {result}")

if __name__ == "__main__":
    main()
```