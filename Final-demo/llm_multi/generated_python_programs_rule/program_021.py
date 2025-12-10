```python
#!/usr/bin/env python3
"""
Program to filter prime numbers from a list of integers,
returning them sorted in ascending order.

Primality check uses an efficient algorithm:
- Handles numbers < 2 as non-prime
- Checks divisibility by 2 and 3 quickly
- Uses 6k ± 1 optimization up to sqrt(n)
"""

import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Efficiently check if n is a prime number.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter prime numbers from the input list and return them sorted.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    for idx, num in enumerate(numbers):
        if not isinstance(num, int):
            raise TypeError(f"Element at index {idx} is not an integer")

    primes = sorted(n for n in numbers if is_prime(n))
    return primes


def main() -> None:
    """
    Demonstrate filter_primes function with sample input.
    """
    sample_input = [
        29, 15, 3, 8, 23, 42, 97, 77, 2, 0, -3, 5, 11, 4,
        19, 1, 49, 53, 17, 6,
    ]
    primes = filter_primes(sample_input)
    print("Original list: ", sample_input)
    print("Prime numbers sorted: ", primes)


if __name__ == "__main__":
    main()
```