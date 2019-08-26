# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        values = []
        def trav(root):
            if root == None:
                return
            trav(root.right)
            values.append(root.val)
            trav(root.left)

        trav(root)
        
        return min([abs(values[i-1] - values[i]) for i in range(1, len(values))])
