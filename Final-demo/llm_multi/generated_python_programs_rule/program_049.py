```python
import math
from typing import List

def is_prime(n: int) -> bool:
    """
    Efficiently checks if a number is prime.
    Returns True if n is a prime number, False otherwise.
    Handles edge cases such as n < 2.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers: List[int]) -> List[int]:
    """
    Returns a list of prime numbers from the input list,
    preserving their order.
    """
    return [num for num in numbers if is_prime(num)]

def main():
    # Example usage and basic test cases
    test_lists = [
        [],
        [0, 1, -3, -5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        [17, 19, 23, 24, 25, 29],
        [-10, -7, -3],
        [2],
        [1],
    ]

    for i, lst in enumerate(test_lists, 1):
        primes = filter_primes(lst)
        print(f"Test case {i}: Input: {lst}")
        print(f"           Primes: {primes}\n")

if __name__ == "__main__":
    main()
```