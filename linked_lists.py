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

    def __str__(self):
        curr = self.head
        stub = "<"
        while curr.next:
            stub += str(curr.data) + ", "
            curr = curr.next
        stub += str(curr.data)
        return stub + ">"

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
            if fast is None:
                return slow.data
            slow = slow.next

    @classmethod
    def get_reversed(cls, thing):
        if not isinstance(thing, LinkedList):
            raise LinkError("this isn't a linked list!")
        out = None
        curr = thing.head
        end = thing.head
        while curr:
            out = Node(curr.data, out)
            curr = curr.next
        result = cls(out)
        result.tail = end
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

    def del_slice(self, i1, i2):
        if self.len() < (max(i1, i2) + 1):
            raise LinkError("index out of range")
        if i1 == i2:
            return LinkedList()
        if i1 + 1 == i2:
            return self.del_at_index(i1)
        curr = self.head
        popped = LinkedList()
        stub = None
        count = 0
        hold = None
        if i1 == 0:
            popped.head = curr
            stub = popped.head
        while curr:
            if count == i1-1:
                popped.head = curr.next
                stub = popped.head
                hold = curr
            elif count == i2-1:
                if hold:
                    hold.next = curr.next
                stub.next = None
                break
            elif count >= i1:
                stub = stub.next
            curr = curr.next
            count += 1
        return popped

    def slice_index(self, i1, i2):
        if self.len() < (max(i1, i2) + 1):
            raise LinkError("index out of range")
        if i1 == i2:
            return LinkedList()
        if i1 + 1 == i2:
            return self.get_at_index(i1)
        curr = self.head
        count = 0
        new = LinkedList()
        while curr:
            if count == i1:
                new.head = curr
                stub = new.head
            elif (count < i2) and (count > i1):
                stub.next = curr
                stub = stub.next
            elif count == i2:
                stub.next = None
            curr = curr.next
            count += 1
        return new

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
            count += 1

    def extend(self, lst):
        for item in lst:
            self.add(item)
        return self

    @classmethod
    def link(cls, lst):
        creation = cls()
        creation.extend(lst)
        return creation

    def unlink(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
