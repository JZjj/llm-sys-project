import sys
import string
from collections import Counter

def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome."""
    return word == word[::-1]

def sanitize_word(word: str) -> str:
    """Remove non-alphabetical characters and convert to lowercase."""
    return ''.join(ch for ch in word if ch.isalpha()).lower()

def get_top_palindromic_words(file_path: str, top_n: int = 5) -> Counter:
    """
    Read a file and return the top N most frequent palindromic words.
    Words are sequences of alphabetical characters only.
    """
    palindromic_counter = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Split line by whitespace to get words
                raw_words = line.strip().split()
                for raw_word in raw_words:
                    word = sanitize_word(raw_word)
                    if word and is_palindrome(word):
                        palindromic_counter[word] += 1
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"IO error while reading file '{file_path}': {e}", file=sys.stderr)
        sys.exit(1)

    return palindromic_counter.most_common(top_n)

def main():
    """Example usage of the program."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_path>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    top_palindromes = get_top_palindromic_words(file_path)

    if not top_palindromes:
        print("No palindromic words found.")
        return

    print("Top palindromic words and their counts:")
    for word, count in top_palindromes:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()