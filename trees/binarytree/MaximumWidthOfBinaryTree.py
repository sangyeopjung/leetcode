# https://leetcode.com/problems/maximum-width-of-binary-tree/
# tags: bfs, tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        out = 1
        root.val = 0
        queue = deque([root])
        while len(queue):
            out = max(out, queue[-1].val - queue[0].val + 1)
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    node.left.val = node.val*2
                    queue.append(node.left)
                if node.right:
                    node.right.val = node.val*2+1
                    queue.append(node.right)
        return out