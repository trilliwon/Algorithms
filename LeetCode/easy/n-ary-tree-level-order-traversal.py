"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
    
        nodeQueue = [(root, 0)]
    
        result = {}
        result[0] = [root.val]

        while len(nodeQueue) != 0:
            node, level = nodeQueue.pop(0)
            
            if level+1 in result:
                if len(node.children) != 0:
                    result[level+1] = result[level+1] + [child.val for child in node.children]
            else:
                if len(node.children) != 0:
                    result[level+1] = [child.val for child in node.children]
            
            for child in node.children:
                nodeQueue.append((child, level+1))

        return result.values()


