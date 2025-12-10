```python
def find_duplicates(nums):
    """
    Returns a list of elements that appear more than once in nums,
    preserving their first occurrence order.
    """
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    result = []
    seen = set()
    for num in nums:
        if counts[num] > 1 and num not in seen:
            result.append(num)
            seen.add(num)

    return result


if __name__ == "__main__":
    # Example usage
    test_input = [4, 5, 6, 5, 4, 3]
    print(f"Input: {test_input}")
    print(f"Output: {find_duplicates(test_input)}")
```