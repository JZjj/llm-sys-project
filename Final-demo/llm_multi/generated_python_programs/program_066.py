```python
def generate_spiral_matrix(n: int) -> list[list[int]]:
    """
    Generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

    Args:
        n (int): Size of the matrix (n > 0)

    Returns:
        list[list[int]]: n x n spiral matrix
    """
    matrix = [[0] * n for _ in range(n)]

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    current_num = 1

    while left <= right and top <= bottom:
        # Traverse from left to right along the top row
        for col in range(left, right + 1):
            matrix[top][col] = current_num
            current_num += 1
        top += 1

        # Traverse from top to bottom along the right column
        for row in range(top, bottom + 1):
            matrix[row][right] = current_num
            current_num += 1
        right -= 1

        if top <= bottom:
            # Traverse from right to left along the bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = current_num
                current_num += 1
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top along the left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = current_num
                current_num += 1
            left += 1

    return matrix


def main():
    # Example usage and demonstration
    test_values = [1, 2, 3, 4, 5]

    for n in test_values:
        print(f"Spiral matrix for n = {n}:")
        matrix = generate_spiral_matrix(n)
        for row in matrix:
            print(row)
        print()


if __name__ == "__main__":
    main()
```