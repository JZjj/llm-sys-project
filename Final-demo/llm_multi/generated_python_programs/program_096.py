```python
import math
from typing import List

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes

def main():
    inputs = [
        [10, 3, 5, 6, 7, 11, 13, 4],
        [1, 4, 6, 8, 10],
        [],
        [29, 15, 3, 2, 17, 19],
        [999983, 1000000, 500000, 2]
    ]

    for i, lst in enumerate(inputs, 1):
        primes = filter_and_sort_primes(lst)
        print(f"Test case {i}: Input: {lst}")
        print(f"Prime numbers sorted: {primes}\n")

if __name__ == "__main__":
    main()
```