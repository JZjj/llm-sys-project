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
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Returns a list of prime numbers from the input list sorted in ascending order.
    If no primes are found, returns an empty list.
    """
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes

def main():
    example_list = [29, 15, 3, 8, 22, 7, 11, 4, 1, 0, 13, 17, 23, 35]
    primes = filter_and_sort_primes(example_list)
    print("Original list:", example_list)
    print("Primes sorted:", primes)

if __name__ == "__main__":
    main()
```