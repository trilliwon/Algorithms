cass Solution:
    def wordPelf.left = None
    #         self.right = None
    
    class Solution:
        
            def rightMost(self, node):
                    if node.right == None:
                                return node
                                        return self.rightMost(node.right)
                                        
                                            def leftMost(self, node):
                                                    if node.left == None:
                                                                return node
                                                                        return self.leftMost(node.left)
                                                                                    
                                                                                            
                                                                                                
                                                                                                    def minDiffInBST(self, root):
                                                                                                            """
                                                                                                                    :type root: TreeNode
                                                                                                                            :rtype: int
                                                                                                                                    """
                                                                                                                                            
                                                                                                                                                    ans = 100
                                                                                                                                                            
                                                                                                                                                                    stack = []
                                                                                                                                                                            stack.append(root)
                                                                                                                                                                                    
                                                                                                                                                                                            while len(stack) != 0:
                                                                                                                                                                                                        root = stack.pop()
                                                                                                                                                                                                        
                                                                                                                                                                                                                    if root.left != None:
                                                                                                                                                                                                                                    ans = min(ans, abs(root.val - self.rightMost(root.left).val))
                                                                                                                                                                                                                                                    stack.append(root.left)
                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                if root.right != None:
                                                                                                                                                                                                                                                                                ans = min(ans, abs(root.val - self.leftMost(root.right).val))
                                                                                                                                                                                                                                                                                                stack.append(root.right)
                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                        return ansttern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        t = str.split()
        s = pattern
        
        # s
        comp = {}
        counter = 0
        ss = []
        
        for c in s:
            if not (c in comp):
                comp[c] = counter
                counter += 1
            ss.append(comp[c])

        comp = {}
        counter = 0
        tt = []
        for c in t:
            if not (c in comp):
                comp[c] = counter
                counter += 1
            tt.append(comp[c])
        return ss == tt

