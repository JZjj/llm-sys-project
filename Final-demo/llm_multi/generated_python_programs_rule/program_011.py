```python
#!/usr/bin/env python3
"""
A module to find anagrams of a given word from a list of candidate words.

An anagram is defined as a word formed by rearranging the letters of another,
using all the original letters exactly once. The comparison is case-insensitive,
but original casing from candidates is preserved in the output.
"""

from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    """
    Returns a list of anagrams of `word` found in `candidates`.

    Args:
        word (str): The reference word to find anagrams of.
        candidates (List[str]): A list of candidate words.

    Returns:
        List[str]: List of anagrams from candidates preserving original casing.
    """
    if not word or not candidates:
        return []

    normalized_word = word.lower()
    sorted_word = sorted(normalized_word)

    result = []
    for candidate in candidates:
        if len(candidate) != len(word):
            continue

        normalized_candidate = candidate.lower()
        if normalized_candidate == normalized_word:
            continue

        if sorted(normalized_candidate) == sorted_word:
            result.append(candidate)

    return result


def main() -> None:
    """
    Example usage of find_anagrams function.
    """
    word = "listen"
    candidates = ["enlists", "google", "inlets", "banana"]

    anagrams = find_anagrams(word, candidates)
    print(anagrams)


if __name__ == "__main__":
    main()
```