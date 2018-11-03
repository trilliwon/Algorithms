# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def depth(self, root):
        if not root:
            return 0
        stack = []
        stack.append((root, 1))

        depthlist = []
        
        while stack:
            curr, depth = stack.pop()

            if curr.right != None:
                stack.append((curr.right, depth + 1))

            if curr.left != None:
                stack.append((curr.left, depth + 1))

            if curr.right == None and curr.left == None:
                depthlist.append(depth)

        return max(depthlist)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        if root.left != None and root.right == None:
            return abs(self.depth(root.left) - 0) <= 1

        elif root.right != None and root.left == None:
            return abs(self.depth(root.right) - 0) <= 1
        
        if root.left != None and root.right != None:
            if abs(self.depth(root.left) - self.depth(root.right)) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return True

        
            
