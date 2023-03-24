# https://leetcode.com/problems/missing-number/description/
# tags: array

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
