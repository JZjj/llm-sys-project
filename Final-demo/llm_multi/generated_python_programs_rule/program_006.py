```python
#!/usr/bin/env python3
"""
A module to check if any anagram of a given string can form a palindrome.
"""

from collections import Counter

def is_anagram_palindrome(s: str) -> bool:
    """
    Determine if any anagram of the input string can form a palindrome.

    The function ignores case and non-alphabetic characters.

    Parameters:
        s (str): The input string to check.

    Returns:
        bool: True if any anagram of `s` can form a palindrome, False otherwise.
    """
    filtered_chars = (ch.lower() for ch in s if ch.isalpha())
    char_counts = Counter(filtered_chars)

    # Count how many characters have an odd frequency
    odd_count = sum(count % 2 for count in char_counts.values())

    # For a palindrome:
    # - At most one character can have an odd count
    return odd_count <= 1


if __name__ == "__main__":
    # Example usage and basic tests
    test_cases = {
        "Tact Coa": True,      # "taco cat"
        "aabbcc": True,        # "abc cba"
        "abc": False,
        "A man, a plan, a canal, Panama!": True,
        "No lemon, no melon": True,
        "": True,
        "1234": True,          # no alphabetic chars, empty considered palindrome
        "abcba": True,
        "abcbad": False,
    }

    for test_str, expected in test_cases.items():
        result = is_anagram_palindrome(test_str)
        print(f"Input: {test_str!r} -> Can form palindrome? {result} (Expected: {expected})")
```