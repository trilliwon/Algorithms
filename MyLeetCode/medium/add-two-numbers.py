# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = None
        node = None
        r = 0
        while l1 != None or l2 != None:
            left = 0 if l1 == None else l1.val
            right = 0 if l2 == None else l2.val
            r = left + right + r
            newNode = ListNode(r % 10)
            r = r // 10
            if s == None:
                s = newNode
                node = s
            else:
                node.next = newNode
                node = node.next
            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next
        
        if r > 0:
            node.next = ListNode(r)
        return s
            
