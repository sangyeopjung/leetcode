# https://leetcode.com/problems/group-anagrams/description/
# tags: hashmap

# O(n+k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            hashed = '#'.join(str(i) for i in count)
            if hashed in groups:
                groups[hashed].append(s)
            else:
                groups[hashed] = [s]
        
        return groups.values()

# O(nklogk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sort = tuple(sorted(s))
            if sort in groups:
                groups[sort].append(s)
            else:
                groups[sort] = [s]
        
        return groups.values()