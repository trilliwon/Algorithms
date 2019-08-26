"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        que = [(1, root)]
        levels = {}
        while len(que) != 0:
            level, node = que.pop(0)
            
            if level in levels:
                levels[level].append(node.val)
            else:
                levels[level] = [node.val]

            for child in node.children:
                que.append((level+1, child))

        return max(levels.keys())
        
