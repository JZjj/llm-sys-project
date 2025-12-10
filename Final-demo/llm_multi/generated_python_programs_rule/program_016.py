```python
#!/usr/bin/env python3
"""
Prime filter

This program defines a function that filters prime numbers from a list of integers.
It uses an efficient deterministic primality test (Miller-Rabin) for correctness and performance.
Includes input validation and gracefully handles invalid inputs.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using a deterministic Miller-Rabin primality test.

    Args:
        n (int): The number to test for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    # Handle small primes quickly
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23)
    if n in small_primes:
        return True
    for sp in small_primes:
        if n % sp == 0:
            return False

    # Miller-Rabin test implementation (deterministic bases for 64-bit range)
    # Reference: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    # Deterministic bases for testing 64-bit integers:
    # According to research, testing a fixed set of bases below is enough for 64-bit range.
    # For larger integers, the test becomes probabilistic but still reliable for practical purposes.

    def miller_rabin_test(d: int, n: int, a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d <<= 1
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    # Write n-1 as d*2^r
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Select bases depending on the size of n for deterministic results on 64-bit integers.
    # For numbers larger than 2^64, this test is probabilistic.
    if n < 1373653:
        test_bases = [2, 3]
    elif n < 9080191:
        test_bases = [31, 73]
    elif n < 4759123141:
        test_bases = [2, 7, 61]
    elif n < 2**32:
        test_bases = [2, 3, 5, 7, 11]
    elif n < 2**64:
        test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    else:
        test_bases = [2, 3, 5, 7, 11]

    for a in test_bases:
        if a >= n:
            break
        if not miller_rabin_test(d, n, a):
            return False
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter and return only the prime numbers from the input list, preserving order.

    Args:
        numbers (List[int]): List of integers to filter primes from.

    Returns:
        List[int]: List containing only prime numbers from the input.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for i, num in enumerate(numbers):
        if not isinstance(num, int):
            raise TypeError(f"All elements must be integers. Element at index {i} is {type(num).__name__}.")

    return [num for num in numbers if is_prime(num)]


def main():
    # Example usage and simple test cases
    test_lists = [
        [2, 3, 4, 5, 15, 17, 19, 20, 23, 24, 25],
        [0, 1, -3, -5, 29, 31, 37],
        [],
        [10**10 + 19, 10**10 + 21],  # large numbers (one prime, one not)
        ['a', 2],  # test invalid input handling
    ]

    for idx, lst in enumerate(test_lists, 1):
        print(f"Test case {idx}: input: {lst}")
        try:
            result = filter_primes(lst)
            print(f"Primes: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
```