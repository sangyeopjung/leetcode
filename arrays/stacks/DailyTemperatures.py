# https://leetcode.com/problems/daily-temperatures/description/
# tags: stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                out[i] = stack[-1] - i
            stack.append(i)
        return out
