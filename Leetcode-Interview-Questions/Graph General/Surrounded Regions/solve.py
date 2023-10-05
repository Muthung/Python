def solve(board):
    if not board:
        return

    m, n = len(board), len(board[0])

    # Helper function to perform DFS and mark 'O's as visited
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = 'V'  # Mark 'O' as visited

        # Recursively check adjacent cells
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    # Mark 'O's on the border as visited
    for i in range(m):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][n - 1] == 'O':
            dfs(i, n - 1)
    for j in range(n):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[m - 1][j] == 'O':
            dfs(m - 1, j)

    # Flip 'O's to 'X' and restore 'V' to 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'V':
                board[i][j] = 'O'