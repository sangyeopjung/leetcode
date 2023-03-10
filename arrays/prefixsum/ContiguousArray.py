# https://leetcode.com/problems/contiguous-array/description/
# tags: prefix sum

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        L = len(nums)
        m = {0: -1} # index of first occurrence of value

        out = 0
        val = 0
        for i in range(L):
            val += (1 if nums[i] else -1)
            if val in m:
                out = max(out, i - m[val])
            else:
                m[val] = i

        return out