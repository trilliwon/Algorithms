# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self, root):
        stack = []
        stack.append((root, 1))
        
        ans = sys.maxsize

        while stack:
            curr, depth = stack.pop()
            
            if curr.right != None:
                stack.append((curr.right, depth + 1))

            if curr.left != None:
                stack.append((curr.left, depth + 1))
                
            if curr.left == None and curr.right == None:
                ans = min(depth, ans)
        return ans
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.dfs(root)
        else:
            return 0
