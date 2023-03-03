# https://leetcode.com/problems/longest-palindromic-substring/description/
# tags: string, two pointers

class Solution:
    def longestPalindrome(self, s: str) -> str:
        curmaxlen = 0
        curmaxbegin = 0
        for i in range(len(s)): # O(n)
            # 2 cases: odd / even lengths
            for l, r, curlen in [(i-1, i+1, 1), (i, i+1, 0)]: # O(2)
                while l >= 0 and r < len(s) and s[l] == s[r]: # O(n)
                    curlen += 2
                    l -= 1
                    r += 1
                if curlen > curmaxlen:
                    curmaxlen = curlen
                    curmaxbegin = l+1
        
        return s[curmaxbegin : curmaxbegin+curmaxlen]