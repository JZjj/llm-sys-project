```python
import re
from collections import Counter
from typing import List, Tuple

def top_three_words(text: str) -> List[Tuple[str, int]]:
    """
    Returns the top three most frequent words in the input text along with their counts.
    The function is case-insensitive, ignores punctuation, and handles ties by alphabetical order.

    :param text: Input paragraph as a string.
    :return: List of tuples [(word, count), ...] sorted by count descending then word ascending.
    """
    if not text:
        return []

    # Normalize case
    lowered_text = text.lower()
    # Extract words: sequences of alphanumeric characters and apostrophes inside words
    # Leading/trailing apostrophes are excluded by the regex pattern
    words = re.findall(r"\b[a-z0-9]+(?:'[a-z0-9]+)*\b", lowered_text)

    if not words:
        return []

    counts = Counter(words)

    # Sort by (-count, word) to get descending frequency and ascending alphabetical order
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    return sorted_words[:3]

def main():
    # Example usage and simple test cases
    test_paragraphs = [
        "",
        "!!! ??? ...",  # no valid words
        "Hello hello HELLO, world! World world.",
        "Apple banana apple Banana orange ORANGE banana apple.",
        "Tie tie tie apple apple banana banana carrot carrot",
        "It's a test. It's only a test!",
        "Word, word. word-word? word! word's words.",
    ]

    for i, paragraph in enumerate(test_paragraphs, 1):
        result = top_three_words(paragraph)
        print(f"Test case {i}: {result}")

if __name__ == "__main__":
    main()
```