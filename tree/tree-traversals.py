"""
- preorder
- inorder
- postorder 

"""

import collections

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Traversals:
    
    # preorder
    def preorder(self, root):
        if root:
            print(root.val, end=', ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=', ')
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=', ')

    def BFS(self, root):
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            node = q.popleft()

            print(node.val, end=', ')
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

if __name__ == "__main__":

    extree = """
               F
           /      \\
          B        G
        /   \       \\
       A     D       I
            / \     /
           C   E   H
    """
    print(extree)

    root = Node('F')
    root.left = Node('B')
    root.right = Node('G')

    root.left.left = Node('A')
    root.left.right = Node('D')
    root.left.right.left = Node('C')
    root.left.right.right = Node('E')

    root.right.right = Node('I')
    root.right.right.left = Node('H')

    traversals = Traversals()

    print("\n- Preorder traversal")
    traversals.preorder(root)
    print("\n---------------------------\n")

    print("\n- Inorder traversal")
    traversals.inorder(root)
    print("\n---------------------------\n")

    print("\n- Postorder traversal")
    traversals.postorder(root)
    print("\n---------------------------\n")

    print("\n- BFS")
    traversals.BFS(root)
    print("\n---------------------------\n")