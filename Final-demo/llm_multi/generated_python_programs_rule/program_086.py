```python
import math
from typing import List

def is_prime(n: int) -> bool:
    """Check if an integer n is prime.

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
    """Extract prime numbers from the list and return them sorted in ascending order.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    # Use a generator expression for memory efficiency on large inputs
    primes = sorted(num for num in numbers if is_prime(num))
    return primes

def main():
    # Example usage and simple test
    test_input = [29, 15, 23, 8, 5, 1, 0, -7, 11, 4, 2, 37, 97, 100, 101]
    result = extract_sorted_primes(test_input)
    print("Input:", test_input)
    print("Primes sorted:", result)

if __name__ == "__main__":
    main()
```