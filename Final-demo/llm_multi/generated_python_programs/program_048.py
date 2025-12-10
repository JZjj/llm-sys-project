```python
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
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


def filter_and_sort_primes(numbers: list[int]) -> list[int]:
    """Return a sorted list of prime numbers from the given list."""
    return sorted(num for num in numbers if is_prime(num))


def main():
    # Example usage and simple test cases
    test_cases = [
        [3, 4, 7, 10, 11, 13, 16],
        [0, 1, 2, 3, 5, 7, 9],
        [],
        [15, 21, 22, 24],
        [29, 2, 17, 23, 4, 6]
    ]

    for i, case in enumerate(test_cases, 1):
        result = filter_and_sort_primes(case)
        print(f"Test case {i}: input = {case}")
        print(f"Prime numbers sorted: {result}\n")


if __name__ == "__main__":
    main()
```