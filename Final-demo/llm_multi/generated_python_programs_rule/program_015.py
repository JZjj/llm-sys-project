```python
#!/usr/bin/env python3
"""
Find the longest substring without repeating characters
Author: Senior Python Engineer
"""

def longest_unique_substring(s: str) -> str:
    """
    Return the longest substring without repeating characters.
    Case-sensitive: 'A' and 'a' are different characters.

    Args:
        s (str): Input string

    Returns:
        str: The longest substring without repeating characters

    Raises:
        TypeError: If input is not of type str
    """
    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, got {type(s).__name__}")

    start = 0
    max_len = 0
    max_start = 0
    index_map = {}

    for i, char in enumerate(s):
        if char in index_map and index_map[char] >= start:
            start = index_map[char] + 1
        index_map[char] = i
        current_len = i - start + 1
        if current_len > max_len:
            max_len = current_len
            max_start = start

    return s[max_start:max_start + max_len]


def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 longest_unique_substring.py <input_string>", file=sys.stderr)
        sys.exit(1)

    input_str = sys.argv[1]
    try:
        result = longest_unique_substring(input_str)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(result)


if __name__ == "__main__":
    main()
```