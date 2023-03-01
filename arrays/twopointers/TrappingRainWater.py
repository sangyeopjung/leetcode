# https://leetcode.com/problems/trapping-rain-water/description/
# tags: two pointers, dp

class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = height[0]
        maxright = height[len(height)-1]
        l = 1
        r = len(height)-2

        out = 0
        while l <= r:
            if maxleft < maxright:
                if maxleft <= height[l]:
                    maxleft = height[l]
                else:
                    out += maxleft - height[l]
                l += 1
            else:
                if maxright <= height[r]:
                    maxright = height[r]
                else:
                    out += maxright - height[r]
                r -= 1

        return out
