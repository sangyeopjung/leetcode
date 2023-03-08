# https://leetcode.com/problems/longest-consecutive-sequence/description/
# tags: hashset, union find


class UF:
    def __init__(self, L):
        self.size = [1 for _ in range(L)]
        self.parent = [i for i in range(L)]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]

    def find(self, x):
        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UF(len(nums))
        val_to_index = {}

        for i in range(len(nums)):
            if nums[i] in val_to_index:
                continue
            val_to_index[nums[i]] = i

            if nums[i]-1 in val_to_index:
                uf.union(val_to_index[nums[i]-1], i)
            if nums[i]+1 in val_to_index:
                uf.union(val_to_index[nums[i]+1], i)

        return max(uf.size) if uf.size else 0


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = 0
        s = set(nums)
        for n in s:
            if n-1 not in s: # first number in a sequence
                i = n+1
                while i in nums:
                    i += 1 
                out = max(out, i-n)
        return out