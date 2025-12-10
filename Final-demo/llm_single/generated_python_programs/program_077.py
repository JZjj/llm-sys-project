def is_prime(n: int) -> bool:
    """Check if the number is prime."""
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


def is_palindrome_number(n: int) -> bool:
    """Check if the digits of the number form a palindrome."""
    s = str(n)
    return s == s[::-1]


def filter_prime_palindromes(numbers):
    """
    Return a new list containing numbers that are prime and whose digits form a palindrome,
    sorted in ascending order.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    filtered = []
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError(f"List element {num} is not an integer.")
        if num > 0 and is_prime(num) and is_palindrome_number(num):
            filtered.append(num)

    return sorted(filtered)


def main():
    # Example usage
    example_list = [131, 23, 11, 22, 313, 7, 44, 101, 4, 6, 5, 909]
    try:
        result = filter_prime_palindromes(example_list)
        print("Prime palindromic numbers:", result)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()