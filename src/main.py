class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

class BinarySearchTree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, key):
        if key < self.val:
            if self.left is None: self.left = BinarySearchTree(key)
            else: self.left.insert(key)
        else:
            if self.right is None: self.right = BinarySearchTree(key)
            else: self.right.insert(key)

if __name__ == "__main__":
    print("Logic Core: Fundamental Data Structures Initialized.")
