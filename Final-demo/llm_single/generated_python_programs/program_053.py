import sys
import string
from collections import Counter

def normalize_word(word):
    """
    Normalize a word by converting to lowercase and ensuring it contains only alphabetic characters.
    """
    return ''.join(filter(str.isalpha, word.lower()))

def get_top_five_words(filename):
    """
    Reads a file and returns a list of the top 5 most frequent words and their counts.
    Words are sequences of alphabetic characters only, case-insensitive.
    If multiple words have the same frequency, they are sorted alphabetically.
    """
    word_counter = Counter()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Split line into words by whitespace
                raw_words = line.strip().split()
                for raw_word in raw_words:
                    word = normalize_word(raw_word)
                    if word:  # Only count non-empty words
                        word_counter[word] += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        return []
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading '{filename}': {e}", file=sys.stderr)
        return []

    # Sort first by frequency descending, then alphabetically ascending
    top_words = sorted(
        word_counter.items(),
        key=lambda x: (-x[1], x[0])
    )[:5]

    return top_words

def main():
    """
    Main function to accept filename input and display the top 5 most frequent words with counts.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    top_words = get_top_five_words(filename)

    if not top_words:
        # An error occurred or no words found
        sys.exit(1)
    
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()