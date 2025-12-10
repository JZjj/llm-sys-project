```python
import math
from typing import List

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Returns True if n is a prime number, else False.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Given a list of integers, returns a new list containing only the prime numbers,
    sorted in ascending order.
    """
    # Use a generator expression inside sorted for memory efficiency
    return sorted(num for num in numbers if is_prime(num))

def main():
    # Example usage with test data
    test_data = [29, 15, 2, 3, 8, 17, 19, 21, 1, 0, -7, 23]
    result = filter_and_sort_primes(test_data)
    print("Prime numbers sorted ascending:", result)

if __name__ == "__main__":
    main()
```