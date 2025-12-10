```python
import re
from collections import Counter
from typing import List, Dict


def count_words(strings: List[str]) -> Dict[str, int]:
    """
    Counts occurrences of each unique word (case-insensitive) across all input strings.
    Words are sequences of alphabetic characters (a-z, A-Z).
    Punctuation and numbers are ignored.

    :param strings: List of input strings.
    :return: Dictionary mapping word to its count.
    """
    word_counter = Counter()
    word_pattern = re.compile(r"[a-zA-Z]+")

    if not strings:
        return {}

    for text in strings:
        if not isinstance(text, str):
            continue  # Skip non-string inputs to avoid errors
        words = word_pattern.findall(text)
        word_counter.update(word.lower() for word in words)

    return dict(word_counter)


def main():
    # Example usage and simple test cases
    test_inputs = [
        ["Hello, world!", "Hello there.", "The world is big."],
        ["Apple apple APPLE", ""],
        [],
        ["Numbers 123 should be ignored!", "Punctuations: should; be! removed?"],
        ["Mixed CASE words: Apple, aPPle, ApPlE."]
    ]

    for i, inputs in enumerate(test_inputs, 1):
        print(f"Test case {i}:")
        counts = count_words(inputs)
        for word, count in sorted(counts.items()):
            print(f"  {word}: {count}")
        print()


if __name__ == "__main__":
    main()
```