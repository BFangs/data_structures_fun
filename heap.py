class HeapError(Exception):
    def __init__(self, msg):
        super(HeapError, self).__init__(msg + ": unable to do")


class BinaryHeap():
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.perc_up(self.size)

    def perc_up(self, i):
        while (i / 2) > 0:
            if self.heap[i] < self.heap[i / 2]:
                hold = self.heap[i / 2]
                self.heap[i / 2] = self.heap[i]
                self.heap[i] = hold
            i = i / 2

    def perc_down(self, i):
        while (i * 2) <= self.size:
            mini = self.minchild(i)
            if self.heap[i] > self.heap[mini]:
                self.heap[i], self.heap[mini] = self.heap[mini], self.heap[i]
            i = mini

    def minchild(self, i):
        if (i * 2 + 1) > self.size:
            return self.heap[i * 2]
        else:
            if self.heap[i * 2] > self.heap[i * 2 + 1]:
                return self.heap[i * 2 + 1]
            else:
                return self.heap[i * 2]

    def show_min(self):
        return self.heap[1]

    def get_min(self):
        popped = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.perc_down(1)
        return popped

    def is_empty(self):
        if self.heap:
            return False
        return True

    def size(self):
        return self.size

    @classmethod
    def build(cls, lst):
        if not isinstance(lst, list):
            raise HeapError("not a list! cannot build")
        new = cls()
        new.size = len(lst)
        i = new.size / 2
        new.heap = [0] + lst
        while (i > 0):
            new.perc_down(i)
            i -= 1
        return new
