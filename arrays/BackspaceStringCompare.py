# https://leetcode.com/problems/backspace-string-compare/description/
# tags: string

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ignore1 = 0
        ignore2 = 0
        i = len(s)-1
        j = len(t)-1
        while i >= 0 or j >= 0:
            while i >= 0 and (s[i] == '#' or ignore1 > 0):
                if s[i] == '#':
                    ignore1 += 1
                else:
                    ignore1 -= 1
                i -= 1
            
            while j >= 0 and (t[j] == '#' or ignore2 > 0):
                if t[j] == '#':
                    ignore2 += 1
                else:
                    ignore2 -= 1
                j -= 1
            
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            if i >= 0 and j < 0 or i < 0 and j >= 0:
                return False

            i -= 1
            j -= 1
        
        return True