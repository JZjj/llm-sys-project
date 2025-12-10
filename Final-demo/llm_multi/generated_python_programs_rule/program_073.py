```python
import math
from typing import List


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def extract_sorted_primes(numbers: List[int]) -> List[int]:
    """Extract prime numbers from the list and return them sorted ascending.

    Args:
        numbers (List[int]): List of integers.

    Raises:
        TypeError: If input is not a list or elements are not integers.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__} instead.")

    primes = []
    for idx, value in enumerate(numbers):
        if not isinstance(value, int):
            raise TypeError(
                f"All elements must be integers. Element at index {idx} is of type {type(value).__name__}."
            )
        if is_prime(value):
            primes.append(value)

    return sorted(primes)


def main():
    # Example usage and simple test cases
    test_cases = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10],  # typical
        [],  # empty list
        [1, 0, -3, 17, 19, 23],  # negative and non-prime numbers
        [29, 11, 13, 5],  # all primes
        [10, 15, 20],  # no primes
    ]

    for i, test in enumerate(test_cases, start=1):
        try:
            primes = extract_sorted_primes(test)
            print(f"Test case {i}: Input: {test} -> Primes: {primes}")
        except Exception as e:
            print(f"Test case {i}: Input: {test} -> Error: {e}")


if __name__ == "__main__":
    main()
```