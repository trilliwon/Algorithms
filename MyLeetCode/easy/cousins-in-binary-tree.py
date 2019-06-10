# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        lookup = dict()     # tuple(parent value, depth)
        que = queue.Queue() # tuple(node, depth)
        que.put((root, 0))
        lookup[root.val] = (0, 0)

        while not que.empty():
            parent, depth = que.get()
            left = parent.left
            right = parent.right
            
            if left != None:
                lookup[left.val] = (parent.val, depth + 1)
                que.put((left, depth+1))

            if right != None:
                lookup[right.val] = (parent.val, depth + 1)
                que.put((right, depth+1))
        
        return lookup[x][0] != lookup[y][0] and lookup[x][1] == lookup[y][1]
