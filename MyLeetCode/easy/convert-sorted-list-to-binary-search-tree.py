# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        median = len(nums)//2
        root = TreeNode(nums[median])
        root.left = self.sortedArrayToBST(nums[:median])
        root.right = self.sortedArrayToBST(nums[median+1:])
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)
