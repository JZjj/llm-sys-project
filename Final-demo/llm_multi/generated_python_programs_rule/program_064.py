```python
#!/usr/bin/env python3
"""
A Python program that defines a function to filter prime numbers from a list of integers.
The function performs input validation and uses an efficient algorithm for primality testing.
"""

from math import isqrt
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using an efficient deterministic approach.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter prime numbers from a list and return them sorted ascending.

    Args:
        numbers (List[int]): List containing integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers.

    Raises:
        TypeError: If input is not a list or contains non-integers.
        ValueError: If the list is empty.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not numbers:
        raise ValueError("Input list must not be empty.")

    for idx, item in enumerate(numbers):
        if not isinstance(item, int):
            raise TypeError(f"Element at index {idx} is not an integer.")

    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    # Example usage and simple test cases
    test_cases = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 13, 17, 19, 23, 29, 31],
        [0, 1, -3, -5, 2, 3],
        [15, 21, 22, 24],
        [],  # Should trigger ValueError
        [2, "3", 5],  # Should trigger TypeError
    ]

    for index, case in enumerate(test_cases, start=1):
        print(f"Test case {index}: input = {case!r}")
        try:
            result = filter_primes(case)
            print(f"Prime numbers: {result}\n")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
```