# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        que = [(0, root)]
        levels = {}
        while len(que) != 0:
            level, node = que.pop(0)
            
            if level in levels:
                levels[level].append(node.val)
            else:
                levels[level] = [node.val]
            
            if node.left:
                que.append((level+1, node.left))
            if node.right:
                que.append((level+1, node.right))
        
        return [sum(levels[key])/len(levels[key]) for key in levels.keys()]
            
