# https://leetcode.com/problems/longest-increasing-subsequence/description/
# tags: dp, binary search

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        out = [nums[0]]
        for i in range(1, len(nums)):
            if out[-1] < nums[i]:
                out.append(nums[i])
            elif out[-1] > nums[i]:
                l = 0
                r = len(out)
                while l < r:
                    m = l + (r-l)//2
                    if out[m] < nums[i]:
                        l = m + 1
                    else:
                        r = m
                out[l] = nums[i]
        return len(out)



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)