```python
from collections import deque

def longest_subarray_with_diff_at_most_one(nums):
    """
    Returns the length of the longest contiguous subarray where the difference between
    the maximum and minimum elements is at most 1.
    """
    if not nums:
        return 0

    max_deque = deque()  # indexes of max elements in descending order
    min_deque = deque()  # indexes of min elements in ascending order

    left = 0
    max_len = 0

    for right, value in enumerate(nums):
        # Maintain max_deque for max elements (descending)
        while max_deque and nums[max_deque[-1]] < value:
            max_deque.pop()
        max_deque.append(right)

        # Maintain min_deque for min elements (ascending)
        while min_deque and nums[min_deque[-1]] > value:
            min_deque.pop()
        min_deque.append(right)

        # Shrink window from left if difference > 1
        while nums[max_deque[0]] - nums[min_deque[0]] > 1:
            left += 1
            # Remove indexes out of window
            if max_deque[0] < left:
                max_deque.popleft()
            if min_deque[0] < left:
                min_deque.popleft()

        max_len = max(max_len, right - left + 1)

    return max_len

def main():
    example = [4, 2, 2, 3, 1, 2]
    result = longest_subarray_with_diff_at_most_one(example)
    print(f"Input: {example}")
    print(f"Length of longest subarray: {result}")

if __name__ == "__main__":
    main()
```