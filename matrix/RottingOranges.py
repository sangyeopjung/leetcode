# https://leetcode.com/problems/rotting-oranges/description/
# tags: matrix, bfs

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        fresh_count = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        elapsed = 0
        while fresh_count and len(queue):
            elapsed += 1
            size = len(queue)
            for _ in range(size):
                i,j = queue.popleft()
                for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    x, y = i+dx, j+dy
                    if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] == 1:
                        fresh_count -= 1
                        queue.append((x,y))
                        grid[x][y] = 2
        
        return elapsed if fresh_count == 0 else -1