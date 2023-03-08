# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# tags: dfs, tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.out
    
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.out = max(self.out, 
                    node.val, 
                    left + node.val, 
                    node.val + right, 
                    left + node.val + right)
        return node.val + max(0, left, right)
        