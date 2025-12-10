import re
from collections import Counter
from typing import List, Dict

def count_words(strings: List[str]) -> Dict[str, int]:
    """
    Counts occurrences of each unique word (case-insensitive) across all input strings.
    Words are sequences of alphabetic characters only.
    Ignores empty strings and non-alphabetic characters.
    
    Args:
        strings (List[str]): List of input strings.
    
    Returns:
        Dict[str, int]: Dictionary mapping words to their counts.
    """
    word_counter = Counter()
    word_pattern = re.compile(r'[a-zA-Z]+')

    for text in strings:
        if not text:
            continue
        words = word_pattern.findall(text)
        word_counter.update(word.lower() for word in words)

    return dict(word_counter)


if __name__ == "__main__":
    sample_input = [
        "Hello, world! This is a test.",
        "Testing, one, two, three...",
        "HELLO again; testing continues.",
        "",
        "123 numbers and symbols #!$ are ignored."
    ]
    result = count_words(sample_input)
    for word, count in sorted(result.items()):
        print(f"{word}: {count}")