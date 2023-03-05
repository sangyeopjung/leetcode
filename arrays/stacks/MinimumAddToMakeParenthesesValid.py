# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
# tags: stack

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        out = 0
        opening = 0
        for c in s:
            if c == '(':
                opening += 1
            else:
                opening -= 1
                if opening == -1:
                    opening = 0
                    out += 1
        return out + opening
