# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def rightMost(self, node):
        if node.right == None:
            return node
        return self.rightMost(node.right)

    def leftMost(self, node):
        if node.left == None:
            return node
        return self.leftMost(node.left)
            
        
    
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        ans = 100
        
        stack = []
        stack.append(root)
        
        while len(stack) != 0:
            root = stack.pop()

            if root.left != None:
                ans = min(ans, abs(root.val - self.rightMost(root.left).val))
                stack.append(root.left)

            if root.right != None:
                ans = min(ans, abs(root.val - self.leftMost(root.right).val))
                stack.append(root.right)

        return ans
