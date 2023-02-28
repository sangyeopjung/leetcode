# https://leetcode.com/problems/search-in-rotated-sorted-array/
# tags: binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]: # pivot is on the right
                if nums[l] <= target < nums[m]: 
                    r = m-1
                else:
                    l = m+1
            else: # pivot is on the left
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        
        return -1
