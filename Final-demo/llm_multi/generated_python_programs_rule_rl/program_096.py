import re
from collections import Counter
from typing import List, Dict

def count_words(strings: List[str]) -> Dict[str, int]:
    """
    Counts occurrences of each unique word (case-insensitive) across a list of strings.
    Words are sequences of alphabetic characters; punctuation and numbers are ignored.

    Args:
        strings (List[str]): List of input strings.

    Returns:
        Dict[str, int]: Dictionary mapping words to their counts.
    """
    word_counter = Counter()
    word_pattern = re.compile(r'[a-zA-Z]+')  # Matches sequences of alphabetic characters

    for text in strings:
        if not isinstance(text, str):
            # Skip non-string inputs to avoid errors
            continue
        # Find all words in the current string
        words = word_pattern.findall(text)
        # Convert words to lowercase for case-insensitive counting
        word_counter.update(word.lower() for word in words)

    return dict(word_counter)


if __name__ == "__main__":
    # Example usage and simple test cases
    sample_input = [
        "Hello, world! This is a test.",
        "Testing, one, two, three... Testing!",
        "",
        "Numbers 123 and punctuation!!! shouldn't count.",
        "HELLO hello HeLLo"
    ]
    result = count_words(sample_input)
    for word, count in sorted(result.items()):
        print(f"{word}: {count}")