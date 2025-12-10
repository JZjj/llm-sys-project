```python
#!/usr/bin/env python3
"""
A Python program that defines a function to extract prime numbers from a list of integers,
returning them sorted in ascending order. Includes input validation and efficient primality checking.
"""

import sys
import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Checks if a given integer n is prime.

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

    # Check divisors up to sqrt(n) using 6k ± 1 optimization
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def extract_primes(numbers: List[int]) -> List[int]:
    """
    Extracts prime numbers from the input list and returns them sorted in ascending order.

    Args:
        numbers (List[int]): List of integers to process.

    Returns:
        List[int]: Sorted list containing only the prime numbers from the input.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__}.")

    primes = []
    for idx, element in enumerate(numbers):
        if not isinstance(element, int):
            raise TypeError(f"Element at index {idx} is not an integer (got {type(element).__name__}).")
        if is_prime(element):
            primes.append(element)

    return sorted(primes)


def main():
    """
    Demonstration main function. Accepts command-line integer arguments, extracts primes, and prints them.
    """
    try:
        input_args = sys.argv[1:]
        if not input_args:
            print("Usage: python3 script.py <int1> <int2> ...", file=sys.stderr)
            sys.exit(1)

        input_numbers = []
        for i, arg in enumerate(input_args):
            try:
                num = int(arg)
            except ValueError:
                print(f"Invalid integer argument at position {i + 1}: '{arg}'", file=sys.stderr)
                sys.exit(1)
            input_numbers.append(num)

        primes = extract_primes(input_numbers)
        print(primes)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```