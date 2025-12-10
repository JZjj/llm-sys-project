import re
from collections import Counter

def count_words(text):
    """
    Count occurrences of each unique word in the given multi-line text.
    Words are sequences of alphabetic characters, case-insensitive.
    Punctuation, numbers, and other symbols are ignored.

    Args:
        text (str): Multi-line input string.

    Returns:
        dict: Mapping of word (lowercase) to count.
    """
    words = re.findall(r'[A-Za-z]+', text)
    normalized_words = (word.lower() for word in words)
    return dict(Counter(normalized_words))

if __name__ == "__main__":
    sample_text = """
    Hello, world! This is a test.
    This test includes multiple lines,
    some repeated words: hello, Hello, HELLO.
    Numbers like 123 and symbols #! are ignored.
    """
    counts = count_words(sample_text)
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")