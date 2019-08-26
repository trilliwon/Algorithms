# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        node = root
        while node != None:
            if node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left
            else:
                return node
        return node
