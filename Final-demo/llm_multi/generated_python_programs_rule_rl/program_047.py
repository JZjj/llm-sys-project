from collections import defaultdict

def group_anagrams(words):
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words (list of str): List of lowercase alphabetic strings.

    Returns:
        list of list of str: Groups of anagrams.
    """
    if not words:
        return []

    anagram_map = defaultdict(list)
    for word in words:
        # Use the sorted tuple of characters as the key
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage and simple test
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_words)
    print(grouped)  # Output can be in any order, e.g. [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]