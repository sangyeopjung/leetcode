# https://leetcode.com/problems/binary-tree-right-side-view/description/
# tags: tree, bfs, dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if not root:
            return out

        q = [root]
        while q:
            out.append(q[-1].val)
            q = [child for node in q for child in (node.left, node.right) if child]

        return out


        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.dfs(root, 0, out)
        return out

    def dfs(self, node, depth, out):
        if not node:
            return
        
        if len(out) == depth:
            out.append(node.val)
        
        self.dfs(node.right, depth+1, out)
        self.dfs(node.left, depth+1, out)



class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if not root:
            return out

        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                if i == size-1: # rightmost element
                    out.append(node.val)
        
        return out

