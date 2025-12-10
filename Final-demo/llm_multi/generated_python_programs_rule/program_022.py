```python
def remove_duplicates_preserve_order(int_list):
    """
    Returns a new list with duplicates removed, preserving original order.

    :param int_list: list[int]
    :return: list[int]
    """
    seen = set()
    unique_list = []
    for num in int_list:
        if num not in seen:
            seen.add(num)
            unique_list.append(num)
    return unique_list


def main():
    import sys

    try:
        line = sys.stdin.readline()
        if not line:
            print("No input provided.")
            return

        parts = line.strip().split()
        int_values = []
        for part in parts:
            try:
                int_values.append(int(part))
            except ValueError:
                print(f"Warning: '{part}' is not a valid integer and will be ignored.", file=sys.stderr)

        if not int_values:
            print("No valid integers provided.")
            return

        result = remove_duplicates_preserve_order(int_values)
        print(result)

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```