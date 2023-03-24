# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# tags: two pointers, sorting

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        out = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            if -nums[l] < nums[r]:
                out[i] = nums[r]*nums[r]
                r -= 1
            else:
                out[i] = nums[l]*nums[l]
                l += 1
        return out
