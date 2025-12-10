```python
import math
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime efficiently."""
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Takes a list of integers and returns a sorted list of prime numbers.
    If no primes found, returns an empty list.
    """
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes

def main():
    # Example usage and simple test cases
    test_lists = [
        [10, 11, 12, 13, 14, 15, 16, 17],
        [4, 6, 8, 10, 12],
        [2, 3, 5, 7, 11, 13, 17, 19],
        [0, 1, -3, -5, 23, 29, 31],
        []
    ]

    for i, lst in enumerate(test_lists, 1):
        primes = filter_and_sort_primes(lst)
        print(f"Test case {i}: Input: {lst}")
        print(f"           Primes: {primes}\n")

if __name__ == "__main__":
    main()
```