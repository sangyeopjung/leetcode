# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# tags: sliding window, hashmap

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        pmap = defaultdict(int)
        smap = defaultdict(int)
        for i in range(len(p)):
            pmap[p[i]] += 1
            smap[s[i]] += 1

        out = []
        for i in range(len(s) - len(p)): # O(n)
            if self.are_equal(smap, pmap): # O(26)
                out.append(i)
            smap[s[i]] -= 1
            smap[s[i + len(p)]] += 1

        if self.are_equal(smap, pmap):
            out.append(len(s) - len(p))

        return out

    def are_equal(self, smap, pmap):
        for k,v in pmap.items():
            if smap[k] != v:
                return False
        return True
