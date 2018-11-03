# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ps_anc = set()
        LCA = None

        to_p = root
        to_q = root
        
        while (to_p != None):
            if to_p.val > p.val:
                ps_anc.add(to_p.val)
                to_p = to_p.left
            elif to_p.val < p.val:
                ps_anc.add(to_p.val)
                to_p = to_p.right
            else:
                ps_anc.add(to_p.val)
                break
        
        while (to_q != None):
            if to_q.val > q.val:
                if to_q.val in ps_anc:
                    LCA = to_q.val
                to_q = to_q.left
            elif to_q.val < q.val:
                if to_q.val in ps_anc:
                    LCA = to_q.val
                to_q = to_q.right
            elif to_q.val == q.val:
                if q.val in ps_anc:
                    LCA = q.val
                break
        return TreeNode(LCA)
