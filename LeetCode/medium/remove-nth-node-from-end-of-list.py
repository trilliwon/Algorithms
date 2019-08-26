# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        if head == None:
            return None
        node = head
        while node != None:
            node = node.next
            length += 1
        
        if length == 1:
            return None
        
        if length == n:
            return head.next
        else:
            node = head
            for _ in range(length - n - 1):
                node = node.next
            node.next = node.next.next
            return head
        
