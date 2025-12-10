```python
#!/usr/bin/env python3
"""
A Python program that defines a function to filter prime numbers from a list of integers,
preserving their original order. The primality check is implemented efficiently using
deterministic Miller-Rabin test suitable for 64-bit integers.

Only the Python standard library is used.
"""

import sys
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using a deterministic Miller-Rabin primality test.

    This implementation is valid for 64-bit integers.

    Args:
        n (int): The integer to test for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    # Check small primes to quickly filter
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23)
    for sp in small_primes:
        if n == sp:
            return True
        if n % sp == 0:
            return False

    # Miller-Rabin test bases for 64-bit determinism
    # Source: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    test_bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    # Write n-1 as d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    def check(a: int, d: int, n: int, s: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    for a in test_bases:
        if a % n == 0:
            # a and n are equal => n is prime
            return True
        if not check(a, d, n, s):
            return False
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filters and returns only the prime numbers from the input list, preserving order.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        List[int]: List of prime integers from input.
    """
    return [num for num in numbers if is_prime(num)]


def main():
    """
    Reads integers from standard input, one per line, until EOF.
    Prints the filtered list of prime numbers as space-separated integers.
    """
    input_numbers = []
    try:
        for line in sys.stdin:
            line = line.strip()
            if line:
                # Safely parse integers; skip invalid lines silently
                try:
                    num = int(line)
                    input_numbers.append(num)
                except ValueError:
                    # Ignore lines that don't represent valid integers
                    continue
    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        pass

    primes = filter_primes(input_numbers)
    print(" ".join(str(p) for p in primes))


if __name__ == "__main__":
    main()
```