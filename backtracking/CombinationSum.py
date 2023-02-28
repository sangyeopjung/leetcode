# https://leetcode.com/problems/combination-sum/description/
# tags: dfs, backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        self.dfs(candidates, 0, out, [], target)
        return out

    def dfs(self, candidates, i, out, path, target):
        if target < 0:
            return

        if target == 0:
            out.append(path.copy())
            return

        for j in range(i, len(candidates)):
            path.append(candidates[j])
            self.dfs(candidates, j, out, path, target-candidates[j])
            path.pop()
        
        return