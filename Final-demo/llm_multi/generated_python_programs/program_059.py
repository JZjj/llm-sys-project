```python
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def find_palindrome_pairs(words):
    pairs = []
    n = len(words)
    for i in range(n):
        for j in range(n):
            if i != j:
                concat = words[i] + words[j]
                if is_palindrome(concat):
                    pairs.append((words[i], words[j]))
    return pairs

def main():
    words = [
        "bat",
        "tab",
        "cat",
        "tac",
        "aba",
        "xyz",
        "zyx",
        "a",
        "aa",
    ]
    
    palindrome_pairs = find_palindrome_pairs(words)
    
    print("Palindrome pairs:")
    for pair in palindrome_pairs:
        print(pair)

if __name__ == "__main__":
    main()
```