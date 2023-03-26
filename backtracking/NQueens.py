# https://leetcode.com/problems/n-queens/description/
# tags: backtracking

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        col = set() # j
        # 0 1 2
        # 0 1 2
        # 0 1 2
        diag1 = set() # i-j
        # 0 -1 -2
        # 1  0 -1
        # 2  1  0
        diag2 = set() # i+j
        # 0  1  2
        # 1  2  3
        # 2  3  4
        matrix = [['.' for _ in range(n)] for _ in range(n)]
        self.placeQueen(0, matrix, col, diag1, diag2, out)
        return out
    
    def placeQueen(self, i, matrix, col, diag1, diag2, out):
        n = len(matrix)
        if i == n:
            out.append([''.join(row) for row in matrix])
            return

        for j in range(n):
            if j not in col and i-j not in diag1 and i+j not in diag2:
                col.add(j)
                diag1.add(i-j)
                diag2.add(i+j)
                matrix[i][j] = 'Q'
                self.placeQueen(i+1, matrix, col, diag1, diag2, out)
                col.remove(j)
                diag1.remove(i-j)
                diag2.remove(i+j)
                matrix[i][j] = '.'
