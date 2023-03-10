# https://leetcode.com/problems/decode-string/
# tags: string, recursion, parser

class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s, 0)[0]

    def helper(self, s, start):
        number = 0
        out = ""
        i = start
        while i < len(s):
            if s[i].isdigit():
                while s[i] != '[':
                    number *= 10
                    number += int(s[i])
                    i += 1
                sub, i = self.helper(s, i+1)
                out += number * sub
                number = 0
            elif s[i] == ']':
                return out, i
            else:
                out += s[i]
            i += 1
        
        return out, i