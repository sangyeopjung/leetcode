# https://leetcode.com/problems/find-median-from-data-stream/description/
# tags: heap, design

class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap
        self.big = [] # minheap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            heappush(self.small, -heappushpop(self.big, num))
        else:
            heappush(self.big, -heappushpop(self.small, -num))

    def findMedian(self) -> float:
        if len(self.small) != len(self.big):
            return -self.small[0]
        else:
            return (-self.small[0] + self.big[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()