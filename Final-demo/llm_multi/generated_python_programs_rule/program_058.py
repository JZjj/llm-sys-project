```python
#!/usr/bin/env python3
"""
A Python program that filters prime numbers from a list of integers 
and returns them sorted in ascending order.

The primality test uses an efficient deterministic method suitable for 
integers within typical 64-bit integer range.

Author: ChatGPT
"""

from math import isqrt
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a given integer n is prime.
    Uses trial division up to sqrt(n) with optimizations:
      - eliminate numbers <= 1
      - handle small primes directly
      - check divisibility by 2 and 3
      - check divisors of form 6k ± 1 up to sqrt(n)

    Args:
        n (int): The number to test for primality.

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


def filter_primes(nums: List[int]) -> List[int]:
    """
    Filter prime numbers from the input list and return them sorted ascendingly.

    Args:
        nums (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    # Generator expression to avoid unnecessary intermediate lists
    primes = (num for num in nums if is_prime(num))
    return sorted(primes)


def main():
    import sys

    # Example usage: read integers from command line arguments
    if len(sys.argv) > 1:
        try:
            input_numbers = [int(arg) for arg in sys.argv[1:]]
        except ValueError:
            print("Error: All arguments must be integers.", file=sys.stderr)
            sys.exit(1)
    else:
        # Example hardcoded test list if no input given
        input_numbers = [29, 15, 3, 11, 4, 18, 2, 23, 0, -7, 17]

    primes = filter_primes(input_numbers)
    print("Prime numbers:", primes)


if __name__ == "__main__":
    main()
```