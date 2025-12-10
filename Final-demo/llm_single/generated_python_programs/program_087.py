def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Returns True if n is a prime number, False otherwise.
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
    Filter prime numbers from the input list and return them sorted in ascending order.
    Non-integers, negative numbers, and zero are excluded from the output.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    primes = []
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers.")
        if num > 0 and is_prime(num):
            primes.append(num)

    return sorted(primes)


def main():
    """
    Main function to demonstrate the filter_and_sort_primes function.
    """
    example_lists = [
        [10, 3, 5, 8, 23, 0, -7, 13],
        [-1, -3, 0, 1, 4, 6],
        [2, 2, 3, 3, 5, 5],
        [],
        [17, 19, 23, 29],
        [4, 6, 8, 9, 10]
    ]

    for idx, lst in enumerate(example_lists, start=1):
        try:
            primes = filter_and_sort_primes(lst)
            print(f"Example {idx}: Input: {lst} -> Primes: {primes}")
        except (TypeError, ValueError) as e:
            print(f"Example {idx}: Input: {lst} -> Error: {e}")


if __name__ == "__main__":
    main()