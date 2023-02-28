# https://leetcode.com/problems/number-of-islands/description/
# tags: dfs, matrix

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.propagate(grid, i, j)
                    out += 1
        return out
    
    def propagate(self, grid, i, j):
        if grid[i][j] == "0":
            return

        grid[i][j] = "0"
        if i > 0:
            self.propagate(grid, i-1, j)
        if j > 0:
            self.propagate(grid, i, j-1)
        if i < len(grid)-1:
            self.propagate(grid, i+1, j)
        if j < len(grid[0])-1:
            self.propagate(grid, i, j+1)