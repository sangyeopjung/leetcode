# https://leetcode.com/problems/search-a-2d-matrix/
# tags: matrix, binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l = 0
        r = m
        while l < r:
            mid = l + (r-l) // 2
            if matrix[mid][n-1] < target:
                l = mid + 1
            else:
                r = mid

        if l == m:
            return False

        row = l
        l = 0
        r = n
        while l < r:
            mid = l + (r-l) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return matrix[row][l] == target
