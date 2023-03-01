# https://leetcode.com/problems/3sum-closest/description/
# tags: two pointers

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        L = len(nums)
        nums.sort()

        out = float('inf')
        i = 0
        for i in range(L-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, L-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target

                if abs(s - target) < abs(out - target):
                    out = s

                if s < target:
                    j += 1
                else:
                    k -= 1
        
        return out