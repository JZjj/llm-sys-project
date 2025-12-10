```python
#!/usr/bin/env python3
"""
Program: filter_primes.py
Description: Provides a function to filter prime numbers from a list of integers.
Author: OpenAI Assistant
Date: 2024-06-15
"""

import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Efficiently check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filters a list of integers, returning only the prime numbers in original order.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: List containing only prime numbers from the input list.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be of type list, got {type(numbers).__name__}")

    primes = []
    for idx, num in enumerate(numbers):
        if not isinstance(num, int):
            raise TypeError(f"Element at index {idx} is not an integer: {type(num).__name__}")
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    # Example usage and simple test cases:
    test_cases = [
        [2, 3, 4, 5, 16, 17, 18, 19, 20],
        [0, 1, -3, 7, 11, 13, 22, 23, 24],
        [],
        [29],
        [1000003, 1000033, 1000037, 1000039, 1000081],  # Large primes and close composite
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            primes = filter_primes(case)
            print(f"Test case {i}: Input: {case}\n  Primes: {primes}\n")
        except Exception as e:
            print(f"Test case {i} raised an error: {e}\n")


if __name__ == "__main__":
    main()
```