```python
from collections import Counter

def find_anagrams(words, target):
    """
    Find all anagrams of the target string in the given list of words.

    Parameters:
    - words: list of lowercase strings
    - target: a single lowercase string

    Returns:
    - list of strings from words that are anagrams of target
    """
    if not isinstance(words, list) or not isinstance(target, str):
        return []

    target_counter = Counter(target)
    target_length = len(target)

    result = []
    for word in words:
        if (
            isinstance(word, str)
            and len(word) == target_length
            and Counter(word) == target_counter
        ):
            result.append(word)
    return result


# Example usage and simple test
if __name__ == "__main__":
    sample_words = ['enlist', 'google', 'inlets', 'banana', 'silent']
    target_word = 'listen'
    anagrams = find_anagrams(sample_words, target_word)
    print(f"Anagrams of '{target_word}' in list: {anagrams}")
```