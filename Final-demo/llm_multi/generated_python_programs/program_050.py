```python
def longest_subarray_with_diff_at_most_one(arr):
    if not arr:
        return 0

    left = 0
    freq = {}
    max_length = 1

    for right, value in enumerate(arr):
        freq[value] = freq.get(value, 0) + 1

        while max(freq) - min(freq) > 1:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1

        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length


def main():
    s = input("Enter a list of integers (e.g. [1, 2, 2, 3, 1, 2]): ").strip()
    try:
        arr = eval(s, {"__builtins__": None}, {})
        if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
            raise ValueError
    except Exception:
        print("Invalid input format. Please enter a list of integers like [1, 2, 3].")
        return

    result = longest_subarray_with_diff_at_most_one(arr)
    print(result)


if __name__ == "__main__":
    main()
```