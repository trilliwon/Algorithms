# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -1
        
        values = []
        
        def inorder(root):
            if root == None:
                return
            values.append(root.val)
            inorder(root.right)
            inorder(root.left)
        inorder(root)

        valuesSet = set(values)
        valuesSet.remove(min(valuesSet))

        if len(valuesSet) > 0:
            return min(valuesSet)
        return -1
        
