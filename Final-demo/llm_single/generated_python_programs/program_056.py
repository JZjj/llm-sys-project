import sys
import string
from collections import Counter

def normalize_word(word):
    """
    Normalize a word by stripping punctuation and converting to lowercase.
    """
    return word.strip(string.punctuation).lower()

def get_most_common_words(filename, top_n=10):
    """
    Reads the given file and returns the top_n most common words with their counts.
    Words are compared case-insensitively and punctuation is ignored.
    """
    word_counter = Counter()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Split line into words and normalize
                words = (normalize_word(word) for word in line.split())
                # Filter out empty strings resulted from normalization
                filtered_words = filter(None, words)
                word_counter.update(filtered_words)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read file '{filename}'.")
    except Exception as e:
        # Unexpected exceptions are re-raised with a generic message
        raise RuntimeError(f"An error occurred while processing the file '{filename}': {e}")
    
    return word_counter.most_common(top_n)

def main():
    if len(sys.argv) != 2:
        print("Usage: python word_counter.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        common_words = get_most_common_words(filename)
        print(f"Top 10 most common words in '{filename}':")
        for word, count in common_words:
            print(f"{word}: {count}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()