import re
from collections import Counter

def unique_word_frequency_sorter(text):
    """
    Takes a string and returns a list of unique words sorted by frequency (descending)
    and alphabetically (ascending) for ties. Words are case-insensitive and returned in lowercase.
    """
    words = re.findall(r'[a-zA-Z]+', text)
    words_lower = [word.lower() for word in words]
    freq = Counter(words_lower)
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, _ in sorted_words]

if __name__ == "__main__":
    input_text = "Hello, hello! Are you there? Yes, you are there."
    result = unique_word_frequency_sorter(input_text)
    print(result)  # Expected: ['are', 'hello', 'there', 'you', 'yes']