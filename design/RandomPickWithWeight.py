# https://leetcode.com/problems/random-pick-with-weight/description/
# tags: design, binary search, random pick, prefix sum

class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.weights = [0 for _ in range(len(w))]
        for i in range(len(w)):
            self.total += w[i]
            self.weights[i] = self.total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        l, r = 0, len(self.weights)
        while l < r:
            m = l + (r-l)//2
            if self.weights[m] < target:
                l = m+1
            else:
                r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
