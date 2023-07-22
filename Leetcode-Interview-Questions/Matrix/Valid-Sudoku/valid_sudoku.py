def is_valid_sudoku(board):
    def is_valid_unit(unit):
        seen = set()
        for num in unit:
            if num != '.' and num in seen:
                return False
            seen.add(num)
        return True

    # Check rows
    for row in board:
        if not is_valid_unit(row):
            return False

    # Check columns
    for col in zip(*board):
        if not is_valid_unit(col):
            return False

    # Check 3x3 sub-boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(sub_box):
                return False

    return True
