# https://leetcode.com/problems/house-robber/description/
# tags: dp

class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = most money until ith house
        two, one = 0, nums[0]
        for i in range(1, len(nums)):
            curr = max(two + nums[i], one)
            two = one
            one = curr
        return one