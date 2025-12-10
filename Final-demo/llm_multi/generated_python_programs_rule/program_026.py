```python
#!/usr/bin/env python3
"""
Find the longest substring without repeating characters.
"""

def longest_unique_substring(s: str) -> str:
    """
    Returns the longest substring without repeating characters.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: The longest substring without repeating characters.
    """
    last_seen = {}
    start = 0
    max_len = 0
    max_start = 0

    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = i
        current_len = i - start + 1
        if current_len > max_len:
            max_len = current_len
            max_start = start

    return s[max_start:max_start + max_len]


def main():
    test_str = "abcbdeaf"
    result = longest_unique_substring(test_str)
    print(result)  # Expected: "cbdeaf"


if __name__ == "__main__":
    main()
```