import string

def find_anagrams(target, words):
    """
    Returns a list of strings from 'words' that are anagrams of 'target'.
    Comparison is case-insensitive and ignores spaces and punctuation.
    """
    def normalize(s):
        allowed_chars = set(string.ascii_lowercase + string.digits)
        s = s.lower()
        filtered = [ch for ch in s if ch in allowed_chars]
        return ''.join(sorted(filtered))
    
    normalized_target = normalize(target)
    return [word for word in words if normalize(word) == normalized_target]

if __name__ == "__main__":
    target_word = "Listen"
    word_list = [
        "enlist",
        "google",
        "in lets",
        "Silent",
        "Tinsel!",
        "banana",
        "Listen."
    ]
    anagrams = find_anagrams(target_word, word_list)
    print(f"Anagrams of '{target_word}':")
    for anagram in anagrams:
        print(anagram)