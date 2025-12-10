```python
def find_anagrams(strings):
    if not strings:
        return []
    
    first_sorted = sorted(strings[0].lower())
    first_lower = strings[0].lower()
    
    result = []
    for s in strings[1:]:
        if s.lower() != first_lower and sorted(s.lower()) == first_sorted:
            result.append(s)
    return result


if __name__ == "__main__":
    # Example usage and simple test
    test_cases = [
        ["listen", "enlists", "Google", "inlets", "banana", "Silent"],
        ["Race", "Care", "acre", "hello", "race"],
        ["abc", "bca", "cab", "bac", "cba", "abc"],
        ["hello"],
        [],
        ["a", "A", "b", "B"],
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"Test case {i}: {test}")
        print("Anagrams of first string:", find_anagrams(test))
        print()
```