# https://leetcode.com/problems/decode-ways/description/
# tags: dp, string

class Solution:
    def numDecodings(self, s: str) -> int:
        two = 1
        one = 0 if s[len(s)-1] == '0' else 1
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = one
                if s[i] == '1' or s[i] == '2' and s[i+1] <= '6':
                    curr += two
            two = one
            one = curr
        return one



class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[len(s)] = 1
        dp[len(s)-1] = 0 if s[len(s)-1] == '0' else 1

        for i in range(len(s)-2, -1, -1):
            if '1' <= s[i] <= '9':
                dp[i] += dp[i+1]
            if s[i] == '1' or s[i] == '2' and s[i+1] <= '6':
                dp[i] += dp[i+2]
        
        return dp[0]



class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [None for _ in range(len(s))]
        return self.read(s, 0, memo)

    def read(self, s, i, memo):
        if i == len(s):
            return 1
        
        if not memo[i]:
            if s[i] == '0':
                memo[i] = 0
            else:
                # case 1: read 1
                memo[i] = self.read(s, i+1, memo)
                
                # case 2: read 2
                if i < len(s)-1 and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
                    memo[i] += self.read(s, i+2, memo)
        
        return memo[i]
