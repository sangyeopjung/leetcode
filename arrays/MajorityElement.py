# https://leetcode.com/problems/majority-element/description/
# tags: counting

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        out = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                count = 1
                out = nums[i]
            elif out == nums[i]:
                count += 1
            else:
                count -= 1
            
        return out