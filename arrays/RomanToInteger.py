# https://leetcode.com/problems/roman-to-integer/description/
# tags: string

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        out = m[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if m[s[i]] < m[s[i+1]]:
                out -= m[s[i]]
            else:
                out += m[s[i]]
        return out
