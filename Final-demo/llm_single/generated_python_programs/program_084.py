import sys
import string
from collections import Counter

def normalize_text(text):
    """
    Normalize the input text by converting to lowercase and removing non-alphabetic characters.
    Returns a list of words.
    """
    # Replace punctuation with spaces
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text = text.translate(translator)
    # Convert to lowercase and split by whitespace
    words = text.lower().split()
    # Filter out any non-alphabetic words
    words = [word for word in words if word.isalpha()]
    return words

def get_top_five_words(filename):
    """
    Reads the file, counts word frequencies, and returns the top 5 most frequent words
    along with their counts. Ties are resolved alphabetically.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied while trying to read '{filename}'.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the file: {e}")

    words = normalize_text(text)
    word_counts = Counter(words)

    # Sort by frequency (descending) then alphabetically (ascending)
    sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

    # Return top 5
    return sorted_words[:5]

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        top_words = get_top_five_words(filename)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()