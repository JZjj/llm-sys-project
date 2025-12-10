```python
import sys
import re
from collections import Counter

def main():
    text = sys.stdin.read().lower()
    pattern = r"\b[a-z]+(?:'[a-z]+)*\b"
    words = re.findall(pattern, text)
    count = Counter(words)
    sorted_words = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for word, freq in sorted_words[:3]:
        print(f"{word} {freq}")

if __name__ == "__main__":
    main()
```