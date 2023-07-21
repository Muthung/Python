def setZeroes(matrix):
    rows_to_zero = set()
    cols_to_zero = set()
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)

    for row in rows_to_zero:
        for j in range(n):
            matrix[row][j] = 0

    for col in cols_to_zero:
        for i in range(m):
            matrix[i][col] =0
