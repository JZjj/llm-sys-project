```python
def is_prime(n: int) -> bool:
    """Check if a number is prime using an efficient method."""
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
    """Return a list of prime numbers from the input list, sorted ascending."""
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    input_str = input("Enter a list of integers separated by spaces: ").strip()
    if not input_str:
        print("No input provided. Result: []")
        return

    tokens = input_str.split()
    numbers = []
    for token in tokens:
        try:
            num = int(token)
        except ValueError:
            print(f"Invalid integer input: {token}")
            return
        numbers.append(num)

    primes = filter_and_sort_primes(numbers)
    print(primes)


if __name__ == "__main__":
    main()
```