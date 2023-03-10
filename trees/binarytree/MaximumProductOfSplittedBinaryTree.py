# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/
# tags: dfs, tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        memo = []
        total = self.getSum(root, memo)
        return max([(total-val) * val for val in memo]) % (10**9+7)

    def getSum(self, node, memo):
        if not node:
            return 0
        
        out = node.val + self.getSum(node.left, memo) + self.getSum(node.right, memo)
        memo.append(out)
        return out
    