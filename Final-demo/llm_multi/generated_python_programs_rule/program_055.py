```python
from collections import defaultdict
from typing import List


def find_anagrams(words: List[str]) -> List[List[str]]:
    """
    Given a list of lowercase words, return a list of lists where each sublist
    contains words that are anagrams of each other. Each sublist contains at least two words.
    The output list and each sublist are sorted alphabetically.
    """
    anagram_map = defaultdict(list)
    for word in words:
        # Sort the letters of the word to create a key
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    # Filter groups with at least two words, sort each group and then sort groups by first word
    result = [sorted(group) for group in anagram_map.values() if len(group) > 1]
    result.sort(key=lambda x: x[0])

    return result


if __name__ == "__main__":
    # Example usage
    input_words = ["listen", "silent", "enlist", "hello", "below", "elbow"]
    anagrams = find_anagrams(input_words)
    print(anagrams)
```