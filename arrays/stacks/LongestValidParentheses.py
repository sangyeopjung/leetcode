# https://leetcode.com/problems/longest-valid-parentheses/description/
# tags: stack, dp, brackets

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = out = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                if left == right:
                    out = max(out, 2*left)
                elif left < right:
                    left = right = 0
            
        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
                if left == right:
                    out = max(out, 2*left)
                elif left > right:
                    left = right = 0
            else:
                right += 1
        
        return out



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        out = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    out = max(out, i - stack[-1])
                else:
                    stack.append(i)

        return out



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        out = 0
        if len(s) < 2:
            return out

        # dp[i] = longest string ending at index i
        # dp[i] = 0 if c=='(', else:
        #       = dp[i-2] + 2 if dp[i-1]=='('
        #         + dp[i - dp[i-1] - 1] + 2 if dp[i-1] == ')'
        dp = [0 for _ in range(len(s))]
        if s[0] == '(' and s[1] == ')':
            dp[1] = 2
            out = 2

        for i in range(2, len(s)):
            if s[i] == ')': # .........)
                if s[i-1] == '(': # .........()
                    dp[i] = dp[i-2] + 2

                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(': # .......))
                    dp[i] = dp[i-1] + 2
                    if i - dp[i-1] - 2 >= 0: # ..(.....))
                        dp[i] += dp[i - dp[i-1] - 2]

                out = max(out, dp[i])
        
        return out
