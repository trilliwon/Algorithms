class Solution:
    
    def preorder(self, t, output):
        if t != None:
            output.append('(')
            output.append(str(t.val))
            if t.left == None and t.right != None:
                output.append('()')
            self.preorder(t.left, output)
            self.preorder(t.right, output)
            output.append(')')

    
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        """
        1(2(4))(3)
        1(2(4))(3)

                1
              /   \
             2     3
           /    
         4     
        """
        
        output = []
        self.preorder(t, output)
        ans = ''.join(output[1:-1])
        return ans

