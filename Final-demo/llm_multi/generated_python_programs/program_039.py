```python
from collections import defaultdict

def longest_subarray_with_max_min_diff_at_most_one(nums):
    """
    Returns the length of the longest contiguous subarray where the difference
    between the maximum and minimum elements is at most 1.
    """
    if not nums:
        return 0

    left = 0
    freq = defaultdict(int)
    max_len = 0

    for right, num in enumerate(nums):
        freq[num] += 1

        while True:
            current_max = max(freq.keys())
            current_min = min(freq.keys())
            if current_max - current_min <= 1:
                break
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    test_list = [1, 2, 2, 3, 4, 2, 2, 1]
    result = longest_subarray_with_max_min_diff_at_most_one(test_list)
    print(f"The length of the longest qualifying subarray is: {result}")


if __name__ == "__main__":
    main()
```