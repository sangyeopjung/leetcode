# https://leetcode.com/problems/spiral-matrix/description/
# tags: matrix, simulation

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        steps = [len(matrix[0]), len(matrix)-1]

        dir = 0
        next = [0,1,0,-1,0]

        i, j = 0, -1
        while steps[dir%2]:
            for _ in range(steps[dir%2]):
                i += next[dir]
                j += next[dir+1]
                out.append(matrix[i][j])
            steps[dir%2] -= 1
            dir = (dir + 1) % 4
        return out



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        dir = 0
        next = [0,1,0,-1,0]

        out = []

        # these indicate the rows/cols being explored
        min_x, max_x = 0, m
        min_y, max_y = -1, n

        # current location
        i = j = 0
        for _ in range(m*n):
            out.append(matrix[i][j])

            x, y = i + next[dir], j + next[dir+1]
            if x == i and y == max_y: # top right corner
                dir = (dir + 1) % 4
                max_y -= 1
            elif x == max_x and y == j: # bottom right corner
                dir = (dir + 1) % 4
                max_x -= 1
            elif x == i and y == min_y: # bottom left corner
                dir = (dir + 1) % 4
                min_y += 1
            elif x == min_x and y == j: # top left corner
                dir = (dir + 1) % 4
                min_x += 1

            i += next[dir]
            j += next[dir+1]
        
        return out