```python
#!/usr/bin/env python3
"""
Module to filter prime numbers from a list of integers.

Includes input validation and efficient primality checking.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Uses an efficient method:
    - Handles small numbers and even numbers quickly.
    - Tests divisors up to sqrt(n).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Return a list containing only the prime numbers from the input list.

    Args:
        numbers: List of integers.

    Returns:
        List of prime integers found in the input list.

    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    for idx, num in enumerate(numbers):
        if not isinstance(num, int):
            raise TypeError(
                f"All elements must be integers. Element at index {idx} is of type {type(num).__name__}."
            )

    return [num for num in numbers if is_prime(num)]


def main():
    # Example usage and simple test cases
    test_lists = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 13, 17, 19, 23, 29],
        [0, 1, -3, -5, 15, 21],
        [],
        [999983, 999979, 999961],  # large primes
    ]

    for i, lst in enumerate(test_lists, start=1):
        try:
            primes = filter_primes(lst)
            print(f"Test case {i}: Input: {lst}")
            print(f"           Primes: {primes}\n")
        except Exception as e:
            print(f"Test case {i} raised an exception: {e}\n")


if __name__ == "__main__":
    main()
```