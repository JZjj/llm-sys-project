```python
def group_strings_by_length(strings):
    result = {}
    for s in strings:
        if not s:  # ignore empty strings
            continue
        length = len(s)
        result.setdefault(length, []).append(s)
    for length in result:
        result[length].sort(key=str.lower)
    return result


if __name__ == "__main__":
    sample = ["apple", "Banana", "pear", "Peach", "banana", "APPLE", "", "plum", "Fig", "fig"]
    grouped = group_strings_by_length(sample)
    for length in sorted(grouped):
        print(f"Length {length}: {grouped[length]}")
```