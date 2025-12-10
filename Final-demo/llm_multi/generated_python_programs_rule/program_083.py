```python
#!/usr/bin/env python3
"""
A Python program that defines a function to filter prime numbers from a list of integers.
The primes are returned sorted in ascending order.
Includes robust input validation and efficient primality checking.
"""


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if prime, False otherwise.
    """
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


def filter_primes(nums):
    """
    Filter and return prime numbers from the input list sorted ascendingly.

    Args:
        nums (list): List of integers.

    Returns:
        list: Sorted list of prime numbers.

    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")

    for i, x in enumerate(nums):
        if not isinstance(x, int):
            raise TypeError(f"All elements must be integers. Element at index {i} is type {type(x).__name__}.")

    primes = [num for num in nums if is_prime(num)]
    return sorted(primes)


def main():
    """
    Main function to demonstrate filter_primes function.
    Reads integers from command line arguments and prints primes found.
    """
    import sys

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <int1> <int2> ...", file=sys.stderr)
        sys.exit(1)

    try:
        input_numbers = [int(arg) for arg in sys.argv[1:]]
    except ValueError as e:
        print(f"Error: All inputs must be integers. {e}", file=sys.stderr)
        sys.exit(1)

    try:
        primes = filter_primes(input_numbers)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print("Prime numbers found:", primes)


if __name__ == "__main__":
    main()
```