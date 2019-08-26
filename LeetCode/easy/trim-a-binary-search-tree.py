# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        """
        [L, R]
        """
        if root == None:
            return None
        
        while root.val < L or root.val > R:
            if root.val < L:
                tRoot = root.right
                while tRoot != None and tRoot.val < L:
                    tRoot = tRoot.right
                root = tRoot

            if root == None:
                return None

            if R < root.val:
                tRoot = root.left
                while tRoot != None and tRoot.val > R:
                    tRoot = tRoot.left
                root = tRoot

            if root == None:
                return None

        stack = []
        stack.append(root)
        
        while len(stack) != 0:
            node = stack.pop()

            # left
            if node.left != None:
                if node.left.val < L:
                    tNode = node.left
                    while tNode != None and tNode.val < L:
                        tNode = tNode.right
                    node.left = tNode
                    if tNode != None:
                        stack.append(node.left)
                else:
                    stack.append(node.left)

            # right
            if node.right != None:
                if R < node.right.val:
                    tNode = node.right
                    while tNode != None and tNode.val > R:
                        tNode = tNode.left
                    node.right = tNode
                    if tNode != None:
                        stack.append(node.right)
                else:
                    stack.append(node.right)
        return root
                
                
                
