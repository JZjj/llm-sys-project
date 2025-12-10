```python
#!/usr/bin/env python3
"""
A module to filter prime numbers from a list of integers.

The function prime_filter takes a list of integers and returns a new list containing only the prime numbers.
It performs input validation and handles edge cases securely and robustly.
"""

import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Parameters:
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


def prime_filter(numbers: List[int]) -> List[int]:
    """
    Filter prime numbers from a list of integers.

    Parameters:
        numbers (List[int]): The list of integers.

    Returns:
        List[int]: A new list containing only prime numbers found in the input list.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__}")
    for i, element in enumerate(numbers):
        if not isinstance(element, int):
            raise TypeError(f"All elements must be integers. Invalid element at index {i}: {type(element).__name__}")

    return [num for num in numbers if is_prime(num)]


def main():
    # Example usage with different test cases:
    test_cases = [
        [],
        [0, 1, -3, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23, 24, 25],
        [-10, -7, -5, -2, 0, 1],
        [29, 31, 37, 41, 43, 47],
        [4, 6, 8, 9, 10, 12],
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            primes = prime_filter(case)
            print(f"Test case {i}: Input: {case}")
            print(f"           Primes: {primes}\n")
        except Exception as e:
            print(f"Test case {i} raised an exception: {e}\n")


if __name__ == "__main__":
    main()
```