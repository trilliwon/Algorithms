# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
            return None
        
        stack = [root]
        visited = set()
        acc = 0

        while len(stack) != 0:
            top = stack[-1]
            if top.right and not top.right.val in visited:
                stack.append(top.right)
            else:
                node = stack.pop()
                acc += node.val
                node.val = acc
                visited.add(node.val)

                if node.left:
                    stack.append(node.left)
        return root
    
    """
    def convertBST(self, root):
        originalKeys = []
        def inorderTravToAppend(root):
            if root == None:
                return
            originalKeys.append(root.val)
            inorderTravToAppend(root.left)
            inorderTravToAppend(root.right)
        inorderTravToAppend(root)

        originalKeys = sorted(originalKeys)
        originalKeys = { originalKeys[index] : sum(originalKeys[index:]) for index in range(0, len(originalKeys))}

        def inorderTravToUpdate(root):
            if root == None:
                return
            root.val = originalKeys[root.val]
            inorderTravToUpdate(root.left)
            inorderTravToUpdate(root.right)
        inorderTravToUpdate(root)
        
        return root
    """
        
