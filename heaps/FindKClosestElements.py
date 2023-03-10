# https://leetcode.com/problems/find-k-closest-elements/description/
# tags: binary search

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k
        while l < r:
            m = l + (r-l)//2
            if arr[m] - x < x - arr[m+k]:
                l = m+1
            else:
                r = m
        
        return arr[l:l+k]



class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        
        if arr[-1] <= x:
            return arr[-k:]

        l = 0
        r = len(arr)
        while l < r:
            m = l + (r-l)//2
            if arr[m] < x:
                l = m+1
            else:
                r = m
        
        r = l
        l = l-1
        for i in range(k):
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            else:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    l -= 1
                else:
                    r += 1

        return arr[l+1:r]