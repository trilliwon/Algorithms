# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertNodeToBST(self, val, root):
        node = root
        while node != None:
            if val < node.val:
                if node.left != None:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return
            elif node.val < val:
                if node.right != None:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return
            else:
                return
                
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        
        for index in range(1, len(preorder)):
            val = preorder[index]
            self.insertNodeToBST(val, root)
        return root
