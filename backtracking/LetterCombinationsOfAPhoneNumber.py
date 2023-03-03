# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# tags: dfs, backtracking

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        out = []
        m = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        self.dfs(digits, [], m, out)
        return out

    def dfs(self, digits, path, m, out):
        if len(path) == len(digits):
            out.append(''.join(path))
            return
        
        for c in m[digits[len(path)]]:
            path.append(c)
            self.dfs(digits, path, m, out)
            path.pop()
            