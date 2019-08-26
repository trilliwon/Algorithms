# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
    
        stack = []
        stack.append((str(root.val), root))
        paths = []
        while stack:
            path, node = stack.pop()
            
            if node.left:
                stack.append((path+'->'+str(node.left.val), node.left))

            if node.right:
                stack.append((path+'->'+str(node.right.val), node.right))
            
            if node.left == None and node.right == None:
                paths.append(path)
        return paths
