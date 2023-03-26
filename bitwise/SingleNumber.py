# https://leetcode.com/problems/single-number/
# tags: bit manupulation

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for n in nums:
            out = out ^ n
        return out
