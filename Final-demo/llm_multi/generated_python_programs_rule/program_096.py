```python
#!/usr/bin/env python3
"""
Remove prime numbers from a list of integers.

This program defines a function that takes a list of integers and returns a new list
with all prime numbers removed. The function validates input types and uses an efficient
primality test to handle large lists. The original list is not modified.

Usage example:
    result = remove_primes([2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)  # Output: [4, 6, 8, 9, 10]
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using an efficient method.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def remove_primes(numbers: List[int]) -> List[int]:
    """
    Return a new list with all prime numbers removed from the input list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A new list with prime numbers removed.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for idx, element in enumerate(numbers):
        if not isinstance(element, int):
            raise TypeError(
                f"All elements must be integers. Invalid element at index {idx}: {repr(element)}"
            )
    return [num for num in numbers if not is_prime(num)]


def main():
    # Example usage and basic test
    test_lists = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 13, 17, 19, 23, 29],
        [1, 0, -3, -5, 15, 21, 22],
        [],
        [4, 6, 8, 9, 10]
    ]
    for lst in test_lists:
        try:
            filtered = remove_primes(lst)
            print(f"Original list: {lst}")
            print(f"Without primes: {filtered}\n")
        except Exception as e:
            print(f"Error processing list {lst}: {e}")


if __name__ == "__main__":
    main()
```