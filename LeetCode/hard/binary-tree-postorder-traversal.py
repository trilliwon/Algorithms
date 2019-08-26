# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        def postorder(node):
            if node == None:
                return
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

        postorder(root)
        return ans
