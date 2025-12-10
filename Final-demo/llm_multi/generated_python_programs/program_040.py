```python
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    result = []
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    for num in nums:
        if num in duplicates and num not in result:
            result.append(num)
    return result

def main():
    try:
        input_str = input("Enter a list of integers separated by spaces: ")
        nums = list(map(int, input_str.strip().split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    duplicates = find_duplicates(nums)
    print(duplicates)

if __name__ == "__main__":
    main()
```