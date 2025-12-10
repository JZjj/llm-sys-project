```python
def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    input_str = input("Enter a list of integers separated by spaces: ")
    try:
        nums = list(map(int, input_str.strip().split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return
    result = longest_consecutive(nums)
    print(result)


if __name__ == "__main__":
    main()
```