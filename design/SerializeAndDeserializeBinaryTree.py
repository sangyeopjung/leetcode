# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# tags: design, tree, bfs

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        out = []
        queue = deque([root])
        while len(queue):
            node = queue.popleft()
            if node:
                out.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                out.append("#")
        
        return ','.join(out)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not len(data):
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))

        i = 1
        uppers = deque([root])
        while i < len(nodes):
            upper = uppers.popleft()
            if nodes[i] != "#":
                upper.left = TreeNode(int(nodes[i]))
                uppers.append(upper.left)
            
            if nodes[i+1] != "#":
                upper.right = TreeNode(int(nodes[i+1]))
                uppers.append(upper.right)
            
            i += 2
        
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))