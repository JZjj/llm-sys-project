```python
from collections import defaultdict

def longest_subarray(nums):
    """
    Returns the length of the longest contiguous subarray where the absolute difference
    between any two elements is at most 1.
    """
    if not nums:
        return 0

    left = 0
    counts = defaultdict(int)
    max_len = 1

    for right, num in enumerate(nums):
        counts[num] += 1

        while max(counts.keys()) - min(counts.keys()) > 1:
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    test_list = [1, 2, 2, 3, 1, 2]
    print(longest_subarray(test_list))  # Expected output: 6
```