# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# tags: bfs, binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = [] # even: left -> right, odd: left <- right
        if not root:
            return out
        
        stack = [root]
        while stack:
            children = []
            curr = []
            for _ in range(len(stack)):
                node = stack.pop()
                curr.append(node.val)
                if len(out) & 1: # left <- right
                    if node.right:
                        children.append(node.right)
                    if node.left:
                        children.append(node.left)
                else: # left -> right
                    if node.left:
                        children.append(node.left)
                    if node.right:
                        children.append(node.right)
            out.append(curr)
            stack = children
        
        return out