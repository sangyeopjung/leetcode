# https://leetcode.com/problems/partition-equal-subset-sum/description/
# tags: dp

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ & 1:
            return False
        half_sum = summ // 2

        dp = [False for _ in range(half_sum + 1)]
        dp[0] = True # base case
        for n in nums:
            if dp[half_sum]:
                return True

            for i in range(half_sum, n-1, -1):
                dp[i] |= dp[i-n]

        return dp[half_sum]
