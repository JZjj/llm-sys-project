```python
def spiral_traversal(matrix):
    result = []
    if not matrix or not matrix[0]:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while left <= right and top <= bottom:
        # Traverse top row from left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse rightmost column from top to bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Traverse bottom row from right to left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Traverse leftmost column from bottom to top
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


if __name__ == "__main__":
    # Test example
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(spiral_traversal(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```