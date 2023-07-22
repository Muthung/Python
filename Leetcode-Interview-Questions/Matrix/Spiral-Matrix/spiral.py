def spiral_order(matrix):
    result = []
    while matrix:
        # Move along the first row from left to right
        result += matrix.pop(0)

        # Move along the last column from top to bottom
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # Move along the last row from right to left
        if matrix:
            result += matrix.pop()[::-1]

        # Move along the first column from bottom to top
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result
