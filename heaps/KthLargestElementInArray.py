# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# tags: heap, quickselect

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)

        bigger = []
        same = []
        smaller = []
        for n in nums:
            if n < pivot:
                smaller.append(n)
            elif n > pivot:
                bigger.append(n)
            else:
                same.append(n)

        if k <= len(bigger):
            return self.findKthLargest(bigger, k)
        elif k > len(bigger) + len(same):
            return self.findKthLargest(smaller, k - len(bigger) - len(same))
        else:
            return same[0]
