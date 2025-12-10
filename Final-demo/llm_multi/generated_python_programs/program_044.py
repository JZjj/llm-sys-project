```python
import math
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime using an efficient method."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check divisors up to sqrt(n), skipping multiples of 2 and 3
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """Return a sorted list of prime numbers from the input list."""
    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)

def main():
    # Example usage
    sample_list = [15, 3, 5, 8, 13, 22, 29, 1, 0, -7, 17]
    primes = filter_and_sort_primes(sample_list)
    print("Original list:", sample_list)
    print("Primes sorted:", primes)

if __name__ == "__main__":
    main()
```