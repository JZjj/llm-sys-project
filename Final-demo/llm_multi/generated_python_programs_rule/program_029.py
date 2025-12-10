```python
#!/usr/bin/env python3
"""
A Python program that provides a function to filter and return prime numbers 
from a given list of integers, sorted in ascending order.

The primality test uses an efficient method that checks divisibility only up to
the integer square root of the candidate number, skipping even numbers after 2.

No external libraries are used; only Python standard library features.
"""

from math import isqrt
from typing import List


def is_prime(n: int) -> bool:
    """
    Efficiently checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = isqrt(n)
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Filters prime numbers from the input list and returns them sorted.

    Args:
        numbers (List[int]): The list of integers to process.

    Returns:
        List[int]: Sorted list containing only prime numbers.
    """
    # Using a generator expression for memory efficiency on large lists
    primes = sorted(num for num in numbers if is_prime(num))
    return primes


def main():
    """
    Example usage and basic test cases.
    """
    example_input = [29, 15, 3, 4, 17, 20, 23, -5, 0, 1, 2, 9973]
    primes = filter_and_sort_primes(example_input)
    print("Input list:", example_input)
    print("Prime numbers sorted:", primes)


if __name__ == "__main__":
    main()
```