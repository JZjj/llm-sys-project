import sys
import string
from collections import Counter

def is_palindrome(word: str) -> bool:
    """
    Check if a given word is a palindrome.
    """
    return word == word[::-1]

def clean_word(word: str) -> str:
    """
    Remove punctuation and convert to lowercase.
    """
    return word.strip(string.punctuation).lower()

def get_top_palindromic_words(filepath: str, top_n: int = 5) -> list[tuple[str, int]]:
    """
    Read the file at filepath and return the top N most common palindromic words with their frequencies.
    """
    counter = Counter()

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                # Split line into words and process each
                for raw_word in line.split():
                    word = clean_word(raw_word)
                    if word and is_palindrome(word):
                        counter[word] += 1
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        return []
    except IOError as e:
        print(f"Error reading file {filepath}: {e}", file=sys.stderr)
        return []

    # Most common palindromic words sorted by frequency descending
    return counter.most_common(top_n)

def main():
    """
    Example usage of the program.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <text_file_path>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    results = get_top_palindromic_words(filepath)

    if not results:
        print("No palindromic words found or error reading file.")
        sys.exit(0)

    print("Top palindromic words with their frequencies:")
    for word, freq in results:
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()