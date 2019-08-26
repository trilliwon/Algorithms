# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        
        result = [[]]
        q = collections.deque([])
        
        q.append((root, 0))
        
        # BFS
        while len(q) != 0:
            
            node, level = q.popleft()
            
            if len(result) - 1 == level:
                result[level].append(node.val)
            else:
                result.append([])
                result[level].append(node.val)
            
            if node.left:
                q.append((node.left, level+1))

            if node.right:
                q.append((node.right, level+1))

        return result[::-1]
