```python
#!/usr/bin/env python3
"""
Module to filter prime numbers from a list of integers.

The is_prime function uses an efficient algorithm for primality testing.
The filter_primes function validates input and returns a list of primes only.
"""

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_primes(numbers):
    """
    Filter and return prime numbers from the input list.

    Args:
        numbers (list): List of integers.

    Returns:
        list: List of prime integers from the input.

    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    primes = []
    for idx, num in enumerate(numbers):
        if not isinstance(num, int):
            raise TypeError(f"Element at index {idx} is not an integer.")
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    """
    Main function to demonstrate filter_primes usage.
    """
    import sys

    args = sys.argv[1:]
    if not args:
        print("Usage: python3 prime_filter.py <int1> <int2> ...")
        print("Example: python3 prime_filter.py 3 4 5 6 7 8 9 10")
        sys.exit(1)

    try:
        input_numbers = [int(arg) for arg in args]
    except ValueError as e:
        print(f"Error: All inputs must be integers. {e}")
        sys.exit(1)

    try:
        primes = filter_primes(input_numbers)
    except TypeError as e:
        print(f"Input error: {e}")
        sys.exit(1)

    print("Prime numbers:", primes)


if __name__ == "__main__":
    main()
```