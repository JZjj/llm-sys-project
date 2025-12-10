from collections import defaultdict

def group_anagrams(words):
    """
    Groups a list of strings into lists of anagrams.
    
    Args:
        words (list of str): List of input strings.
        
    Returns:
        list of list of str: List where each sublist contains anagrams.
    """
    anagram_map = defaultdict(list)
    
    for word in words:
        # Normalize the word: lowercase, remove spaces
        normalized = word.replace(" ", "").lower()
        # Sort the characters to form the key
        key = ''.join(sorted(normalized))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())

if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
    grouped = group_anagrams(input_words)
    for group in grouped:
        print(group)