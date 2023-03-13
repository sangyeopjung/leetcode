# https://leetcode.com/problems/longest-common-prefix/description/
# tags: string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # for each letter in str0
            for j in range(len(strs)): # for each string
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]