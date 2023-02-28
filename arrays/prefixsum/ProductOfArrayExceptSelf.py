# https://leetcode.com/problems/product-of-array-except-self/
# tags: prefix sum

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)

        # out[i] = cumulative product [0,i)
        out = [1 for _ in range(L)]
        for i in range(1, L):
            out[i] = out[i-1] * nums[i-1]
        
        right = 1
        for i in range(L-1, -1, -1):
            out[i] *= right
            right *= nums[i]

        return out
