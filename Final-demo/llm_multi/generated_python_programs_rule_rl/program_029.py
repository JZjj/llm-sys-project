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
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc"]
    grouped = group_anagrams(input_words)
    print(grouped)