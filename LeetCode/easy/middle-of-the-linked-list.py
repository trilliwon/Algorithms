# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        1, 2, 3, 4, 5, 6
        """
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        middle = head
        for _ in range(1, length//2 + 1):
            middle = middle.next
        return middle
