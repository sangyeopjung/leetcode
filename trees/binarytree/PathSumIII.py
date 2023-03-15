# https://leetcode.com/problems/path-sum-iii/description/
# tags: dfs, hashmap, binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.dfs(root, targetSum, 0, {})

    def dfs(self, node, target, path, memo):
        if not node:
            return 0
        
        path += node.val

        out = (1 if path == target else 0)
        out += memo.get(path - target, 0)

        memo[path] = memo.get(path, 0) + 1
        out += self.dfs(node.left, target, path, memo)
        out += self.dfs(node.right, target, path, memo)
        memo[path] -= 1

        return out


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        return self.dfs(root, targetSum) \
            + self.pathSum(root.left, targetSum) \
            + self.pathSum(root.right, targetSum)

    def dfs(self, node, target):
        if not node:
            return 0
        
        return (1 if node.val == target else 0) \
                + self.dfs(node.left, target - node.val) \
                + self.dfs(node.right, target - node.val)