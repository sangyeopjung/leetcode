# https://leetcode.com/problems/3sum-closest/description/
# tags: two pointers

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        out, curmin = 0, float('inf')
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = abs(s - target)
                if diff < curmin:
                    out, curmin = s, diff
                
                if s == target:
                    return target
                elif s < target:
                    j += 1
                else:# s > target:
                    k -= 1
        return out
