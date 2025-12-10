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

    # Check divisors up to sqrt(n) using 6k ± 1 optimization
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Return a new list containing only the prime numbers from the original list,
    sorted in ascending order.
    """
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes

def main():
    # Example usage:
    input_list = [10, 3, 5, 4, 7, 11, 13, 17, 19, 23, 24, 25, 29, 97, 1, 0, -3, 2]
    result = filter_and_sort_primes(input_list)
    print("Original list:", input_list)
    print("Prime numbers sorted:", result)

if __name__ == "__main__":
    main()
```