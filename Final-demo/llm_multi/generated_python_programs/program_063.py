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

def extract_sorted_primes(numbers: List[int]) -> List[int]:
    """
    Extract prime numbers from the input list and return them sorted in ascending order.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        List[int]: Sorted list of primes from the input.
    """
    primes = (num for num in numbers if is_prime(num))
    return sorted(primes)

def main():
    test_list = [
        29, 15, 3, 23, 4, 5, 9, 11, 0, 1, 2, 37, 97, 100, 101, 103, 104, 105,
        7919, 104729, 1299709, 15485863, 32452843, 49999999
    ]
    primes = extract_sorted_primes(test_list)
    print("Primes extracted and sorted:")
    print(primes)

if __name__ == "__main__":
    main()
```