from collections import deque

class Solution():
    def snakesAndLadders(board):
        n = len(board)
        target = n * n
        
        def square_to_row_col(square):
            row = n - 1 - (square - 1) // n
            if (n - 1 - row) % 2 == 0:
                col = (square - 1) % n
            else:
                col = n - 1 - (square - 1) % n
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # Start at square 1 with 0 moves

        while queue:
            square, moves = queue.popleft()

            if square == target:
                return moves

            if square in visited:
                continue

            visited.add(square)

            for next_square in range(square + 1, min(square + 7, target + 1)):
                next_row, next_col = square_to_row_col(next_square)
                if board[next_row][next_col] != -1:
                    next_square = board[next_row][next_col]

                queue.append((next_square, moves + 1))

        return -1  # If we can't reach the last square