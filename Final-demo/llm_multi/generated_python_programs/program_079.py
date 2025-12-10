```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        [],
        ["interspace", "internet", "internal", "interval"],
        ["", "b", "c"],
        ["same", "same", "same"],
        ["prefix", "prefixes", "prefixation"]
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"Test case {i}: {test_case}")
        print(f"Longest common prefix: '{longest_common_prefix(test_case)}'\n")
```