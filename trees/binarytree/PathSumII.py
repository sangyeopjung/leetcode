# https://leetcode.com/problems/path-sum-ii/description/
# tags: dfs, tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []
        self.dfs(root, targetSum, [], out)
        return out
    
    def dfs(self, node, target, path, out):
        if not node:
            return

        path.append(node.val)
        if not node.left and not node.right:
            if target == node.val:
                out.append(path.copy())
        else:
            self.dfs(node.left, target - node.val, path, out)
            self.dfs(node.right, target - node.val, path, out)
        path.pop()