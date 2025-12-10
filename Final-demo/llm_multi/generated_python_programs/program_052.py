```python
def group_strings_by_length(strings):
    length_dict = {}
    for s in strings:
        length_dict.setdefault(len(s), []).append(s)
    for length in length_dict:
        length_dict[length].sort(key=str.lower)
    return length_dict


if __name__ == "__main__":
    example = ["apple", "bat", "arm", "banana", "Ant"]
    result = group_strings_by_length(example)
    print(result)
```