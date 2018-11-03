# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        
        leafValues = []
        
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            if root.left == None and root.right == None:
                leafValues.append(root.val)
            inorder(root.right)
        
        
        inorder(root1)
        leafValues1 = [x for x in leafValues]
        leafValues = []
        inorder(root2)
        return leafValues1 == leafValues
