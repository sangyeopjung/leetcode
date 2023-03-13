# https://leetcode.com/problems/generate-parentheses/description/
# tags: backtracking

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        self.dfs(0, 0, n, [], out)
        return out
    
    def dfs(self, op, cl, n, path, out):
        if cl == n:
            out.append(''.join(path))
            return
        
        if op < n:
            path.append('(')
            self.dfs(op+1, cl, n, path, out)
            path.pop()
        
        if cl < op:
            path.append(')')
            self.dfs(op, cl+1, n, path, out)
            path.pop()