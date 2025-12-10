```python
import sys
import math

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
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

def filter_primes(numbers: list[int]) -> list[int]:
    """Return a list of prime numbers from the input list, preserving order."""
    return [num for num in numbers if is_prime(num)]

def main():
    try:
        line = input()
        tokens = line.strip().split()
        numbers = []
        for token in tokens:
            # Validate integer token explicitly
            if token.startswith('-'):
                if len(token) == 1 or not token[1:].isdigit():
                    print("Error: invalid input")
                    return
            elif not token.isdigit():
                print("Error: invalid input")
                return
            num = int(token)
            numbers.append(num)
    except Exception:
        print("Error: invalid input")
        return

    primes = filter_primes(numbers)
    print(primes)

if __name__ == "__main__":
    main()
```