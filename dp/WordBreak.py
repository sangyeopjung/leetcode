# https://leetcode.com/problems/word-break/description/
# tags: dp, trie

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True
        
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)): # i = index of char
            if not dp[i]:
                continue
            
            j = i
            node = trie
            while j < len(s) and s[j] in node:
                node = node[s[j]]
                j += 1
                if '$' in node:
                    dp[j] = True
        
        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = possible until index i
        #       = dp[i - len(word)] if word in dict
        wordset = set(wordDict)
        lengths = set([len(word) for word in wordDict])
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for length in lengths:
                if length <= i and dp[i-length] and s[i-length:i] in wordset:
                    dp[i] = True
                    break
        return dp[len(s)]