import sys
import string
from collections import Counter

def normalize_text(text):
    """
    Normalize the input text by converting to lowercase and replacing
    non-alphabetic characters with spaces.
    """
    # Create a translation table that maps all non-alphabetic characters to space
    trans_table = str.maketrans({ch: ' ' for ch in string.punctuation + string.digits})
    # Translate and convert to lowercase
    cleaned = text.translate(trans_table).lower()
    # Replace any remaining non-alphabetic characters with space (e.g. whitespace remains)
    # Split on whitespace to isolate words
    return cleaned

def extract_words(text):
    """
    Extract words from normalized text. Words are sequences of alphabetic characters.
    """
    words = []
    for token in text.split():
        # Keep only tokens that are purely alphabetic
        if token.isalpha():
            words.append(token)
    return words

def get_top_five_words(words):
    """
    Given a list of words, return a list of tuples (word, count) of the top 5 most frequent words.
    In case of ties, words are sorted alphabetically.
    """
    counter = Counter(words)
    # Create a list of (word, count) sorted by count desc, then alphabetically asc
    sorted_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:5]

def main():
    """
    Main function to read filename from command line argument, process the file,
    and print the top 5 most frequent words with their counts.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Could not read file '{filename}': {e}")
        sys.exit(1)

    normalized_text = normalize_text(text)
    words = extract_words(normalized_text)
    if not words:
        print("No valid words found in the file.")
        sys.exit(0)

    top_five = get_top_five_words(words)
    # Output the result
    for word, count in top_five:
        print(f"{word} {count}")

if __name__ == "__main__":
    main()