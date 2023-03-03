# https://leetcode.com/problems/string-to-integer-atoi/description/
# tags: string

class Solution:
    def myAtoi(self, s: str) -> int:
        L = len(s)

        i = 0
        # 1. ignore trailing whitespace
        while i < L and s[i] == ' ':
            i += 1
        
        # edge case: empty string
        if i == L:
           return 0

        # 2. check for sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # 3. check for numbers
        INT_MAX = 2147483647
        out = 0
        while i < L and 0 <= ord(s[i]) - ord('0') <= 9:
            # check for overflow
            x = ord(s[i]) - ord('0')
            if out > (INT_MAX - x) // 10:
                return INT_MAX if sign == 1 else -INT_MAX-1
            out = 10 * out + x
            i += 1
        
        return sign * out