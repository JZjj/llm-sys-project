```python
def find_anagrams(word, word_list):
    """
    Finds all anagrams of the given word in the provided word_list.

    Args:
        word (str): The word to find anagrams of.
        word_list (list of str): List of candidate words.

    Returns:
        list of str: List containing anagrams of `word` from `word_list` in original casing.
    """
    if not isinstance(word, str) or not isinstance(word_list, list):
        # Defensive programming: if inputs are not of expected types, return empty list
        return []

    normalized_word = sorted(word.lower())

    anagrams = []
    for candidate in word_list:
        if not isinstance(candidate, str):
            # Skip non-string entries to avoid exceptions
            continue
        if candidate.lower() == word.lower():
            # Same word, not considered an anagram
            continue
        if sorted(candidate.lower()) == normalized_word:
            anagrams.append(candidate)
    return anagrams


def main():
    # Example usage and simple tests
    tests = [
        ("listen", ["enlists", "google", "inlets", "banana", "Silent"]),
        ("", ["", "a", " "]),
        ("a", ["A", "b", ""]),
        ("evil", []),
        ("race", ["care", "acer", "race", "RACE", "car"]),
        ("Dormitory", ["Dirty room", "dormitory", "dirtyroom", "dirty room"]),
        ("123", ["231", "312", "213", "abc"]),
        ("!@#", ["#@!", "!#@", "@#!", "abc"]),
        ("aabb", ["baba", "abab", "bbaa", "aabb", "aaab"]),
    ]

    for word, word_list in tests:
        result = find_anagrams(word, word_list)
        print(f"Anagrams of '{word}' in {word_list}: {result}")


if __name__ == "__main__":
    main()
```