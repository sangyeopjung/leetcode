# https://leetcode.com/problems/permutations/description/
# tags: backtracking

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        self.helper(nums, out, [], 0)
        return out
    
    def helper(self, nums, out, depth):
        if len(nums) == depth:
            out.append(nums.copy())
            return
        
        for i in range(depth, len(nums)):
            nums[depth], nums[i] = nums[i], nums[depth]
            self.helper(nums, out, i+1)
            nums[depth], nums[i] = nums[i], nums[depth]
