"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        ans = []
        
        def postorder(node):
            if node == None:
                return

            for child in node.children:
                postorder(child)
            ans.append(node.val)

        postorder(root)
        
        print(ans)
        return ans
        
