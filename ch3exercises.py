from stacks import Stack
import timeit
from random import randint

def check_symbols(thing):
    """checking a string of symbols only to see if balanced"""
    s = Stack()
    i = 0
    balanced = True
    symbols = {"(": ")",
               "{": "}",
               "[": "]"}
    while balanced and i < len(thing):
        char = thing[i]
        if symbols.get(char):
            s.push(char)
        elif s.is_empty():
            balanced = False
        else:
            last = s.pop()
            if char != symbols[last]:
                balanced = False
        i += 1
    if balanced and s.is_empty():
        return True
    return False

def check_tags(doc):
    s = Stack()
    tags = Stack()
    i = 0
    stub = ""
    which = None
    balanced = True
    while balanced and i < len(doc):
        if doc[i] == "<":
            if s.is_empty():
                s.push("<")
                if doc[i+1] == "/":
                    which = "close"
                else:
                    which = "open"
            else:
                balanced = False
        if not s.is_empty():
            if doc[i] == ">":
                s.pop()
                if which == "open"
                    tags.append(stub)
                    stub = ""
                elif which == "close":
                    last = tags.pop()
                    if stub != last:
                        balanced = False
                which = None
                stub = ""
            else:
                stub += doc[i]
        i += 1
    if balanced and s.is_empty() and tags.is_empty():
        return True
    return False

def check_pal(pal):
    """implemented to account for whitespace"""
    squish = [x for x in pal if x != " "]
    for i in xrange(len(squish)):
        if squish[i] != squish[-i-1]:
            return False
    return True


def rev_in_place(thing):
    for i in xrange(len(thing)/2):
        thing[i], thing[-i-1] = thing[-i-1], thing[i]
    return thing

class QueueRear(object):
    """implemented with list rear as queue rear"""
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

class QueueFront(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()

def timer(func, arg):
    def wrapped():
        return func(arg)
    return wrapped

def hotPotato(names, num=None):
    sim = Queue.make(names)
    howmany = len(names)
    while sim.queue.len() > 1:
        num = randint(0, howmany)
        for i in range(num):
            sim.enqueue(sim.dequeue)
        sim.dequeue()
    return sim.dequeue()
