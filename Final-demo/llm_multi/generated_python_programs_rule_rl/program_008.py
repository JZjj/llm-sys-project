def find_anagrams(target, words):
    """
    Returns a list of strings from 'words' that are anagrams of the 'target' word.
    Comparison ignores case and whitespace, but returned strings maintain original formatting.
    """
    normalized_target = ''.join(target.lower().split())
    sorted_target = sorted(normalized_target)

    return [word for word in words if sorted(''.join(word.lower().split())) == sorted_target]


if __name__ == "__main__":
    target_word = "listen"
    word_list = ["enlist", "google", "in lets", "banana"]
    result = find_anagrams(target_word, word_list)
    print(result)  # Expected output: ['enlist', 'in lets']