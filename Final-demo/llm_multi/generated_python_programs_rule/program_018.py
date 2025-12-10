```python
import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Efficiently checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
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


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filters and returns only prime numbers from the input list.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: List containing only prime numbers from input.

    Raises:
        TypeError: If the input is not a list of integers.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__!r}")

    for idx, item in enumerate(numbers):
        if not isinstance(item, int):
            raise TypeError(f"All elements must be integers. Element at index {idx} is of type {type(item).__name__!r}")

    return [num for num in numbers if is_prime(num)]


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python primes_filter.py num1 num2 num3 ...")
        print("Example: python primes_filter.py 3 4 5 6 7 8 9 10")
        return

    input_strings = sys.argv[1:]
    try:
        input_numbers = [int(x) for x in input_strings]
    except ValueError as e:
        print(f"Error: All inputs must be integers. {e}")
        return

    try:
        primes = filter_primes(input_numbers)
    except TypeError as e:
        print(f"Error: {e}")
        return

    print("Prime numbers:", primes)


if __name__ == "__main__":
    main()
```