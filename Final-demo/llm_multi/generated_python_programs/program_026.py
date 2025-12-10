```python
from collections import defaultdict

def longest_subarray(arr):
    """
    Returns the length of the longest contiguous subarray where the absolute difference
    between any two elements is at most 1.
    """
    if not arr:
        return 0

    count = defaultdict(int)
    left = 0
    max_length = 1
    min_val = arr[0]
    max_val = arr[0]

    for right, val in enumerate(arr):
        count[val] += 1
        min_val = min(min_val, val)
        max_val = max(max_val, val)

        while max_val - min_val > 1:
            left_val = arr[left]
            count[left_val] -= 1
            if count[left_val] == 0:
                del count[left_val]
            left += 1
            if count:
                min_val = min(count.keys())
                max_val = max(count.keys())

        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    # Example test
    arr = [2, 2, 3, 4, 3, 3, 2]
    print("Input:", arr)
    print("Length of longest subarray:", longest_subarray(arr))

    # Additional tests
    tests = [
        ([1, 2, 2, 3, 4, 2, 1], 4),
        ([1, 1, 1, 1, 1], 5),
        ([1, 3, 5, 7], 1),
        ([4, 5, 5, 6, 7, 8, 8, 7, 7], 5),
        ([], 0),
        ([1], 1),
    ]

    for i, (test_arr, expected) in enumerate(tests, 1):
        result = longest_subarray(test_arr)
        print(f"Test {i}: input={test_arr} expected={expected} got={result} {'PASS' if result == expected else 'FAIL'}")
```