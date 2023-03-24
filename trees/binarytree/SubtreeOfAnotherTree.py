# https://leetcode.com/problems/subtree-of-another-tree/description/
# tags: dfs, serialise string

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        a = []
        b = []
        self.serialise(root, a)
        self.serialise(subRoot, b)
        return ''.join(b) in ''.join(a)
    
    def serialise(self, node, out):
        if not node:
            out.append('#')
            return
        
        out.append('$')
        out.append(str(node.val))
        self.serialise(node.left, out)
        self.serialise(node.right, out)
