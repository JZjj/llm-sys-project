import sys
from typing import Tuple


def longest_unique_substring(s: str) -> Tuple[int, str]:
    """
    Finds the longest substring without repeating characters in the given string.

    Args:
        s (str): The input string to search.

    Returns:
        Tuple[int, str]: A tuple containing the length of the longest substring
                         and the substring itself.
    """
    start = 0
    max_length = 0
    max_start = 0
    used_chars = {}

    for i, char in enumerate(s):
        # If the character was seen and is inside the current window, move start
        if char in used_chars and used_chars[char] >= start:
            start = used_chars[char] + 1
        used_chars[char] = i

        current_length = i - start + 1
        if current_length > max_length:
            max_length = current_length
            max_start = start

    return max_length, s[max_start:max_start + max_length]


def read_file_contents(filepath: str) -> str:
    """
    Reads the contents of a file safely.

    Args:
        filepath (str): Path to the file to read.

    Returns:
        str: Contents of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    with open(filepath, 'r', encoding='ascii') as f:
        return f.read()


def main() -> None:
    """
    Main function to demonstrate reading a file and finding the longest substring
    without repeating characters. Reads the filename from command line arguments.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]

    try:
        content = read_file_contents(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: File '{filename}' contains non-ASCII characters.", file=sys.stderr)
        sys.exit(1)

    length, substring = longest_unique_substring(content)
    print(f"Length of longest substring without repeating characters: {length}")
    print(f"Longest substring without repeating characters: {substring}")


if __name__ == "__main__":
    main()