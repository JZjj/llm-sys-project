```python
#!/usr/bin/env python3
"""
A module to find anagrams of a given word from a list of words.
The function is case-insensitive but preserves original casing in output.
"""

from typing import List


def find_anagrams(word: str, word_list: List[str]) -> List[str]:
    """
    Find all anagrams of the given word in the word_list.

    Args:
        word (str): The word to find anagrams of.
        word_list (List[str]): The list of candidate words.

    Returns:
        List[str]: A list of anagrams from word_list matching the word.
    """
    if not isinstance(word, str) or not isinstance(word_list, list):
        # Defensive programming: Type check inputs
        return []

    normalized_word = ''.join(sorted(word.lower()))

    anagrams = []
    for candidate in word_list:
        if not isinstance(candidate, str):
            continue
        if len(candidate) != len(word):
            continue
        if ''.join(sorted(candidate.lower())) == normalized_word:
            anagrams.append(candidate)

    return anagrams


def main():
    # Example usage and simple tests
    examples = [
        ("listen", ["enlists", "google", "inlets", "banana", "Silent"]),
        ("", ["", "a", ""]),
        ("a", ["A", "b", "aa", ""]),
        ("earth", ["heart", "hater", "rathe", "arthe", "other"]),
        ("NoAnagram", []),
        ("test", ["tset", "sett", "estt", "test", "taste"]),
        ("Case", ["case", "Case", "aces", "seca", "caSe", "scae"]),
        ("123", ["321", "132", "213", "312", "231", "123", "124"]),
    ]

    for word, word_list in examples:
        result = find_anagrams(word, word_list)
        print(f"Anagrams of '{word}' in {word_list}:\n  {result}\n")


if __name__ == "__main__":
    main()
```