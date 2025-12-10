```python
#!/usr/bin/env python3
"""
Prime Filter Module

This script defines a function to filter prime numbers from a given list of integers.
It includes input validation and raises appropriate exceptions for invalid inputs.

The prime checking is optimized for integers up to the range reasonably expected in the input list.
"""

from math import isqrt
from typing import List


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Returns a list containing only the prime numbers from the input list.

    :param numbers: List of integers to filter.
    :return: List of prime integers.
    :raises TypeError: If input is not a list or contains non-integers.
    :raises ValueError: If the list contains integers less than 2.
    """

    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__}")

    # Validate that all elements are integers and >= 2
    for i, num in enumerate(numbers):
        if not isinstance(num, int):
            raise TypeError(f"Element at index {i} is not an integer: {repr(num)}")
        if num < 2:
            raise ValueError(f"Element at index {i} is less than 2 (not prime): {num}")

    def is_prime(n: int) -> bool:
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        limit = isqrt(n)
        # Check divisors of form 6k ± 1 up to sqrt(n)
        for i in range(5, limit + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]


def main():
    """Main function demonstrating usage of filter_primes."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 prime_filter.py <int1> <int2> ...")
        print("Example: python3 prime_filter.py 3 4 5 6 7 8 9 10")
        return

    try:
        input_numbers = [int(arg) for arg in sys.argv[1:]]
        primes = filter_primes(input_numbers)
        print("Primes in input:", primes)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```