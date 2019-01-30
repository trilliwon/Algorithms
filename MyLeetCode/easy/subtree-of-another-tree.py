class Solution:
    def isEqualTree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        """
        if s == None or t == None:
            return False
        
        if s.val != t.val:
            return False

        que = []
        que.append((s, t))
        
        while len(que) != 0:
            sNode, tNode =  que.pop(0)
            if sNode.val == tNode.val:
                if sNode.left != None and tNode.left != None:
                    que.append((sNode.left, tNode.left))
                else:
                    if not (sNode.left == None and tNode.left == None):
                        return False
                if sNode.right != None and tNode.right != None:
                    que.append((sNode.right, tNode.right))
                else:
                    if not (sNode.right == None and tNode.right == None):
                        return False
            else:
                return False
            
        return True
        
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        stack = []
        stack.append(s)

        while len(stack) != 0:
            node = stack.pop()

            if node.val == t.val:
                if self.isEqualTree(node, t):
                    return True
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return False
