import sys
import string
from collections import Counter

def process_text(text):
    """
    Process the input text by removing punctuation, converting to lowercase,
    and splitting into words based on whitespace.
    """
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return words

def get_top_five_words(words):
    """
    Given a list of words, return the top 5 most frequent words with their counts.
    If multiple words have the same frequency, they are sorted alphabetically.
    """
    counter = Counter(words)
    # Sort by frequency (descending) then alphabetically (ascending)
    sorted_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:5]

def read_file(filename):
    """
    Read the contents of the given filename safely.
    Raises FileNotFoundError or IOError on failure.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    """
    Main function to execute the program.
    Expects a filename as a command-line argument.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        text = read_file(filename)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)

    words = process_text(text)
    if not words:
        print("No words found in the file.")
        sys.exit(0)

    top_words = get_top_five_words(words)

    # Output the result
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()