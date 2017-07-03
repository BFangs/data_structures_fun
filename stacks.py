class StackError(Exception):
    """unsure about formatting"""
    def __init__(self, msg):
        super(StackError, self).__init__(msg + (": unable to execute!"))

class Stack(object):
    """implemented using a list"""

    def __init__(self, listed=None):
        if listed:
            self.stack = listed
        else:
            self.stack = []

    @classmethod
    def s(cls, lst):
        if isinstance(lst, list):
            return cls(lst)
        return "not a list!"

    def __repr__(self):
        if not self.stack:
            return "<stack is empty!>"
        else:
            return "<this long: %s last item: %s>" % (len(self.stack), self.stack[-1])

    def __iter__(self):
        while self.stack:
            yield self.pop()

    def push(self, item):
        self.stack.append(item)

    def extend(self, lst):
        self.stack.extend(lst)

    def len(self):
        return len(self.stack)

    def pop(self):
        if not self.stack:
            raise StackError("Nothing left in Stack")
        else:
            return self.stack.pop()

    def peek(self, index=-1):
        try:
            return self.stack[index]
        except IndexError:
            raise StackError("Stack ain't that big")

    def is_empty(self):
        return not self.stack

    def dump(self):
        self.stack, result = [], self.stack
        return result

    def empty(self):
        self.stack = []
