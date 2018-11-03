import queue

class Solution:
    
    def mergedNode(self, t1, t2):

        if t1 != None and t2 != None:
            return TreeNode(t1.val + t2.val)
        elif t1 != None and t2 == None:
            return TreeNode(t1.val)
        elif t2 != None and t1 == None:
            return TreeNode(t2.val)
        else:
            return None
        
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        que = queue.Queue()
        
        root = self.mergedNode(t1, t2)

        temp = root
        
        que.put((t1, t2, temp))
        
        while not que.empty():
            t1, t2, new = que.get()

            print(t1.val if t1 != None else 'None', t2.val if t2 != None else 'None')

            t1_left = None
            t1_right = None
            if t1 != None:
                t1_left = t1.left
                t1_right = t1.right

            t2_left = None
            t2_right = None
            if t2 != None:
                t2_left = t2.left
                t2_right = t2.right

            if not (t1_left == None and t2_left == None):
                new.left = self.mergedNode(t1_left, t2_left)
                que.put((t1_left, t2_left, new.left))

            if not (t1_right == None and t2_right == None):
                new.right = self.mergedNode(t1_right, t2_right)
                que.put((t1_right, t2_right, new.right))

        return root
        
        

            
