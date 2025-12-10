import sys
import string
from collections import Counter

def read_file(filename):
    """
    Reads the contents of a file.
    Raises FileNotFoundError if the file does not exist.
    Raises IOError for other I/O issues.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def normalize_text(text):
    """
    Converts text to lowercase and removes punctuation.
    Returns a list of words.
    """
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    cleaned_text = text.translate(translator)
    words = cleaned_text.lower().split()
    return words

def get_top_frequent_words(words, top_n=5):
    """
    Returns a list of tuples (word, count) for the top_n most frequent words.
    Sorted by frequency descending.
    If fewer than top_n unique words, returns all.
    """
    counter = Counter(words)
    most_common = counter.most_common(top_n)
    return most_common

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        text = read_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)

    words = normalize_text(text)

    if not words:
        print("No words found in the file.")
        sys.exit(0)

    top_words = get_top_frequent_words(words, 5)

    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()