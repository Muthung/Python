def game_of_life(board):
    def count_live_neighbors(x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                    count += board[x + i][y + j]
        return count

    m, n = len(board), len(board[0])
    next_state = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            live_neighbors = count_live_neighbors(i, j)

            if board[i][j] == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    next_state[i][j] = 0  # Dies due to under-population or over-population
                else:
                    next_state[i][j] = 1  # Lives on to the next generation
            else:  # Dead cell
                if live_neighbors == 3:
                    next_state[i][j] = 1  # Becomes a live cell due to reproduction

    for i in range(m):
        for j in range(n):
            board[i][j] = next_state[i][j]
