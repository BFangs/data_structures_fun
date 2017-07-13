class LinkError(Exception):
    def __init__(self, msg):
        super(LinkError, self).__init__(msg + ":unable to execute")

class Node(object):
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __repr__(self):
        return "This node has: %s" % (self.data)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def __repr__(self):
        return "This linked list starts: %s and is %s long!" % (self.head, self.len())

    def is_empty(self):
        if not self.head:
            return True
        return False

    def get_midpoint(self):
        slow = self.head
        fast = self.head
        while slow and fast:
            if fast == self.tail:
                return slow.data
            fast = fast.next.next
            if fast == None:
                return slow.data
            slow = slow.next

    @classmethod
    def get_reversed(cls, thing):
        if not isinstance(thing, LinkedList):
            raise LinkError("this isn't a linked list!")
        out = None
        curr = thing.head
        while curr:
            out = Node(curr.data, out)
            curr = curr.next
        result = cls(out)
        return result.head

    def reverse_link(self):
        if self.len() < 2:
            return self.head
        prev = None
        curr = self.head
        self.tail = self.head
        while curr:
            hold = curr.next
            curr.next = prev
            prev = curr
            curr = hold
        self.head = prev
        return self.head

    def len(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def print_list(self):
        if self.is_empty():
            print "nothing here"
        curr = self.head
        while curr:
            print curr.data
            curr = curr.next

    def find(self, data):
        """return true if data exists in list"""
        if self.is_empty():
            raise LinkError("nothing here!")
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def get_index(self, data):
        """returns indices data exists in"""
        if self.is_empty():
            raise LinkError("nothing here!")
        count = 0
        curr = self.head
        indices = []
        while curr:
            if curr.data == data:
                indices.append(count)
            curr = curr.next
            count += 1
        return indices

    def get_at_index(self, index):
        """get data at 0 based index"""
        if self.len() < (index + 1):
            raise LinkError("index out of range")
        count = 0
        curr = self.head
        while count != index:
            curr = curr.next
            count += 1
        return curr.data

    def remove(self, data):
        """remove all nodes with this data"""
        if self.is_empty():
            raise LinkError("nothing to remove!")
        old = self.len()
        if self.head.data == data:
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
        print "%s items removed" % (old - self.len())

    def del_at_index(self, index):
        """delete node at index"""
        if self.len() < (index + 1):
            raise LinkError("index out of range")
        curr = self.head
        if index == 0:
            self.head = curr.next
            return curr.data
        count = 0
        while count != (index - 1):
            curr = curr.next
            count += 1
        removed = curr.next.data
        curr.next = curr.next.next
        return removed

    def pop(self):
        """pop the last item off the list"""
        if self.is_empty():
            raise LinkError("nothing there!")
        popped = self.tail
        if self.len() == 1:
            self.head = None
            self.tail = None
        curr = self.head
        while curr:
            if curr.next == self.tail:
                self.tail = curr
                curr.next = None
            curr = curr.next
        return popped.data

    def chop(self):
        """remove head of list"""
        if self.is_empty():
            raise LinkError("nothing here")
        self.head = self.head.next
        if not self.head:
            self.tail = None

    def add(self, data):
        new = Node(data)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new

    def add_after(self, data, target):
        new = Node(data)
        curr = self.head
        while curr:
            if curr.data == target:
                new.next = curr.next
                curr.next = new
                return True
            curr = curr.nextl
        return False

    def add_at_index(self, data, index):
        new = Node(data)
        if self.len < index:
            raise LinkError("index out of range")
        curr = self.head
        if index == 0:
            new.next = curr
            self.head = new
            return True
        count = 0
        while curr:
            if count == (index - 1):
                new.next = curr.next
                curr.next = new
                return True
            curr = curr.next
            count +=1

    def extend(self, lst):
        for item in lst:
            self.add(item)
        return self

    @classmethod
    def link(cls, lst):
        creation = cls()
        creation.extend(lst)
        return creation
