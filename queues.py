from linked_lists import LinkedList


class Queue(object):
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, data):
        self.add(data)

    def dequeue(self):
        return self.del_at_index(0)

    def is_empty(self):
        if self.queue:
            return True
        return False

    @classmethod
    def make(cls, lst):
        a = cls()
        a.queue.extend(lst)
        return a.queue.head
