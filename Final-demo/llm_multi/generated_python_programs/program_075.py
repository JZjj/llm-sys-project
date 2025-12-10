```python
def find_duplicates(lst):
    """
    Returns a list of elements that appear more than once in the original list,
    preserving their original order of first occurrence.
    """
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1

    result = []
    seen = set()
    for num in lst:
        if counts[num] > 1 and num not in seen:
            result.append(num)
            seen.add(num)
    return result


def main():
    example = [4, 5, 6, 5, 4, 7, 8, 4]
    print("Input:", example)
    print("Duplicates:", find_duplicates(example))

    print("Duplicates in [1,2,3,4]:", find_duplicates([1, 2, 3, 4]))  # []
    print("Duplicates in [1,1,1,2,2,3]:", find_duplicates([1, 1, 1, 2, 2, 3]))  # [1, 2]
    print("Duplicates in []:", find_duplicates([]))  # []
    print("Duplicates in [10, 10, 10, 10]:", find_duplicates([10, 10, 10, 10]))  # [10]


if __name__ == "__main__":
    main()
```