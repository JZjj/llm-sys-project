import sys
import string
from collections import Counter

def read_file(filename):
    """
    Reads the content of a text file.
    Returns the content as a string.
    Raises FileNotFoundError or IOError if file cannot be read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def normalize_text(text):
    """
    Converts text to lowercase and removes punctuation.
    Returns a list of words.
    """
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return words

def get_top_words(words, top_n=5):
    """
    Returns a list of tuples (word, frequency) for the top_n most common words.
    In case of frequency ties, words are sorted alphabetically.
    """
    counter = Counter(words)
    # Create a list of (word, count) pairs
    # Sort primarily by count descending, secondarily by word ascending
    sorted_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:top_n]

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    try:
        text = read_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)

    words = normalize_text(text)
    if not words:
        print("No words found in the file.")
        sys.exit(0)

    top_words = get_top_words(words, top_n=5)
    for word, freq in top_words:
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()