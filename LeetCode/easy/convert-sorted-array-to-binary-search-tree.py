# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def node(self, nums, start, end):
        median = (start+end)//2
        node = TreeNode(nums[median])

        if start == end:
            return node
        elif start < end:
            node.left = self.node(nums, start, median-1)
            node.right = self.node(nums, median+1, end)
        else:
            return None
        return node
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        root = self.node(nums, 0, len(nums)-1)
        return root
