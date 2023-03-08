# https://leetcode.com/problems/counting-bits/description/
# tags: bit manipulation

class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            out[i] = out[i >> 1] + (i & 1)        
        return out
