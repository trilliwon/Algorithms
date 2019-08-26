# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        count = collections.Counter()
        
        def inorder(root):
            if root == None:
                return
            count[root.val] += 1
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        
        m = max(count.values())

        return map(lambda x: x[0], filter(lambda x: x[1] == m, count.items()))
        
