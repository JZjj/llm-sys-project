```python
import math
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime efficiently."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check only up to sqrt(n), skipping multiples of 2 and 3
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """Return a sorted list of prime numbers from the input list."""
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes

def main():
    # Example inputs to demonstrate the function
    test_lists = [
        [10, 15, 3, 7, 11, 20, 2, 1, 0, -5],
        [4, 6, 8, 9, 10],
        [29, 23, 17, 19, 13, 11, 7, 5, 3, 2],
        [],
        [1, 1, 1, 1]
    ]

    for i, lst in enumerate(test_lists, start=1):
        primes = filter_and_sort_primes(lst)
        print(f"Test case {i}: Input: {lst}")
        print(f"Prime numbers sorted: {primes}\n")

if __name__ == "__main__":
    main()
```