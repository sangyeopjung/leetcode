# https://leetcode.com/problems/subsets/description/
# tags: backgracking, dfs

class Solution:
    def subsets(self, nums):
        out = []
        self.dfs(nums, 0, [], out)
        return out

    def dfs(self, nums, i, path, out):
        out.append(path.copy())
        for j in range(i, len(nums)):
            path.append(nums[j])
            self.dfs(nums, j+1, path, out)
            path.pop()


class Solution:
    def subsets(self, nums):
        out = [[]]
        for n in nums:
            out += [arr + [n] for arr in out]
        return out
