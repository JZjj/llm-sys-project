```python
def group_strings_by_length(strings):
    result = {}
    for s in strings:
        length = len(s)
        result.setdefault(length, []).append(s)
    # Sort each list ignoring case, but preserve original casing
    for length in result:
        result[length].sort(key=str.lower)
    return result


if __name__ == "__main__":
    # Example usage and simple test
    sample_strings = [
        "Apple",
        "banana",
        "Cherry",
        "apricot",
        "blueberry",
        "Avocado",
        "cherry",
        "Banana",
        "date",
        "egg",
        "Fig",
        "grape"
    ]

    grouped = group_strings_by_length(sample_strings)
    for length in sorted(grouped):
        print(f"Length {length}: {grouped[length]}")
```