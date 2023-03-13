# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
# tags: matrix, dfs

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        out = 0
        visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                out = max(out, self.dfs(matrix, visited, i, j))
        return out
    
    def dfs(self, matrix, visited, i, j):
        if visited[i][j] == 0:
            visited[i][j] = 1
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                x, y = i+dx, j+dy
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    visited[i][j] = max(visited[i][j], 1 + self.dfs(matrix, visited, x, y))

        return visited[i][j]
