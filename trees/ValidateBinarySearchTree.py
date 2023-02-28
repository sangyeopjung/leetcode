# https://leetcode.com/problems/validate-binary-search-tree/description/
# tags: bst, dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, minval, maxval):
        if not node:
            return True
        
        return minval < node.val < maxval \
            and self.helper(node.left, minval, node.val) \
            and self.helper(node.right, node.val, maxval)
