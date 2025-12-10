from typing import List
from collections import Counter


def is_anagram_of_palindrome(s: str) -> bool:
    """
    Check if the given string is an anagram of a palindrome.
    The check is case-insensitive and ignores non-alphabetic characters.
    """
    filtered_chars = (ch.lower() for ch in s if ch.isalpha())
    char_counts = Counter(filtered_chars)
    odd_count = sum(count % 2 for count in char_counts.values())
    return odd_count <= 1


def filter_anagrams_of_palindrome(strings: List[str]) -> List[str]:
    """
    Given a list of strings, return a new list containing only those strings
    that are anagrams of a palindrome.
    """
    return [s for s in strings if is_anagram_of_palindrome(s)]


if __name__ == "__main__":
    input_strings = ["carrace", "daily", "aabb", "abc"]
    result = filter_anagrams_of_palindrome(input_strings)
    print(result)  # Expected output: ['carrace', 'aabb']