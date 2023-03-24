# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# tags: binary search

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            # pivot on right
            if nums[0] <= nums[m]:
                l = m+1
            # pivot on left
            else:
                r = m
        
        return nums[l]
