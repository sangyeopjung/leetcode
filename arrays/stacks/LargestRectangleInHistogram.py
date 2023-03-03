# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# tags: stack, prefix sum

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # bounds control
        stack = [] # index of bars smaller than current
        out = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]: # pop if you find same/decreasing
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                out = max(out, height * width)
            stack.append(i)
        
        return out


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        L = len(heights)

        left = [-1 for _ in range(L)] # first smaller element index to the left
        right = [L for _ in range(L)] # first smaller element index to the right

        for i in range(1, L):
            j = i-1
            while j >= 0 and heights[j] >= heights[i]:
                j = left[j]
            left[i] = j

        for i in range(L-2, -1, -1):
            k = i+1
            while k < L and heights[k] >= heights[i]:
                k = right[k]
            right[i] = k
        
        out = 0
        for i in range(L):
            out = max(out, heights[i] * (right[i]-left[i]-1))
        return out
