```python
import bisect
import sys

def length_of_lis(nums):
    """
    Returns the length of the longest strictly increasing subsequence in nums.
    Uses a patience sorting approach with O(n log n) time complexity.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    for num in nums:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers.")
    sub = []
    for num in nums:
        # Locate the insertion point for num in sub to maintain sorted order.
        i = bisect.bisect_left(sub, num)
        # If num is larger than any element in sub, append it.
        if i == len(sub):
            sub.append(num)
        else:
            # Otherwise, replace the element at the found position.
            sub[i] = num
    return len(sub)


def main():
    # Read input list from stdin, expecting space-separated integers.
    try:
        input_line = input("Enter a list of integers separated by spaces: ").strip()
        if not input_line:
            print(0)
            return
        nums = list(map(int, input_line.split()))
    except (ValueError, EOFError):
        print("Invalid input. Please enter only integers separated by spaces.", file=sys.stderr)
        sys.exit(1)

    try:
        result = length_of_lis(nums)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(result)


if __name__ == "__main__":
    main()
```