def remove_duplicates_preserve_order(int_list):
    """
    Remove duplicates from the list while preserving the original order.

    Parameters:
        int_list (list): A list of integers.

    Returns:
        list: A new list with duplicates removed, preserving order.

    Raises:
        TypeError: If input is not a list or elements are not integers.
    """
    if not isinstance(int_list, list):
        raise TypeError("Input must be a list.")
    seen = set()
    result = []
    for item in int_list:
        if not isinstance(item, int):
            raise TypeError("All elements of the input list must be integers.")
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main():
    # Example usage of remove_duplicates_preserve_order
    try:
        example_list = [3, 5, 3, 7, 9, 5, 7, 1]
        print("Original list:", example_list)
        no_duplicates = remove_duplicates_preserve_order(example_list)
        print("List after duplicates removed:", no_duplicates)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()