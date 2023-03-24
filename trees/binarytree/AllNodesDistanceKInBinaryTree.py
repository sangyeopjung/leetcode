# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# tags: bfs, binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        self.dfs(root, target, parents)

        queue = deque([target])
        visited = set()
        for i in range(k):
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                visited.add(node)
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                if node.val in parents and parents[node.val] not in visited:
                    queue.append(parents[node.val])

        return [n.val for n in queue]

    def dfs(self, node, target, parents):
        if node.left:
            parents[node.left.val] = node
            self.dfs(node.left, target, parents)
        if node.right:
            parents[node.right.val] = node
            self.dfs(node.right, target, parents)
