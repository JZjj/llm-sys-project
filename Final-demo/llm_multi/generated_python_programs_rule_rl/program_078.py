from collections import defaultdict

def group_anagrams(words):
    """
    Groups a list of lowercase alphabetic strings into lists of anagrams.

    Args:
        words (list of str): List of lowercase alphabetic strings.

    Returns:
        list of list of str: List containing groups of anagrams.
    """
    anagram_map = defaultdict(list)
    for word in words:
        # Use a tuple of sorted characters as the key
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

if __name__ == "__main__":
    # Example usage
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
    grouped = group_anagrams(input_words)
    for group in grouped:
        print(group)