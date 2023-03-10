# https://leetcode.com/problems/find-the-duplicate-number/description/
# tags: two pointers

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        fast = nums[0]
        slow = nums[slow]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow