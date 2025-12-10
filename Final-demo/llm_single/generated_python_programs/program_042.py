def filter_greater_than_average(numbers):
    """
    Returns a list of elements from the input list that are greater than the average of all elements.

    :param numbers: List of integers
    :return: List of integers greater than the average; preserves the original order
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements in the input list must be integers.")
    if not numbers:
        return []

    average = sum(numbers) / len(numbers)
    return [num for num in numbers if num > average]


def main():
    # Example usage of filter_greater_than_average function
    example_lists = [
        [1, 2, 3, 4, 5],
        [10, 10, 10, 10],
        [-5, 0, 5, 10],
        [],
        [100]
    ]

    for idx, lst in enumerate(example_lists, start=1):
        try:
            result = filter_greater_than_average(lst)
            print(f"Example {idx}: Input: {lst} -> Output: {result}")
        except (TypeError, ValueError) as e:
            print(f"Example {idx}: Input: {lst} -> Error: {e}")


if __name__ == "__main__":
    main()