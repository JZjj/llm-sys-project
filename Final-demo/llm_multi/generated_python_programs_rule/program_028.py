```python
def find_anagrams(word, word_list):
    """
    Find all anagrams of a given word within a list of words.

    Args:
        word (str): The word to find anagrams of.
        word_list (List[str]): The list of words to check.

    Returns:
        List[str]: A list of anagrams from word_list matching the word.
    """
    if not isinstance(word, str) or not isinstance(word_list, list):
        return []

    normalized_word = word.lower()
    sorted_word = sorted(normalized_word)

    result = []
    for candidate in word_list:
        if not isinstance(candidate, str):
            continue
        if len(candidate) != len(word):
            continue
        if sorted(candidate.lower()) == sorted_word:
            result.append(candidate)

    return result


if __name__ == "__main__":
    test_word = "listen"
    test_list = ["enlists", "google", "inlets", "banana"]
    print(find_anagrams(test_word, test_list))  # Output: ['inlets']
```