```python
def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while left <= right and top <= bottom:
        # Left to Right
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # Top to Bottom
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            # Right to Left
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        if left <= right:
            # Bottom to Top
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    return matrix


def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python spiral_matrix.py <n>")
        return

    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Please provide a positive integer for n.")
        return

    result = generate_spiral_matrix(n)
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
```