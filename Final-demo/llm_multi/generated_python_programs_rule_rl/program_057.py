from typing import List, Dict

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of groups, each containing anagrams.
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        # Sort the word to get the anagram key
        key = ''.join(sorted(word))
        # Append the word to the corresponding anagram group
        anagram_map.setdefault(key, []).append(word)

    # Return the list of anagram groups
    return list(anagram_map.values())

if __name__ == "__main__":
    # Example usage
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
    grouped = group_anagrams(input_words)
    print(grouped)