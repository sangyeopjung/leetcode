# https://leetcode.com/problems/sudoku-solver/description/
# tags: matrix, backtracking

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False for _ in range(10)] for _ in range(9)]
        cols = [[False for _ in range(10)] for _ in range(9)]
        grids = [[False for _ in range(10)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j])
                    rows[i][n] = True
                    cols[j][n] = True
                    grids[3*(i//3) + j//3][n] = True
        self.solver(board, rows, cols, grids, 0, 0)

    def solver(self, board, rows, cols, grids, i, j):
        if i == 9:
            return True
        if j == 9:
            return self.solver(board, rows, cols, grids, i+1, 0)
        if board[i][j] != '.':
            return self.solver(board, rows, cols, grids, i, j+1)
        
        for n in range(1, 10):
            if not rows[i][n] and not cols[j][n] and not grids[3*(i//3) + j//3][n]:
                rows[i][n] = True
                cols[j][n] = True
                grids[3*(i//3) + j//3][n] = True
                board[i][j] = str(n)
                if self.solver(board, rows, cols, grids, i, j+1):
                    return True
                rows[i][n] = False
                cols[j][n] = False
                grids[3*(i//3) + j//3][n] = False
        board[i][j] = '.'
        return False
