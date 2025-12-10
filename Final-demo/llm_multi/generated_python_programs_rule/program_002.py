```python
import re
from collections import Counter
from typing import List, Dict

def count_words(strings: List[str]) -> Dict[str, int]:
    """
    Counts occurrences of unique words across a list of strings,
    ignoring case and considering only alphabetic characters as words.

    Args:
        strings (List[str]): List of input strings.

    Returns:
        Dict[str, int]: Dictionary mapping words to their counts.
    """
    word_pattern = re.compile(r'[a-zA-Z]+')
    counter = Counter()

    for text in strings:
        # Defensive check: ensure input is string to avoid unexpected errors
        if not isinstance(text, str):
            continue
        # Find all alphabetic words
        words = word_pattern.findall(text)
        # Convert to lowercase to ensure case-insensitivity
        lowered_words = (word.lower() for word in words)
        counter.update(lowered_words)

    return dict(counter)


def main():
    # Example usage
    input_strings = ["Hello, world!", "The world is big.", "Hello again."]
    result = count_words(input_strings)
    print(result)


if __name__ == '__main__':
    main()
```