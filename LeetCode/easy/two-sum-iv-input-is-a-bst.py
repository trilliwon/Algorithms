class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        """
        if k > root.val then scan all 
        if k < root.val then scan left
        """
        
        if root == None:
            return False
        stack = [root]
        
        comp = {}
        ans = False

        while len(stack) != 0:
            node = stack.pop(0)
            if k - node.val in comp:
                ans = True
            comp[node.val] = True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        print(comp, ans)

        return ans
