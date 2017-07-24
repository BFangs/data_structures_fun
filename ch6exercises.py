from stacks import Stack
import operator as op


class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, new):
        if self.left is None:
            self.left = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.left = self.left
            self.left = t

    def insert_right(self, new):
        if self.right is None:
            self.right = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.right = self.right
            self.right = t

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_root(self, thing):
        self.key = thing

    def get_root(self):
        return self.key

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    def leaves(self):
        if self.is_leaf():
            return True
        if self.left.is_leaf() and self.right.is_leaf():
            return True
        return False


def preshow(tree):
    if tree:
        print tree.key
        show(tree.left)
        show(tree.right)


def show(tree):
    if tree:
        show(tree.left)
        print tree.key
        show(tree.right)


def postshow(tree):
    if tree:
        show(tree.left)
        show(tree.right)
        print tree.key


def build_parse(data):
    data = list(data)
    ops = Stack()
    tree = BinaryTree(" ")
    curr = tree
    print curr
    ops.push(tree)
    for i in data:
        if i == "(":
            curr.insert_left(" ")
            ops.push(curr)
            curr = curr.get_left()
        elif i not in '+-*/)':
            curr.set_root(int(i))
            curr = ops.pop()
        elif i in '+-*/':
            curr.set_root(i)
            curr.insert_right(" ")
            ops.push(curr)
            curr = curr.get_right()
        elif i == ')':
            curr = ops.pop()
        else:
            raise ValueError("unsupported operator " + i)
    return tree


def eval_tree(tree):
    ops = {"-": op.add,
           "+": op.sub,
           "*": op.mul,
           "/": op.truediv}
    if tree:
        left = tree.get_left()
        right = tree.get_right()
        if left and right:
            func = ops[tree.get_root()]
            return func(eval_tree(left), eval_tree(right))
        else:
            return tree.get_root()


def printops(tree):
    val = ""
    if tree:
        left = printops(tree.get_left())
        if not tree.is_leaf():
            left = "(" + left
        right = printops(tree.get_right())
        if not tree.is_leaf():
            right += ")"
        val = left + str(tree.get_root()) + right
    return val
