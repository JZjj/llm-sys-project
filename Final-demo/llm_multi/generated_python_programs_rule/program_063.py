```python
#!/usr/bin/env python3
"""
Find the length of the longest contiguous subarray where the absolute difference
between any two elements is at most 1.

Time complexity: O(n)
"""

from typing import List
from collections import defaultdict


def longest_subarray(nums: List[int]) -> int:
    if not nums:
        return 0

    count = defaultdict(int)
    left = 0
    max_len = 1

    for right, val in enumerate(nums):
        count[val] += 1

        # Shrink window while invalid: difference between max and min keys > 1
        while max(count.keys()) - min(count.keys()) > 1:
            left_val = nums[left]
            count[left_val] -= 1
            if count[left_val] == 0:
                del count[left_val]
            left += 1

        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len


def main() -> None:
    import sys

    data = sys.stdin.read().strip()
    if not data:
        print(0)
        return

    try:
        nums = list(map(int, data.split()))
    except ValueError:
        print("Invalid input. Please provide a list of integers separated by whitespace.", file=sys.stderr)
        sys.exit(1)

    result = longest_subarray(nums)
    print(result)


if __name__ == "__main__":
    main()
```