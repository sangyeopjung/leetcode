# https://leetcode.com/problems/number-of-1-bits/
# tags: bit manipulation

class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n > 0:
            out += n & 1
            n = n >> 1
        return out