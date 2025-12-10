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
    # Example usage and simple test cases
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interstellar", "internet", "interval"], "int"),
        ([], ""),
        (["same", "same", "same"], "same"),
        (["Case", "case", "cas"], ""),
        (["prefix", "prefixes", "prefixation"], "prefix"),
        (["a", "a", "a"], "a"),
        (["", "b", "c"], ""),
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        result = longest_common_prefix(input_list)
        print(f"Test case {i}: Input: {input_list}")
        print(f"Expected: '{expected}', Got: '{result}'")
        print(f"Pass: {result == expected}\n")
```