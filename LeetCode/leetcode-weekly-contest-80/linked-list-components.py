# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        
        bits = []
        G = { x:x for x in G }
        while head:
            if head.val in G:
                bits.append(1)
            else:
                bits.append(0)
            head = head.next
        
        counter = 0
        flag = True
        for bit in bits:

            if flag and bit == 1:
                counter += 1

            if bit == 1:
                flag = False
            else:
                flag = True
            
        return counter
            
