# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# tags: binary tree, dfs, divide and conquer


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        vtoi = {}
        for i, n in enumerate(inorder):
            vtoi[n] = i
        
        q = deque()
        for n in preorder:
            q.append(n)
        
        return self.helper(q, inorder, vtoi, 0, len(inorder)-1)
    
    def helper(self, preorder, inorder, vtoi, start, end):
        if start > end:
            return None
        
        if start == end:
            return TreeNode(preorder.popleft())
        
        node = TreeNode(preorder.popleft())
        loc = vtoi[node.val]
        node.left = self.helper(preorder, inorder, vtoi, start, loc-1)
        node.right = self.helper(preorder, inorder, vtoi, loc+1, end)
        return node


# O(n^2)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        loc = inorder.index(preorder[0])
        return TreeNode(preorder[0],
                        self.buildTree(preorder[1:loc+1], inorder[:loc]),
                        self.buildTree(preorder[loc+1:], inorder[loc+1:]))
