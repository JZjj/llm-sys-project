import re
from typing import List, Dict

def map_word_lengths(words: List[str]) -> Dict[int, List[str]]:
    """
    Takes a list of strings and returns a dictionary mapping each unique word length
    to a sorted list of unique words of that length.
    Uniqueness is determined ignoring case, but original casing is preserved.
    Non-alphabetic characters are removed from words before processing.
    """
    length_to_words = {}
    seen_words = set()  # To track lowercase words for uniqueness

    for raw_word in words:
        cleaned_word = re.sub(r'[^a-zA-Z]', '', raw_word)
        if not cleaned_word:
            continue

        word_lower = cleaned_word.lower()
        if word_lower in seen_words:
            continue

        seen_words.add(word_lower)
        word_len = len(cleaned_word)

        length_to_words.setdefault(word_len, []).append(cleaned_word)

    for length in length_to_words:
        length_to_words[length].sort(key=str.lower)

    return length_to_words


if __name__ == "__main__":
    example_input = ["Hello!", "world", "HELLO", "Python3", "code", "Code."]
    result = map_word_lengths(example_input)
    print(result)  # Expected: {5: ["Hello", "world"], 6: ["Python"], 4: ["code"]}