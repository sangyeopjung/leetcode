# https://leetcode.com/problems/longest-palindrome/description/
# tags: string, hashmap

class Solution:
    def longestPalindrome(self, s: str) -> int:
        out = 0
        chars = set()
        for c in s:
            if c in chars:
                out += 2
                chars.remove(c)
            else:
                chars.add(c)
        
        return out + (1 if len(chars) else 0)