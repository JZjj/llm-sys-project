```python
#!/usr/bin/env python3
"""
This program defines a function to filter prime numbers from a list of integers,
returning a sorted list of primes. It includes efficient primality checking
and handles edge cases such as empty input or lists without prime numbers.
"""

from math import isqrt
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using 6k ± 1 optimization.

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
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def filter_primes(nums: List[int]) -> List[int]:
    """
    Filter and return prime numbers from the input list, sorted in ascending order.

    Args:
        nums (List[int]): List of integers.

    Returns:
        List[int]: Sorted list of prime numbers found in nums.
    """
    # Using a generator expression for memory efficiency
    primes = (num for num in nums if is_prime(num))
    return sorted(primes)


def main() -> None:
    """
    Example usage and simple tests for the filter_primes function.
    """
    test_cases = [
        [],
        [0, 1, 4, 6, 8, 9],
        [2, 3, 5, 7, 11],
        [15, 21, 23, 29, 30],
        [-3, -2, 2, 3],
        [1000003, 1000033, 1000037, 1000039, 1000081],  # Larger primes and non-primes
    ]

    for i, case in enumerate(test_cases, start=1):
        result = filter_primes(case)
        print(f"Test case {i}: input={case}")
        print(f"  Primes found: {result}\n")


if __name__ == "__main__":
    main()
```