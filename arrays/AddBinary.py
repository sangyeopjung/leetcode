# https://leetcode.com/problems/add-binary/description/
# tags: string

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = []
        i = len(a)-1
        j = len(b)-1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            s = carry + (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0)
            out.append('1' if s & 1 else '0')
            carry = 1 if s > 1 else 0

            i -= 1
            j -= 1
        
        out.reverse()
        return ''.join(out)