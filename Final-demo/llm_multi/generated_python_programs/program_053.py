```python
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime efficiently."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_primes(nums: List[int]) -> List[int]:
    """Return a sorted list of prime numbers from the input list."""
    primes = [x for x in nums if is_prime(x)]
    primes.sort()
    return primes

def main():
    # Example usage:
    input_list = [29, 15, 3, 8, 22, 17, 1, 0, -5, 2, 97, 100, 101]
    result = filter_primes(input_list)
    print("Input list:", input_list)
    print("Primes sorted:", result)

if __name__ == "__main__":
    main()
```