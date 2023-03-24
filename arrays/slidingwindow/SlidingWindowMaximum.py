# https://leetcode.com/problems/sliding-window-maximum/description/
# tags: queue, sliding window

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        queue = deque()
        for i in range(len(nums)):
            if queue and i - queue[0] >= k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                out.append(nums[queue[0]])
        return out
