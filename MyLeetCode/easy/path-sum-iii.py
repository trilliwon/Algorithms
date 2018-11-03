import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self, root, sum):
        stack = []
        stack.append((root, root.val))
        
        numOfPath = 0
        
        while stack:
            node, s = stack.pop()
            
            if s == sum:
                numOfPath += 1
            if node.right != None:
                stack.append((node.right, node.right.val + s))
            if node.left != None:
                stack.append((node.left, node.left.val + s))
        return numOfPath
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        if root == None:
            return 0

        ans = 0
        
        que = queue.Queue()
        que.put(root)
        
        while not que.empty():
            node = que.get()
            
            ans += self.dfs(node, sum)
            
            if node.right != None:
                que.put(node.right)
            if node.left != None:
                que.put(node.left)

        return ans
        
        
