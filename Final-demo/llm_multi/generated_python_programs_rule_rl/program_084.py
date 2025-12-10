from collections import OrderedDict

def group_anagrams(words):
    """
    Groups words into lists of anagrams, ignoring case.

    Args:
        words (list of str): List of input words.

    Returns:
        list of lists of str: Groups of anagrams preserving original order.
    """
    anagram_groups = OrderedDict()

    for word in words:
        key = ''.join(sorted(word.lower()))
        anagram_groups.setdefault(key, []).append(word)

    return list(anagram_groups.values())

if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
    grouped = group_anagrams(input_words)
    print(grouped)