```python
#!/usr/bin/env python3

import sys
import math

def is_prime(n: int) -> bool:
    """
    Efficiently checks if a number is prime.
    Handles edge cases and uses 6k ± 1 optimization.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_and_sort_primes(numbers: list[int]) -> list[int]:
    """
    Returns a sorted list of prime numbers from the given list.
    """
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes

def parse_input(input_str: str) -> list[int]:
    """
    Parses a string of space-separated integers.
    Raises ValueError if any token is invalid.
    """
    tokens = input_str.strip().split()
    if not tokens:
        raise ValueError("No input provided.")
    numbers = []
    for token in tokens:
        # Validate each token strictly as a base-10 integer
        if token.startswith(('+', '-')):
            if len(token) == 1 or not token[1:].isdigit():
                raise ValueError(f"Invalid integer token: '{token}'")
        elif not token.isdigit():
            raise ValueError(f"Invalid integer token: '{token}'")
        try:
            number = int(token)
        except Exception as e:
            # This should not happen given above checks but just in case
            raise ValueError(f"Invalid integer token: '{token}'") from e
        numbers.append(number)
    return numbers

def main():
    print("Enter a sequence of integers separated by spaces:")
    try:
        input_line = sys.stdin.readline()
        if not input_line:
            print("No input received. Exiting.", file=sys.stderr)
            sys.exit(1)
        numbers = parse_input(input_line)
    except ValueError as err:
        print(f"Input error: {err}", file=sys.stderr)
        sys.exit(1)

    primes_sorted = filter_and_sort_primes(numbers)
    if primes_sorted:
        print("Sorted prime numbers:")
        print(" ".join(str(p) for p in primes_sorted))
    else:
        print("No prime numbers found in the input.")

if __name__ == "__main__":
    main()
```