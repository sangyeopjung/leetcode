# https://leetcode.com/problems/maximum-product-subarray/description/
# tags: prefix sum

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out = nums[0]
        
        forwards = 1
        backwards = 1
        for i in range(len(nums)):
            forwards *= nums[i]
            backwards *= nums[len(nums)-1 -i]
            out = max(out, forwards, backwards)
            if forwards == 0:
                forwards = 1
            if backwards == 0:
                backwards = 1
        
        return out