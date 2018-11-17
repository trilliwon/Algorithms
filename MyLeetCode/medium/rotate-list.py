# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        """
        
        1->2->3->4->5->NULL
        5->1->2->3->4->NULL
        4->5->1->2->3->NULL
        
        """
        if head == None:
            return head
        
        node = head
        length = 0

        while node != None:
            length += 1
            node = node.next

        k = k % length
        
        newTail = head
        for _ in range(length - k - 1):
            newTail = newTail.next
            
        newHead = newTail.next
        newTail.next = None
        
        node = newHead
        if node == None:
            return head

        while node.next != None:
            node = node.next
        node.next = head
        
        return newHead
