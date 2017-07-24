class TNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left or self.right)

    def has_child(self):
        return self.right or self.left

    def has_children(self):
        return self.right and self.left

    def update(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def len(self):
        return self.size

    def __iter__(self):
        if self:
            if self.has_left():
                for thing in self.left:
                    yield thing
            yield self.key
            if self.has_right():
                for item in self.right:
                    yield item

    def __setitem__(self, key, val):
        self.put(key, val)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        return False

    def __delitem__(self, key):
        self.delete(key)

    def delete(self, key):
        if self.size > 1:
            node = self._get(key, self.root)
            if node:
                self.remove(node)
                self.size -= 1
            else:
                raise KeyError("key not in tree!")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError("key not in tree!")

    def find_new(self):
        new = None
        if self.has_right():
            new = self.right.min()
        else:
            if self.parent:
                if self.is_left():
                    new = self.parent
                else:
                    self.parent.right = None
                    new = self.parent.find_new()
                    self.parent.right = self
        return new

    def min(self):
        curr = self
        while curr.has_left():
            curr = curr.left
        return curr

    def splice(self):
        if self.is_leaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_child():
            if self.has_left():
                if self.is_left():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def remove(self, node):
        if node.is_leaf():
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.has_children():
            new = node.find_new()
            new.splice()
            node.key, node.val = new.key, new.val
        elif node.has_child():
            if node.has_left():
                if node.is_root():
                    node.update(node.left.key,
                                node.left.val,
                                node.left.left,
                                node.left.right)
                else:
                    node.left.parent = node.parent
                    if node.is_left():
                        node.parent.left = node.left
                    else:
                        node.parent.right = node.left
            else:
                if node.is_root():
                    node.update(node.right.key,
                                node.right.val,
                                node.right.left,
                                node.right.right)
                else:
                    node.right.parent = node.parent
                    if node.is_left():
                        node.parent.left = node. right
                    else:
                        node.parent.right = node.right

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TNode(key, val)
        self.size += 1

    def _put(self, key, val, curr):
        if key < curr.key:
            if curr.has_left():
                self._put(key, val, curr.left)
            else:
                curr.left = TNode(key, val, parent=curr)
        elif key == curr.key:
            curr.update(key, val, curr.left, curr.right)
        else:
            if curr.has_right():
                self._put(key, val, curr.right)
            else:
                curr.right = TNode(key, val, parent=curr)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.val
        return None

    def _get(self, key, curr):
        if not curr:
            return None
        elif curr.key == key:
            return curr
        elif key < curr.key:
            return self._get(key, curr.left)
        else:
            return self._get(key, curr.right)
