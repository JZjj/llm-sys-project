```python
import collections
from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    """
    Return a list of anagrams of `word` found in `candidates`.
    An anagram is defined as a word formed by rearranging the letters of another,
    using all the original letters exactly once.
    The comparison is case-insensitive.
    The original word is not considered its own anagram.

    Parameters:
        word (str): The word to find anagrams of.
        candidates (List[str]): List of candidate words.

    Returns:
        List[str]: List of anagrams from candidates.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If word or any candidate is an empty string.
    """
    if not isinstance(word, str):
        raise TypeError(f"Expected 'word' to be str, got {type(word).__name__}")
    if not isinstance(candidates, list):
        raise TypeError(f"Expected 'candidates' to be list, got {type(candidates).__name__}")
    if not word:
        raise ValueError("Input 'word' must not be empty string")

    normalized_word = word.lower()
    word_counter = collections.Counter(normalized_word)

    anagrams = []
    for candidate in candidates:
        if not isinstance(candidate, str):
            raise TypeError(f"All candidates must be strings, got {type(candidate).__name__}")
        if not candidate:
            raise ValueError("Candidates must not contain empty strings")
        if len(candidate) != len(word):
            continue

        normalized_candidate = candidate.lower()
        if normalized_candidate == normalized_word:
            continue

        if collections.Counter(normalized_candidate) == word_counter:
            anagrams.append(candidate)

    return anagrams


if __name__ == "__main__":
    try:
        result = find_anagrams("listen", ["enlists", "google", "inlets", "banana"])
        print(result)  # Expected output: ['inlets']
    except Exception as e:
        print(f"Error: {e}")
```