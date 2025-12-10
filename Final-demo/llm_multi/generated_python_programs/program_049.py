```python
def longest_subsequence_with_diff_one(arr):
    """
    Returns the length of the longest subsequence where the absolute difference 
    between any two consecutive elements is exactly 1.
    The subsequence elements appear in the same order but are not necessarily contiguous.
    """
    if not arr:
        return 0

    value_to_length = {}
    max_length = 1

    for val in arr:
        best_prev = max(value_to_length.get(val - 1, 0), value_to_length.get(val + 1, 0))
        current_length = best_prev + 1
        if value_to_length.get(val, 0) < current_length:
            value_to_length[val] = current_length
        if current_length > max_length:
            max_length = current_length

    return max_length


def main():
    import sys

    print("Enter the list of integers separated by spaces:")
    line = sys.stdin.readline()
    arr = list(map(int, line.strip().split()))

    result = longest_subsequence_with_diff_one(arr)
    print(result)


if __name__ == "__main__":
    main()
```