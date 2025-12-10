from collections import defaultdict

def group_anagrams(words):
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words (list of str): List of lowercase words.

    Returns:
        list of list of str: Groups of anagrams.
    """
    anagram_map = defaultdict(list)
    for word in words:
        # Use the sorted tuple of characters as the key
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

if __name__ == "__main__":
    # Example usage
    input_words = ["listen", "silent", "enlist", "hello", "ohlle", "world"]
    grouped = group_anagrams(input_words)
    print(grouped)