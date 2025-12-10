```python
#!/usr/bin/env python3
"""
A Python program that defines a function to filter prime numbers from a list of integers,
returning them sorted in ascending order.

The program includes:
- Efficient primality testing using 6k ± 1 optimization.
- Input validation with appropriate error handling.
- Designed to handle large input lists gracefully.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using an efficient algorithm.

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

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w  # alternate between adding 2 and 4 (checks 6k ± 1)
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter prime numbers from a list of integers and return them sorted ascendingly.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers from the input list.

    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    # Validate all elements are integers
    for idx, item in enumerate(numbers):
        if not isinstance(item, int):
            raise TypeError(f"All elements must be integers. Invalid element at index {idx}: {repr(item)}")

    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    """
    Example usage and basic interactive test.
    """
    import sys

    def print_usage():
        print("Usage: python3 script.py <space-separated list of integers>")
        print("Example: python3 script.py 10 3 5 8 13 21 2")

    args = sys.argv[1:]

    if not args:
        print("No input provided.")
        print_usage()
        sys.exit(1)

    try:
        input_numbers = [int(arg) for arg in args]
    except ValueError as e:
        print(f"Error: All inputs must be integers. {e}")
        print_usage()
        sys.exit(1)

    try:
        primes = filter_primes(input_numbers)
    except TypeError as e:
        print(f"Input error: {e}")
        sys.exit(1)

    print("Prime numbers (sorted):", primes)


if __name__ == "__main__":
    main()
```