import sys
import re
from collections import Counter


def extract_words(text):
    """
    Extracts words from the given text.
    Words are defined as sequences of alphabetic characters.
    Returns a list of lowercase words.
    """
    # Use regex to find sequences of alphabetic characters
    words = re.findall(r"[A-Za-z]+", text)
    # Convert all words to lowercase for case-insensitive counting
    return [word.lower() for word in words]


def get_top_words(words, top_n=5):
    """
    Returns the top_n most common words with their counts.
    Sorted by frequency descending, then alphabetically ascending.
    """
    # Count word frequencies
    counter = Counter(words)
    # Sort items by frequency descending, then word ascending
    sorted_items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    # Return top_n items or all if fewer than top_n
    return sorted_items[:top_n]


def process_file(file_path):
    """
    Reads the file at file_path, extracts words, and returns top words with counts.
    Raises exceptions if file cannot be read.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = extract_words(text)
    return get_top_words(words)


def main():
    """
    Entry point of the program.
    Expects a single command line argument: the path to the text file.
    Prints the top words and their counts.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_path>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        top_words = process_file(file_path)
        if not top_words:
            print("No words found in the file.")
            return
        for word, count in top_words:
            print(f"{word} {count}")
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied: {file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()