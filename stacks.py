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
        try:
            to_list = list(lst)
            print "is this what you wanted?", to_list
            return cls(to_list)
        except:
            return "not a list!"

    def __repr__(self):
        if not self.stack:
            return "<stack is empty!>"
        else:
            return "<this long: %s last item: %s>" % (len(self.stack), self.stack[-1])

    def view(self):
        return self.stack

    def __iter__(self):
        while self.stack:
            yield self.pop()

    def push(self, item):
        self.stack.append(item)

    def extend(self, lst):
        self.stack.extend(lst)

    def len(self):
        return len(self.stack)

    def pop(self, num=1):
        if not isinstance(num, int):
            raise StackError("Input invalid, arg should be integer!")
        if self.len() < num:
            raise StackError("Nothing left in Stack")
        if num == 1:
            return self.stack.pop()
        removed = []
        count = 0
        while count != num:
            removed.append(self.stack.pop())
            count += 1
        return reversed(removed)

    def remove(self, num):
        """this one takes only a number as input"""
        removed = self.stack[-num:]
        self.stack = self.stack[:-num]
        return removed

    def slice(self, start=0, end=None):
        if not end:
            end = self.len()
        removed = self.stack[start:end]
        self.stack = self.stack[0:start] + self.stack[end:]
        return removed

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
