class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "This node has: %s" % (self.data)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def is_empty(self):
        if not self.head:
            return True

    def len(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def print_list(self):
        if self.is_empty():
            print "nothing here!"
        curr = self.head
        while curr:
            print curr.data
            curr = curr.next

    def find(self, data):
        """return true if data exists in list"""
        if self.is_empty():
            print "nothing here!"
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next

    def remove(self, data):
        """remove all nodes with this data"""
        if self.is_empty():
            print "nothing to remove!"
        elif self.head.data == data:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                if not curr.next:
                    self.tail = curr
            curr = curr.next

    def add(self, data):
        new = Node(data)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new

    def extend(self, lst):
        for item in lst:
            self.add(item)

    @classmethod
    def link(cls, lst):
        creation = LinkedList()
        creation.extend(lst)
        return creation
