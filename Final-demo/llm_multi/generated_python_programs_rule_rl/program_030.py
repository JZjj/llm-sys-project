def group_words_by_length(words):
    """
    Receives a list of strings and returns a dictionary mapping each unique word length
    to a list of all words of that length, sorted alphabetically.
    Ignores strings containing non-alphabetic characters.
    Grouping is case-insensitive but original case is preserved in output.
    """
    length_dict = {}

    for word in words:
        if not isinstance(word, str):
            continue
        # Ignore words with non-alphabetic characters
        if not word.isalpha():
            continue

        length = len(word)
        length_dict.setdefault(length, []).append(word)

    # Sort each list alphabetically, case-insensitive but preserve original case
    for length in length_dict:
        length_dict[length].sort(key=lambda w: w.lower())

    return length_dict


if __name__ == "__main__":
    sample_words = ["Apple", "banana", "Cherry", "date", "egg", "Fig", "grape2"]
    result = group_words_by_length(sample_words)
    print(result)