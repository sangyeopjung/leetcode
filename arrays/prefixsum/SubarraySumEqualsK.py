# https://leetcode.com/problems/subarray-sum-equals-k/description/
# tags: hash table, prefix sum

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out = 0
        freq = {0: 1} # subarray sum : occurrence
        cursum = 0
        for n in nums:
            cursum += n
            out += freq.get(cursum - k, 0)
            freq[cursum] = freq.get(cursum, 0) + 1
        return out