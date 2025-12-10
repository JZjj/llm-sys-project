from collections import defaultdict

def group_anagrams(words):
    """
    Groups a list of strings into lists of anagrams.
    Case-insensitive grouping, original casing preserved.

    Parameters:
        words (list of str): List of input words.

    Returns:
        list of list of str: Groups of anagrams.
    """
    if not words:
        return []

    anagram_map = defaultdict(list)

    for word in words:
        # Normalize word to lowercase and sort letters to form the key
        key = ''.join(sorted(word.lower()))
        anagram_map[key].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage
    sample_input = ["listen", "silent", "enlist", "hello", "below", "elbow", "bowl"]
    grouped = group_anagrams(sample_input)
    for group in grouped:
        print(group)