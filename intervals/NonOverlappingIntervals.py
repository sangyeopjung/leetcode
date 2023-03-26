# https://leetcode.com/problems/non-overlapping-intervals/description/
# tags: intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        out, currend = 0, float('-inf')
        for begin, end in sorted(intervals, key=lambda x: x[1]):
            if currend <= begin:
                currend = end
            else:
                out += 1
        return out
