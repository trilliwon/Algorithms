"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        
        def preorder(node):
            if node == None:
                return
            ans.append(node.val)
            for child in node.children:
                preorder(child)
                        

        preorder(root)
        return ans
        
