class DoubleError(Exception):
    def __init__(self, msg):
        super(DoubleError, self).__init__(msg + ":what do?")


class Node(object):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "This node has: %s" % (self.data)


class DoubleLinkedList(object):
    def __init__(self, data=None):
        
