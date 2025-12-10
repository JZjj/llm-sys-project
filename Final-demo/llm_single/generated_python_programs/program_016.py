import sys
import string
from collections import Counter

def normalize_word(word):
    """Normalize word by stripping punctuation and converting to lowercase."""
    return word.strip(string.punctuation).lower()

def get_top_words(file_path, top_n=5):
    """
    Reads a file and returns the top_n most frequent words with counts.
    Words are normalized by ignoring case and punctuation.
    """
    word_counts = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split line into words and normalize
                words = (normalize_word(word) for word in line.split())
                # Filter out empty strings caused by normalization
                filtered_words = filter(None, words)
                word_counts.update(filtered_words)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")

    # Sort words by frequency descending, then alphabetically ascending
    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:top_n]

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_path>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        top_words = get_top_words(file_path)
        for word, count in top_words:
            print(f"{word}: {count}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()