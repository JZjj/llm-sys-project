```python
from collections import defaultdict

def find_anagrams(words):
    # Dictionary to group words by their sorted character tuple
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)

    # Collect words that have at least one anagram (more than one word in group)
    result_set = {word for group in groups.values() if len(group) > 1 for word in group}

    return sorted(result_set)


if __name__ == "__main__":
    # Example usage
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc"]
    output_words = find_anagrams(input_words)
    print(output_words)
```