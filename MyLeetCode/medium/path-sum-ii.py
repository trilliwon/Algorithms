# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []

        stack = []
        stack.append(([root.val], root))
        paths = []
        
        while stack:
            path, node = stack.pop()
            
            if node.left:
                t_path = copy.deepcopy(path)
                t_path.append(node.left.val)
                stack.append((t_path, node.left))

            if node.right:
                t_path = copy.deepcopy(path)
                t_path.append(node.right.val)
                stack.append((t_path, node.right))
            
            if node.left == None and node.right == None:
                s = 0
                for x in path:
                    s += x
                if s == sum:
                    paths.append(path)
        
        
        return paths
