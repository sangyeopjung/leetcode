# https://leetcode.com/problems/rotate-array/
# tags: array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        k %= L
        self.reverse(nums, 0, L)
        self.reverse(nums, 0, k)
        self.reverse(nums, k, L)
    
    def reverse(self, nums, l, r):
        r -= 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1