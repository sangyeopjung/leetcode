# https://leetcode.com/problems/first-missing-positive/description/
# tags: array, in place

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            while 0 < nums[i] and nums[i] <= l and nums[i] != nums[nums[i]-1]:
                tmp1 = nums[i]
                tmp2 = nums[nums[i]-1]
                nums[nums[i]-1] = tmp1
                nums[i] = tmp2
        
        for i in range(l):
            if i+1 != nums[i]:
                return i+1
        return l+1
