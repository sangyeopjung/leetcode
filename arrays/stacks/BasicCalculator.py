# https://leetcode.com/problems/basic-calculator/description/
# tags: stack, recursion, string, calculator

class Solution:
    def calculate(self, s: str) -> int:
        return self.helper(s, 0)[0]

    def helper(self, s, i):
        out = 0
        sign = 1
        num = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                out += sign * num
                num = 0
                sign = 1
            elif c == "-":
                out += sign * num
                num = 0
                sign = -1
            elif c == '(':
                num, i = self.helper(s, i+1)
            elif c == ')':
                out += sign * num
                return out, i
            i += 1
        
        out += sign * num
        return out, i