```python
import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using an efficient method.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Filter prime numbers from the input list and return them sorted in ascending order.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    seen = set()
    primes = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            if is_prime(num):
                primes.append(num)
    primes.sort()
    return primes


def main():
    # Example usage and test
    test_numbers = [
        29, 15, 3, 8, 2, 11, 17, 19, 23, 1, 0, -7, 29, 31, 37, 41, 43, 97, 100,
        7919, 7920, 10007, 10009, 10037, 100003, 100019, 100043
    ]
    primes = filter_and_sort_primes(test_numbers)
    print("Prime numbers from the list (sorted):")
    print(primes)


if __name__ == "__main__":
    main()
```