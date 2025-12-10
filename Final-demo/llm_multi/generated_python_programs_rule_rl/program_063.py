import string

def group_words_by_length(words):
    """
    Groups words by their length after stripping non-alphabetic characters
    from the start and end, ignoring case for grouping but preserving original casing
    in the output lists. The lists are sorted alphabetically (case-insensitive).
    
    Parameters:
        words (list of str): List of input words.
        
    Returns:
        dict: Dictionary mapping word length (int) to list of words (list of str).
    """
    if not words:
        return {}

    result = {}
    alphabetic_chars = set(string.ascii_letters)

    for word in words:
        if not word:
            continue

        # Strip non-alphabetic characters from start
        start = 0
        while start < len(word) and word[start] not in alphabetic_chars:
            start += 1
        # Strip non-alphabetic characters from end
        end = len(word) - 1
        while end >= start and word[end] not in alphabetic_chars:
            end -= 1

        cleaned_word = word[start:end+1] if start <= end else ''

        if cleaned_word:
            length = len(cleaned_word)
            result.setdefault(length, []).append(cleaned_word)

    # Sort each list alphabetically, ignoring case but preserving original casing
    for length in result:
        result[length].sort(key=str.lower)

    return result


if __name__ == "__main__":
    test_words = [
        "Hello!", "world", "Python3", "is", "great.", "!!!Amazing!!!", "test-case",
        "123", "", "End.", "start-", "middle", "UPPER", "lower", "MiXeD"
    ]

    grouped = group_words_by_length(test_words)
    for length in sorted(grouped):
        print(f"Length {length}: {grouped[length]}")