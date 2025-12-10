```python
#!/usr/bin/env python3
"""
A Python program that defines a function to count occurrences of unique strings
in a case-insensitive manner from a list of strings.
"""

def count_strings_case_insensitive(strings):
    """
    Count occurrences of unique strings in a list, case-insensitively.

    Args:
        strings (list of str): List of strings to count.

    Returns:
        dict: A dictionary mapping lowercase strings to their counts.
    """
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings.")
    counts = {}
    for item in strings:
        if not isinstance(item, str):
            raise TypeError("All items in the list must be strings.")
        key = item.casefold()  # casefold for better case-insensitive matching than lower()
        counts[key] = counts.get(key, 0) + 1
    return counts


def main():
    # Example usage:
    example_list = ["Apple", "banana", "APPLE", "Banana", "orange", "ORANGE", "orange"]
    counted = count_strings_case_insensitive(example_list)
    for key, count in counted.items():
        print(f"'{key}': {count}")

if __name__ == "__main__":
    main()
```