import sys
import string
from collections import Counter

def normalize_word(word):
    """
    Normalize the word by stripping punctuation and converting to lowercase.
    """
    # Strip punctuation from both ends
    return word.strip(string.punctuation).lower()

def get_top_common_words(file_path, top_n=5):
    """
    Reads the file at file_path and returns a list of tuples (word, frequency)
    for the top_n most common words, sorted by frequency descending and then alphabetically.
    """
    word_counts = Counter()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Split line into words
                words = line.split()
                for word in words:
                    normalized = normalize_word(word)
                    if normalized:  # Skip empty strings
                        word_counts[normalized] += 1
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        return []
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}", file=sys.stderr)
        return []

    # Sort by frequency descending, then alphabetically ascending
    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:top_n]

def main():
    """
    Example usage:
    python this_script.py path_to_file.txt
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <text_file_path>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    top_words = get_top_common_words(file_path)

    if top_words:
        for word, freq in top_words:
            print(f"{word}: {freq}")

if __name__ == '__main__':
    main()