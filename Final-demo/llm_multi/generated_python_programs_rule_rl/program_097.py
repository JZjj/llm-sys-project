import re
from collections import Counter

def top_frequent_words(text, stopwords):
    """
    Returns a list of the top 10 most frequent words in `text` that are not in `stopwords`.
    Words are compared case-insensitively, punctuation and numeric characters are ignored.
    The returned list contains tuples (word, frequency), sorted by frequency descending,
    then alphabetically for ties.
    """
    words = re.findall(r'[a-zA-Z]+', text)
    words_lower = (word.lower() for word in words)
    filtered_words = (word for word in words_lower if word not in stopwords)
    freq = Counter(filtered_words)
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:10]

if __name__ == "__main__":
    text = '''
    In computer science, a trie, also called digital tree or prefix tree, is a kind of search tree—an ordered tree data structure 
    used to store a dynamic set or associative array where the keys are usually strings.
    '''
    stopwords = ['a', 'or', 'to', 'the', 'in', 'is', 'of', 'and', 'where']
    result = top_frequent_words(text, stopwords)
    print(result)