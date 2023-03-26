# https://leetcode.com/problems/combination-sum-iv/description/
# tags: dp, dfs

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(target+1):
            for n in nums:
                if n <= i:
                    dp[i] += dp[i-n]
        return dp[target]
