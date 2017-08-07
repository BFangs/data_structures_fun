# add to bst


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def insert_recursive(self, data):
        if data <= self.data:
            if self.left:
                self.left.insert_bit(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.insert_bit(data)
            else:
                self.right = Node(data)


class Tree(object):
    def __init__(self, root):
        self.root = root

    def insert(self, data):
        curr = self.root
        while curr:
            if data < curr.data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(data)
                    curr = None
            elif data > curr.data:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(data)
                    curr = None
