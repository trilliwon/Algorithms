# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def copy(self, node) -> TreeNode:
        newTree = TreeNode(node.val)
        stack = [(node, newTree)]

        while len(stack) != 0:
            n, newN = stack.pop()
            if n.left != None:
                newN.left = TreeNode(n.left.val)
                stack.append((n.left, newN.left))
            if n.right != None:
                newN.right = TreeNode(n.right.val)
                stack.append((n.right, newN.right))            
        return newTree

    def createBSTs(self, n, bsts) -> List[TreeNode]:
        res = []

        for tree in bsts:

            copiedTree = self.copy(tree)
            newNode = TreeNode(n)
            newNode.left = copiedTree
            res.append(newNode)

            moveCount = 0
            while True:

                copiedTree = self.copy(tree)
                newNode = TreeNode(n)

                tempNode = copiedTree

                for move in range(moveCount):
                    tempNode = tempNode.right
                
                tRight = tempNode.right
                tempNode.right = newNode
                newNode.left = tRight

                res.append(copiedTree)
                moveCount += 1
                if newNode.left == None and newNode.right == None:
                    break
        return res
            
    def generateTrees(self, n: int) -> List[TreeNode]:

        bsts = [[], [TreeNode(1)]]

        for x in range(2, n+1):
            bst_with_node = self.createBSTs(x, bsts[x-1])
            bsts.append(bst_with_node)

        return bsts[n]
