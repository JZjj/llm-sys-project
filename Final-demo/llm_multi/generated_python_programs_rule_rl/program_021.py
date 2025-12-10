import string

def find_anagrams(target, words):
    """
    Returns a list of strings from 'words' that are anagrams of 'target'.
    Comparison is case-insensitive and ignores spaces and punctuation.
    The order of returned list matches the order of 'words'.
    """
    translator = str.maketrans('', '', string.punctuation + ' ')

    def normalize(s):
        cleaned = s.translate(translator).lower()
        return ''.join(sorted(cleaned))

    normalized_target = normalize(target)
    return [word for word in words if normalize(word) == normalized_target]

if __name__ == "__main__":
    target_word = "Listen"
    word_list = ["enlist", "Google", "in lets", "banana"]
    anagrams = find_anagrams(target_word, word_list)
    print(anagrams)  # Expected output: ['enlist', 'in lets']