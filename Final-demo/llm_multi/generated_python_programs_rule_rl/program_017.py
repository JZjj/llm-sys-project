def group_words_by_length(words):
    """
    Groups words by their length, ignoring case for grouping but preserving original case.
    Only includes words with alphabetic characters.

    Args:
        words (list of str): List of input words.

    Returns:
        dict: Mapping from word length to list of words of that length, sorted alphabetically ignoring case.
    """
    from collections import defaultdict

    length_to_words = defaultdict(list)

    for word in words:
        if not isinstance(word, str):
            continue
        # Ignore words containing non-alphabetic characters
        if not word.isalpha():
            continue

        length_to_words[len(word)].append(word)

    for length in length_to_words:
        length_to_words[length].sort(key=lambda w: w.lower())

    return dict(length_to_words)


if __name__ == "__main__":
    input_words = ["Apple", "bat", "ball", "Cat", "dog2", "elephant"]
    result = group_words_by_length(input_words)
    print(result)
    # Expected output:
    # {3: ['bat', 'Cat'], 4: ['ball', 'Apple'], 8: ['elephant']}