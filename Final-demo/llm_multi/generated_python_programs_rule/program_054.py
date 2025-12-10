```python
#!/usr/bin/env python3
"""
This module provides a function to filter prime numbers from a list of integers,
returning a sorted list of unique prime numbers.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n**0.5)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter and return a sorted list of unique prime numbers from the input list.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        List[int]: Sorted list containing only prime numbers, without duplicates.
    """
    primes = {num for num in numbers if is_prime(num)}
    return sorted(primes)


def main():
    # Example usage and simple tests
    test_cases = [
        [],
        [0, 1, -10, -3],
        [2, 3, 5, 7, 11, 13],
        [4, 6, 8, 9, 10],
        [3, 3, 3, 5, 5, 7, 11, 11, 13, 13],
        [-2, 2, 17, 19, 20, 23, 24, 29, 29]
    ]

    for i, case in enumerate(test_cases, 1):
        result = filter_primes(case)
        print(f"Test case {i}: Input: {case}\n  Primes: {result}\n")


if __name__ == "__main__":
    main()
```