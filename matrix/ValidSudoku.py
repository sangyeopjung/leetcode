# https://leetcode.com/problems/valid-sudoku/
# tags: matrix

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue

                if v in cols[i] or v in rows[j] or v in grids[i//3 * 3 + j//3]:
                    return False
                
                cols[i].add(v)
                rows[j].add(v)
                grids[i//3 * 3 + j//3].add(v)
        
        return True
