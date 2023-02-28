# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# tags: dfs, binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not node or node == p or node == q:
            return node
        
        left = self.lowestCommonAncestor(node.left, p, q)
        right = self.lowestCommonAncestor(node.right, p, q)
        if left and right:
            return node
        if left or right:
            return left or right
