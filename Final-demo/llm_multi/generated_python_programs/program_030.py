```python
from collections import defaultdict

def longest_subarray(nums):
    if not nums:
        return 0

    count = defaultdict(int)
    left = 0
    max_len = 0

    for right, num in enumerate(nums):
        count[num] += 1

        while max(count.keys()) - min(count.keys()) > 1:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3, 1, 2], 3),
        ([1, 1, 1, 1], 4),
        ([4, 5, 5, 6, 7, 7, 8], 3),
        ([1, 3, 5, 7], 1),
        ([], 0),
        ([1, 2, 1, 2, 1, 2], 6),
        ([10], 1),
        ([1, 2, 3, 2, 2, 1, 1, 2], 5),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = longest_subarray(nums)
        print(f"Test case {i}: Input: {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print()
```