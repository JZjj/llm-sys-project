```python
#!/usr/bin/env python3
import sys
import collections

def is_anagram(s1: str, s2: str) -> bool:
    """
    Determine whether two strings are anagrams, ignoring case, whitespace,
    and non-alphabetic characters.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        bool: True if s1 and s2 are anagrams, False otherwise.
    """
    filtered_s1 = (ch.lower() for ch in s1 if ch.isalpha())
    filtered_s2 = (ch.lower() for ch in s2 if ch.isalpha())

    return collections.Counter(filtered_s1) == collections.Counter(filtered_s2)


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <string1> <string2>", file=sys.stderr)
        sys.exit(1)

    s1, s2 = sys.argv[1], sys.argv[2]

    print(str(is_anagram(s1, s2)))


if __name__ == "__main__":
    main()
```