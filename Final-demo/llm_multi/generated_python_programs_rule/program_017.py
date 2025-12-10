```python
#!/usr/bin/env python3
import sys
import math
from typing import List

def is_prime(n: int) -> bool:
    """
    Efficiently check if a number is prime.
    Handles large integers gracefully.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Returns a sorted list of prime numbers found in the input list.
    """
    return sorted(num for num in numbers if is_prime(num))

def parse_input(input_str: str) -> List[int]:
    """
    Parses a space-separated string of integers.
    Raises ValueError on invalid input.
    """
    if not input_str.strip():
        return []

    parts = input_str.strip().split()
    numbers = []
    for p in parts:
        try:
            # int() handles leading '+' and '-' correctly
            num = int(p)
            numbers.append(num)
        except ValueError:
            raise ValueError(f"Invalid integer value: '{p}'")
    return numbers

def main() -> None:
    print("Enter space-separated integers (e.g. 2 3 4 5 23):")
    try:
        user_input = input()
    except EOFError:
        user_input = ""

    try:
        numbers = parse_input(user_input)
    except ValueError as e:
        print(f"Input error: {e}", file=sys.stderr)
        sys.exit(1)

    primes = filter_and_sort_primes(numbers)
    print(primes)

if __name__ == "__main__":
    main()
```