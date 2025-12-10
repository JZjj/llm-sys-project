```python
import bisect


def length_of_lis(nums):
    """
    Returns the length of the longest strictly increasing subsequence in nums.
    Uses a patience sorting based algorithm with O(n log n) complexity.
    """
    if not nums:
        return 0

    sub = []
    for x in nums:
        i = bisect.bisect_left(sub, x)
        if i == len(sub):
            sub.append(x)
        else:
            sub[i] = x
    return len(sub)


def main():
    try:
        nums = list(map(int, input("Enter integers separated by spaces: ").split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    result = length_of_lis(nums)
    print(result)


if __name__ == "__main__":
    main()
```