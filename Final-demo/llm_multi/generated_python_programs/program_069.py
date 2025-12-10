```python
from collections import defaultdict

def find_anagrams(words):
    """
    Takes a list of strings and returns a new list containing only those strings
    that are anagrams of at least one other string in the original list.
    Comparison is case insensitive.
    The order of strings in the returned list is the same as their order in the input list.
    """
    anagram_groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        anagram_groups[key].append(word)

    return [word for word in words if len(anagram_groups[''.join(sorted(word.lower()))]) > 1]


if __name__ == "__main__":
    # Example usage
    input_list = ["listen", "silent", "enlist", "hello", "world"]
    output_list = find_anagrams(input_list)
    print(output_list)  # Expected: ['listen', 'silent', 'enlist']
```