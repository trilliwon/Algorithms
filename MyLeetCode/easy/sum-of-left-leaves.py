# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        Using DFS
        
        O(2^N)
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
    
        stack = []
        stack.append((None, root))
        
        ans = 0
        
        while stack:
            p, node = stack.pop()

            if node.left:
                stack.append((node, node.left))

            if node.right:
                stack.append((node, node.right))
                
            if node.left == None and node.right == None:
                if p != None and p.left == node:
                    ans += node.val
        return ans
            
        
