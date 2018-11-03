# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        values = []
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)
        inorder(root)
        root = TreeNode(values[0])
        node = root
        for v in values[1:]:
            node.right = TreeNode(v)
            node = node.right
        return root    
