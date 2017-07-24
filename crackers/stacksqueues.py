class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min = None
    def __repr__(self):
        return "Node: %s Next: %s Min: %s" %(self.data, self.next, self.min)

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

    def add(self, data, min):
        new = Node(data)
        new.min = min
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new

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

# 3.1 use a single array to implement three stacks


# 3.2 implement a min value finder in O(1), can do with extra stack or extra values with each node
class Stack(object):
    def __init__(self):
        self.stack = LinkedList()
        self.min = None

    def push(self, data):
        if data < self.min:
            self.min = data
        self.stack.add(data, self.min)

    def pop(self):
        last = self.stack.pop()
        if last.min != self.min:
            self.min = last.min
        return last

class StackMin(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

mins = StackMin()

class StackLess(object):
    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):
        if data <= mins.peek():
            mins.push(data)
        self.stack.add(data)

    def pop(self):
        last = self.stack.pop()
        if last.data == mins.peek():
            mins.pop()
        return last

    def get_min(self):
        return mins.peek()

# 3.3 implement a data structure that mimics starting a new stack when previous stack gets too high
from stacks import Stack

class SetOfStacks(object):

    def __init__(self, limit=10):
        self.stacks = []
        self.limit = limit

    def empty(self):
        if not self.stacks:
            return True
        return False

    def underflow(self):
        if not self.empty() and not self.stacks[-1]:
            return True
        return False

    def peek(self):
        if not self.empty():
            return self.stacks[-1]

    def overflow(self):
        if not self.stacks:
            return True
        if len(self.stacks[-1]) == self.limit:
            return True
        return False

    def push(self, data):
        if self.overflow():
            self.stacks.append([data])
        else:
            self.stacks[-1].append(data)

    def pop(self):
        if self.empty():
            raise StackError("nothing left")
        if self.underflow():
            self.stacks.pop()
        return self.stacks[-1].pop()

    def del_index(i):
        if i >= len(self.stacks):
            raise StackError("nothing there")
        if i + 1 == len(self.stacks):
            return self.pop()
        popped = self.stacks[i].pop()
        hold = None
        for x in xrange(i+1, len(self.stacks)):
            hold = self.stacks[x][0]
            self.stacks[x] = self.stacks[x][1:]
            self.stacks[x-1].append(hold)
        return popped

# 3.4

# 3.5

# 3.6
