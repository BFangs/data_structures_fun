class DoubleError(Exception):
    def __init__(self, msg):
        super(DoubleError, self).__init__(msg + ":what do?")


class Node(object):
    def __init__(self, data, prev=None, nex=None):
        self.data = data
        self.prev = prev
        self.next = nex

    def __repr__(self):
        return "This node has: %s" % (self.data)


class DoubleLinkedList(object):
    def __init__(self, data=None):
        self.head = data
        self.tail = data

    def add(self, data):
        last = self.tail
        new = Node(data, last)
        
