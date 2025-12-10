```python
def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

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

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_and_sort_primes(numbers):
    """
    Takes a list of integers and returns a new list containing only the prime numbers,
    sorted in ascending order.

    Args:
        numbers (list): List of integers.

    Returns:
        list: Sorted list of prime numbers.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for idx, item in enumerate(numbers):
        if not isinstance(item, int):
            raise TypeError(f"All elements must be integers. Invalid element at index {idx}: {item}")

    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    """
    Main function to demonstrate filter_and_sort_primes usage.
    """
    test_cases = [
        [10, 3, 5, 8, 2, 11, 0, -7],
        [],
        [4, 6, 8, 10],
        [13, 17, 19, 23],
        [1, 1, 1, 1],
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            result = filter_and_sort_primes(case)
            print(f"Test case {i}: Input: {case}")
            print(f"           Primes: {result}\n")
        except Exception as e:
            print(f"Test case {i} raised an exception: {e}\n")


if __name__ == "__main__":
    main()
```