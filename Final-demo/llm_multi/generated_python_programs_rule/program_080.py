```python
#!/usr/bin/env python3
"""
Module to find groups of anagrams from a list of lowercase strings.
"""

from typing import List


def find_anagram_groups(words: List[str]) -> List[List[str]]:
    """
    Finds and returns groups of anagrams from the provided list of lowercase strings.

    Parameters:
    - words (List[str]): List of lowercase strings.

    Returns:
    - List[List[str]]: List containing groups (lists) of anagrams.

    Raises:
    - TypeError: If input is not a list or contains non-string elements.
    - ValueError: If any string contains characters other than lowercase alphabets.
    """
    if not isinstance(words, list):
        raise TypeError("Input must be a list.")

    for idx, word in enumerate(words):
        if not isinstance(word, str):
            raise TypeError(f"All elements must be strings. Element at index {idx} is of type {type(word).__name__}.")
        if not word.isalpha() or not word.islower():
            raise ValueError(f"All strings must contain lowercase alphabets only. Invalid string at index {idx}: '{word}'")

    if not words:
        return []

    anagram_map = {}
    for word in words:
        key = ''.join(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    return list(anagram_map.values())


def _run_example():
    example_input = ["listen", "silent", "enlist", "hello", "ohlle"]
    result = find_anagram_groups(example_input)
    print("Anagram groups found:")
    for group in result:
        print(group)


if __name__ == "__main__":
    _run_example()
```