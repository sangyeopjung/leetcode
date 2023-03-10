# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# tags: bfs, matrix

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        neighbours = [(0,1), (1,0), (0,-1), (-1,0)]

        def bfs(queue, visited):
            while queue:
                i, j = queue.popleft()
                if visited[i][j]:
                    continue

                visited[i][j] = True
                for dx, dy in neighbours:
                    x, y = i+dx, j+dy
                    if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y] and heights[i][j] <= heights[x][y]:
                        queue.append((x,y))

        queue_p = deque([(0, j) for j in range(n)] + [(i, 0) for i in range(m)])
        visited_p = [[False for _ in range(n)] for _ in range(m)]
        bfs(queue_p, visited_p)

        queue_a = deque([(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)])
        visited_a = [[False for _ in range(n)] for _ in range(m)]
        bfs(queue_a, visited_a)

        out = []
        for i in range(m):
            for j in range(n):
                if visited_p[i][j] and visited_a[i][j]:
                    out.append([i,j])
        return out
