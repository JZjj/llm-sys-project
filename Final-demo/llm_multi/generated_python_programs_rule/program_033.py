```python
import sys
import math
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime using an efficient method."""
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

def filter_primes(numbers: List[int]) -> List[int]:
    """Return a list of prime numbers from the input list, preserving order."""
    return [num for num in numbers if is_prime(num)]

def read_int_sequence_from_input(prompt: str = "Enter integers separated by spaces: ") -> List[int]:
    """
    Reads a sequence of integers from user input (space-separated).
    Continues prompting until valid input is provided.
    """
    while True:
        try:
            line = input(prompt)
            parts = line.strip().split()
            if not parts:
                raise ValueError("No integers entered")
            numbers = []
            for part in parts:
                # Validate integer format explicitly to avoid false positives
                if not (part.lstrip("+-").isdigit() and (part.count('+') + part.count('-') <= 1 and (part[0] in '+-' or part[0].isdigit()))):
                    raise ValueError(f"Invalid integer value: '{part}'")
                num = int(part)
                numbers.append(num)
            return numbers
        except ValueError as e:
            print(f"Error: {e}. Please enter only valid integers separated by spaces.", file=sys.stderr)

def main():
    numbers = read_int_sequence_from_input()
    primes = filter_primes(numbers)
    print(primes)

if __name__ == "__main__":
    main()
```