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

def filter_primes(numbers: List[int]) -> List[int]:
    """
    Returns a list of prime numbers filtered from the input list.
    Handles empty list and negative numbers gracefully.
    """
    return [num for num in numbers if is_prime(num)]

def main() -> None:
    sample_inputs = [
        [],  # empty list
        [-10, -3, 0, 1, 2, 3, 4, 5],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [29, 31, 37, 41, 43, 47, 53, 59],
        [1000003, 1000033, 1000037, 1000039],  # large primes
    ]

    for idx, numbers in enumerate(sample_inputs, 1):
        primes = filter_primes(numbers)
        print(f"Test case {idx}: Input: {numbers}")
        print(f"Prime numbers: {primes}\n")

if __name__ == "__main__":
    main()
```