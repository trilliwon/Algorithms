class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None
        self.prev = None
        self.head = None
        self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        walker = self.head
        for i in range(index):
            if walker == None:
                break
            walker = walker.next

        if walker != None:
            return walker.val
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        newNode = MyLinkedList()
        newNode.val = val

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        newNode = MyLinkedList()
        newNode.val = val
        
        if self.tail == None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        
        if index == 0:
            self.addAtHead(val)
        else:
            mover = self.head
            for i in range(index-1):
                if mover == None:
                    break
                mover = mover.next

            if mover != None: 
                newNode = MyLinkedList()
                newNode.val = val

                newNode.next = mover.next
                if newNode.next != None:
                    newNode.next.prev = newNode
                mover.next = newNode
                newNode.prev = mover
                if mover == self.tail:
                    self.tail = newNode

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.head == None:
            return

        mover = self.head

        for i in range(index):
            if mover == None:
                return
            mover = mover.next

        if mover != None:
                
            if mover.prev != None and mover.next != None:
                mover.prev.next = mover.next
                mover.next.prev = mover.prev
            elif mover == self.head and mover == self.tail:
                self.head = None
                self.tail = None
            elif mover == self.head and mover.next != None:
                self.head = self.head.next
                self.head.prev = None
            elif mover.prev != None and mover == self.tail:
                self.tail.prev.next = None
                self.tail = self.tail.prev
                
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
["MyLinkedList","addAtHead","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[1,2],[1],[1],[1]]
["MyLinkedList","addAtHead","addAtIndex","get","get","get"]
[[],[1],[1,2],[1],[0],[2]]
["MyLinkedList","get","addAtIndex","get","get","addAtIndex","get","get"]
[[],[0],[1,2],[0],[1],[0,1],[0],[1]]
["MyLinkedList","addAtHead","addAtHead","deleteAtIndex","addAtIndex","addAtHead","addAtHead","addAtHead","get","addAtTail","addAtIndex","addAtHead"]
[[],[5],[2],[1],[1,9],[4],[9],[8],[3],[1],[3,6],[3]]
["MyLinkedList","addAtHead","get","addAtIndex","deleteAtIndex","get","addAtIndex","addAtHead","get","deleteAtIndex","get","addAtHead","get","addAtHead","addAtTail","addAtHead","get","addAtHead","addAtHead","get","addAtTail","get","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtIndex","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtTail","get","get","addAtHead","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtHead","addAtTail","addAtIndex","addAtTail","addAtHead","addAtTail","addAtHead","get","deleteAtIndex","deleteAtIndex","addAtIndex","addAtTail","addAtTail","deleteAtIndex","get","addAtHead","addAtIndex","addAtHead","addAtTail","addAtIndex","addAtTail","get","addAtHead","addAtHead","addAtTail","addAtTail","addAtHead","addAtHead","addAtIndex","addAtHead","addAtHead","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtHead","addAtIndex","addAtTail","addAtIndex","get","addAtTail","get","addAtHead","get","addAtHead","get","get","addAtHead","get","addAtTail","deleteAtIndex","deleteAtIndex","addAtHead","deleteAtIndex","addAtHead","deleteAtIndex","addAtTail","addAtHead"]
[[],[56],[1],[1,50],[1],[1],[1,43],[82],[2],[3],[1],[41],[1],[44],[36],[57],[1],[64],[24],[4],[89],[5],[7],[33],[11],[24],[2,66],[91],[7],[48],[67],[32],[14],[12],[97],[91],[29],[6],[47],[69],[13],[88],[82],[4],[8],[8,85],[75],[56],[16],[51],[4],[13],[27],[11,62],[66],[10],[4],[28],[87],[22,99],[17],[30],[28,82],[17],[16],[76],[61],[36],[45],[31],[19],[2,73],[56],[58],[48],[87],[2],[4,49],[99],[81],[9,2],[39],[35,35],[19],[98],[50],[73],[22],[29],[6],[45],[13],[54],[42],[3],[8],[27],[16],[43],[39],[0],[23]]
"""
