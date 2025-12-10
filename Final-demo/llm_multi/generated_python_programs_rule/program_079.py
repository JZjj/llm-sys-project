```python
#!/usr/bin/env python3
"""
Program to filter prime numbers from a list and return them sorted in ascending order.

The primality test uses a deterministic variant of the Miller-Rabin test for 32-bit integers
to ensure efficiency and correctness for large input lists.

Only the Python standard library is used.
"""


def is_prime(n: int) -> bool:
    """
    Efficiently tests whether n is prime using deterministic Miller-Rabin test
    for 32-bit integers.
    Returns True if n is prime, else False.
    """
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Decompose n-1 as d * 2^r with d odd
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Deterministic bases for 32-bit integers (per research on Miller-Rabin)
    # Source: https://en.wikipedia.org/wiki/Miller–Rabin_primality_test
    test_bases = [2, 7, 61]
    for a in test_bases:
        if a > n - 2:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def filter_and_sort_primes(numbers):
    """
    Takes an iterable of integers and returns a new list containing only the prime numbers 
    from the original iterable, sorted in ascending order.
    """
    # Using a generator expression for memory efficiency on large inputs
    primes = (num for num in numbers if is_prime(num))
    return sorted(primes)


def main():
    # Example usage:
    sample_numbers = [29, 15, 3, 8, 23, 42, 19, 1, 0, -5, 2, 7, 13, 11]
    primes_sorted = filter_and_sort_primes(sample_numbers)
    print("Prime numbers (sorted):", primes_sorted)


if __name__ == "__main__":
    main()
```