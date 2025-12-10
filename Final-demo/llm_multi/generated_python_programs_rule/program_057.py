```python
import math
from typing import List

def is_prime(n: int) -> bool:
    """
    Efficiently check if a number is prime.
    Handles edge cases and avoids expensive operations for large n.
    """
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
    Return a list of prime numbers from the input list.
    """
    return [num for num in numbers if is_prime(num)]

def main():
    input_list = [2, 3, 4, 17, 19, 20, 23, 24, 25, 7919, 7920]
    primes = filter_primes(input_list)
    print("Input numbers:", input_list)
    print("Prime numbers:", primes)

if __name__ == "__main__":
    main()
```