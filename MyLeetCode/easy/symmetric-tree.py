# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        leftStack = []
        rightStack = []

        self.addLeftToStack(leftStack, root)
        self.addRightToStack(rightStack, root)
        
        while leftStack and rightStack:

            if len(leftStack) != len(rightStack):
                return False

            left = leftStack.pop()
            right = rightStack.pop()

            if left.val != right.val:
                return False
            else:
                if left.right:
                    self.addLeftToStack(leftStack, left.right)

                if right.left:
                    self.addRightToStack(rightStack, right.left)
        return True

    def addLeftToStack(self, leftStack, node):
        while node != None:
            leftStack.append(node)
            node = node.left
            
    def addRightToStack(self, rightStack, node):
        while node != None:
            rightStack.append(node)
            node = node.right
