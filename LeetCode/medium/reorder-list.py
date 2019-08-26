# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.

        1->2->3->4
        1->4->2->3
        """
        if head == None:
            return
        stack = []
        node = head
        length = 0
        while node != None:
            length += 1
            stack.append(node)
            node = node.next

        node = head
        for _ in range(length//2 + 1):
            n = stack.pop()
            n.next = None
            n.next = node.next
            node.next = n
            node = n.next
        node.next = None
