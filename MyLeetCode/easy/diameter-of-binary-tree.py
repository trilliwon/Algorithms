# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def depth(self, root):
        queue = [(root, 0)]
        depth = 0
        while len(queue) != 0:
            node, level = queue.pop(0)

            if node.left:
                queue.append((node.left, level+1))

            if node.right:
                queue.append((node.right, level+1))

            if node.left == None and node.right == None:
                depth = max(depth, level)

        return depth

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
          1
         / \
        2   3
       / \     
      4   5
      
      - find right child max depth
      - find left child max depth
      
      """
        if root == None:
            return 0
        
        
        ans = 0
        que = [root]

        while len(que) != 0:
            node = que.pop(0)
            right = 0
            left = 0
            if node.right:
                que.append(node.right)
                right = self.depth(node.right) + 1
            if node.left:
                que.append(node.left)
                left = self.depth(node.left) + 1
            ans = max(left + right, ans)
        return ans
