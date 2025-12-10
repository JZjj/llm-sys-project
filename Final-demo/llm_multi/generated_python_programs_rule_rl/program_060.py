def find_anagrams(target_word, words):
    """
    Returns a list of strings from 'words' that are anagrams of 'target_word'.
    Comparison is case-insensitive, and order is preserved.
    """
    normalized_target = sorted(target_word.lower())
    return [word for word in words if sorted(word.lower()) == normalized_target]


if __name__ == "__main__":
    target = "listen"
    word_list = ["enlists", "google", "inlets", "banana"]
    anagrams = find_anagrams(target, word_list)
    print(anagrams)  # Expected output: ['inlets']