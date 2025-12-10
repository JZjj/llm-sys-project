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
    Filter prime numbers from the list and return them sorted.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A sorted list of prime numbers from the input list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    
    # Validate each element is an integer
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the input list must be integers.")
    
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    """
    Main function to demonstrate the filter_and_sort_primes function.
    """
    example_lists = [
        [3, 4, 5, 6, 7, 8, 9, 10],
        [15, 21, 22, 24],
        [],
        [2, 3, 5, 7, 11, 13],
        [0, 1, -3, 17, 19, 23],
    ]

    for idx, numbers in enumerate(example_lists, 1):
        try:
            result = filter_and_sort_primes(numbers)
            print(f"Example {idx}: Input: {numbers}\n"
                  f"          Prime numbers sorted: {result}\n")
        except (TypeError, ValueError) as e:
            print(f"Example {idx}: Input: {numbers}\n"
                  f"          Error: {e}\n")


if __name__ == "__main__":
    main()