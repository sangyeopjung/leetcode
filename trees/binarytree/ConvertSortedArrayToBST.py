# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# tags: array, bst, dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums, 0, len(nums))
    
    def dfs(self, nums, begin, end):
        if end - begin == 1:
            return TreeNode(nums[begin])
        
        if end - begin == 2:
            return TreeNode(nums[begin+1], TreeNode(nums[begin]))
        
        mid = begin + (end-begin)//2
        return TreeNode(nums[mid], self.dfs(nums, begin, mid), self.dfs(nums, mid+1, end))
