# https://leetcode.com/problems/word-search/description/
# tags: dfs, matrix, backtracking

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 1):
                    return True
        return False
    
    def dfs(self, board, word, i, j, depth):
        if depth == len(word):
            return True
        
        c = board[i][j]
        board[i][j] = '#'
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            x, y = i+dx, j+dy
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == word[depth]:
                if self.dfs(board, word, x, y, depth+1):
                    return True
        board[i][j] = c
        return False
