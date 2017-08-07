import random


class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def valid(self):
        if self.is_leaf():
            return True
        if self.left:
            if self.left < self.value:
                left = self.left.valid()
            else:
                return False
        if self.right:
            if self.right > self.value:
                right = self.right.valid()
            else:
                return False
        return left and right

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        if not self.stack():
            return None
        return self.stack[-1]

    def is_empty(self):
        return not self.stack


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


# 1
def highest_stock(lst):
    """find highest profit for buying and selling"""
    if len(lst) < 2:
        raise Exception("must be able to buy and sell in a day")
    lowest = lst[0]
    profit = lst[1] - lst[0]
    for stock in lst:
        new = stock - lowest
        profit = max(profit, new)
        lowest = min(stock, lowest)
    return profit


# 2
def product(lst):
    """for each find the product of all integers except index"""
    before = [None] * len(lst)
    sofar = 1
    since = 1
    for i in xrange(len(lst)):
        before.append(sofar)
        sofar *= lst[i]
    for i in xrange(len(lst)-1, -1, -1):
        before[i] *= since
        since *= lst[i]
    return before


# 3
def highest_product(lst):
    """find highest product from three integers in lst"""
    three = lst[0] * lst[1] * lst[3]
    highest_two = lst[0] * lst[1]
    lowest_two = lst[0] * lst[1]
    highest = lst[0]
    lowest = lst[0]
    for i, num in enumerate(lst[3:]):
        if num * highest_two > three:
            three = num * highest_two
        if num * lowest_two > three:
            three = num * lowest_two
        if num * highest > highest_two:
            highest_two = num * highest
        if num * lowest > lowest_two:
            lowest_two = num * highest
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    return three


# 4
def availabilities(lst):
    """given a list of tuples with available times return condensed meeting times"""
    ordered = sorted(lst)
    new = [ordered[0]]
    for start, end in ordered[1:]:
        if new[-1][1] >= start:
            if new[-1][1] > end:
                new[-1] = (new[-1][0], new[-1][1])
            else:
                new[-1] = (new[-1][0], end)
        else:
            new.append((start, end))
    return new


# 5
coinmemo = {}


def coins(lst, target, index=-1):
    """list of denominations and a target number returns number of ways to make it"""
    if target == 0:
        return 1
    if target < 0:
        return 0
    if index < -len(lst):
        return 0
    coin = lst[index]
    possible = 0
    while target > 0:
        if not coinmemo.get((target, index-1)):
            coinmemo[(target, index-1)] = coins(lst, target, index-1)
        possible += coinmemo[(target, index-1)]
        target -= coin
    return possible


def make_coins(denominations, target):
    """dynamic programing approach"""
    subs = [0] * (target + 1)
    subs[0] = 1

    for coin in denominations:
        for x in xrange(coin, target + 1):
            leftover = x - coin
            subs[x] += subs[leftover]
    return subs[target]


# 6
def find_intersection(one, two):
    """find intersection of rectangles defined as dictionaries"""
    for rectangle in [one, two]:
        rectangle['top'] = rectangle['bottom_y'] + rectangle['height']
        rectangle['right'] = rectangle['left_x'] + rectangle['width']
    y = min(one['top'], two['top']) - max(one['bottom_y'], two['bottom_y'])
    x = min(one['right'], two['right']) - max(one['left_x'], two['left_x'])
    if y > 0 and x > 0:
        overlap = {'left_x': max(one['left_x'], two['left_x']),
                   'bottom_y': max(one['bottom_y'], two['bottom_y']),
                   'width': x,
                   'height': y}
        return overlap
    return None


# 7
class TempTracker(object):
    def __init__(self):
        self.temps = {}
        self.mean = None
        self.size = 0
        self.max = None
        self.min = None
        self.mode = None
        self.mode_number = 0

    def insert(self, temperature):
        """records new temperature"""

        if self.size == 0:
            self.mean = float(temperature)
            self.mode = temperature
            self.mode_number = 1
            self.max = temperature
            self.min = temperature
            self.temps[temperature] = 1
        else:
            if temperature < self.min:
                self.min = temperature
            if temperature > self.max:
                self.max = temperature
            self.mean = ((self.mean * self.size) + float(temperature)) / (self.size + 1)
            self.temps[temperature] = self.temps.setdefault(temperature, 0) + 1
            if self.temps[temperature] > self.mode_number:
                self.mode = temperature
                self.mode_number = self.temps[temperature]
        self.size += 1

    def get_max(self):
        """returns highest"""
        return self.max

    def get_min(self):
        """returns lowest"""
        return self.min

    def get_mean(self):
        """returns mean"""
        return self.mean

    def get_mode(self):
        """gets mode"""
        return self.mode


# 8
def is_superbalanced(root):
    visit = [(root, 0)]
    depths = []
    while visit:
        curr, depth = visit.pop()
        if curr.is_leaf():
            if depth not in depths:
                depths.append(depth)
                if len(depths) > 2:
                    return False
                if len(depths) == 2 and abs(depths[0] - depths[1]) > 1:
                    return False
        else:
            if curr.left:
                visit.append((curr.left, depth + 1))
            if curr.right:
                visit.append((curr.right, depth + 1))
    return True


# 9
def valid_tree(root):
    visit = [(root, None, None)]
    while visit:
        curr, lower, upper = visit.pop()
        if upper:
            if curr.value > upper:
                return False
        if lower:
            if curr.value < lower:
                return False
        if curr.left:
            visit.append((curr.left, lower, curr.value))
        if curr.right:
            visit.append((curr.right, curr.value, upper))
    return True


# 10
def find_second(root):
    """find second largest element in BST"""
    if root is None or (root.left is None and root.right is None):
        raise Exception("tree needs at least two nodes")
    curr = root
    fork = False
    while curr:
        if curr.right:
            if curr.right.is_leaf() and fork is False:
                return curr
            curr = curr.right
        elif curr.right is None and fork is True:
            return curr
        elif curr.left and fork is False:
            curr = curr.left
            fork = True


def recursive_second(root):
    """find second largest element in BST cleaned up recursive code"""
    if root is None or (root.left is None and root.right is None):
        raise Exception("tree needs at least two nodes")
    if root.left and root.right is None:
        return recursive_second(root.left)
    if root.right:
        if root.right.is_leaf():
            return root.value
    return recursive_second(root.right)


# 11
class Trie(object):
    def __init__(self):
        self.root = {}

    def add(self, word):
        curr = self.root
        newflag = False
        for char in word:
            curr = curr.setdefault(char, {})
            if curr == {}:
                newflag = True
        if "end" not in curr:
            newflag = True
            curr["end"] = {}
        return newflag


# 12 maybe clean up code later
def binary_search(lst, target):
    """seeing if number is in a sorted list. """
    if not lst:
        raise Exception("nothing to search")
    index = len(lst) / 2
    increment = index / 2
    while increment >= 1:
        if lst[index] < target:
            index += increment
            increment /= 2
        elif lst[index] > target:
            index -= increment
            increment /= 2
        else:
            return True
    return False


# 13
def find_rotation(lst):
    """return the index of the rotation point"""
    start = lst[0]
    ceiling = len(lst) - 1
    floor = 0
    while (ceiling - floor) > 1:
        index = floor + ((ceiling - floor) / 2)
        if lst[index] >= start:
            floor = index
        elif lst[index] < start:
            if lst[index-1] >= start:
                return index
            else:
                ceiling = index
    return index


# 14
def find_two(lst, time):
    seen = set()
    for movie in lst:
        leftover = (time - movie)
        if leftover in seen:
            return True
        seen.add(movie)
    return False


# 15
def fib(n):
    a = 0
    b = 1
    if n < 0:
        raise Exception("not positive number")
    elif n == 0:
        return a
    index = 2
    while index < n:
        a, b = b, a + b
        index += 1
    return b


# 16 need to study unbound knapsack and dynamic programming
def max_cake(lst, capacity):
    pass


# 17 question about javascript variable scope, review later


# 18 question about javascript variable mutability review closures later


# 19
class Queue(object):
    def __init__(self):
        self.stackin = Stack()
        self.stackout = Stack()

    def enqueue(self, data):
        self.stackin.push(data)

    def dequeue(self):
        if self.stackout:
            return self.stackout.pop()
        elif self.stackin:
            while self.stackin:
                hold = self.stackin.pop()
                self.stackout.push(hold)
            return self.stackout.pop()
        else:
            raise Exception("nothing to dequeue")


# 20
class MaxStack(object):
    def __init__(self):
        self.stack = Stack()
        self.max = Stack()

    def push(self, data):
        self.stack.push(data)
        if self.max.peek() is None or data >= self.max.peek():
            self.max.push(data)

    def pop(self):
        if not self.stack:
            return None
        if self.stack.peek() == self.max.peek():
            self.max.pop()
        return self.stack.pop()

    def get_max(self):
        return self.max.peek()


# 21 practice using bitwise operators!
def find_unique(lst):
    seen = set()
    for num in lst:
        if num not in seen:
            seen.add(num)
        else:
            seen.remove(num)
    return seen.pop()


def find_bitwise(lst):
    seen = 0
    for num in lst:
        seen ^= num
    return seen


# 22
def delete_node(node):
    next = node.next
    if next:
        node.data = next.data
        node.next = next.next
    else:
        raise Exception("can't delete tail node")


# 23 check if linked list has a cycle
def check_loop(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# 24 my code was ugly, practice more
def reverse_list(head):
    curr = head
    prev = None
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


# 25
def find_kth_node(k, head):
    count = 0
    fast = head
    slow = head
    while count != k:
        try:
            fast = fast.next
            count += 1
        except:
            raise Exception("not enough nodes in list")
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow


#  26 reverse a string in place, but not really because strings are immutable
def rev_string(words):
    thing = list(words)
    for i in xrange(len(thing)/2):
        thing[i], thing[-i-1] = thing[-i-1], thing[i]
    return "".join(thing)


def rev_words(phrase):
    words = phrase.split(" ")
    for i in xrange(len(words)/2):
        words[i], words[-i-1] = words[-i-1], words[i]
    return " ".join(words)


# 27
def match_parens(chars, match):
    indices = Stack()
    for i, char in enumerate(chars):
        if char == "(":
            indices.push(i)
        elif char == ")":
            opening = indices.pop()
            if opening == match:
                return i
    return None


# 28
def validate_tokens(doc):
    match = {"(": ")",
             "{": "}",
             "[": "]"}
    tokens = Stack()
    for char in doc:
        if char in "({[":
            tokens.push(char)
        elif char in ")}]":
            if tokens.is_empty():
                return False
            last = tokens.pop()
            if char != match.get(last):
                return False
    if tokens.is_empty():
        return True
    return False


# 30
def palindrome_perm(word):
    singles = set()
    for char in word:
        if char in singles:
            singles.remove(char)
        else:
            singles.add(char)
    return len(singles) <= 1


# 31
def permute(thing):
    if len(thing) <= 1:
        return set(thing)
    stub = permute(thing[:-1])
    permutations = set()
    for item in stub:
        for x in range(len(thing)):
            permutation = item[:x] + thing[-1] + item[x:]
            permutations.add(permutation)
    return permutations


# 32
def sort_scores(lst):
    counter = [0] * 101
    for num in lst:
        counter[num] += 1
    result = []
    for i, item in enumerate(counter[::-1]):
        result.extend([i] * item)
    return result


# 33
def find_double(lst):
    total = sum(lst)
    unique = sum(range(len(lst) - 1))
    return total - unique


# 34
def build_cloud(doc):
    words = doc.split(" ")
    results = {}
    for word in words:
        results[word.strip(".,!?:;()").upper()] = results.setdefault(word.strip(".,!?:;()").upper(), 0) + 1


# 35 first one not truly well distributed probability wise
def shuffle(lst):
    for i in xrange(len(lst)):
        new = random.randint(0, len(lst) - 1)
        lst[i], lst[new] = lst[new], lst[i]


def really_shuffle(lst):
    if len(lst) <= 1:
        return lst
    for i in range(0, len(lst) - 1):
        new = random.randint(i, len(lst) - 1)
        lst[i], lst[new] = lst[new], lst[i]


# 36
def determine_riffle(deck, half1, half2):
    half1 = reversed(half1)
    half2 = reversed(half2)
    for card in deck:
        if half1 and card == half1[-1]:
            half1.pop()
        elif half2 and card == half2[-1]:
            half2.pop()
        else:
            return False
    return True


# 37
def rand7():
    """given for problem"""
    return random.randint(7)


def rand5():
    result = rand7()
    while result > 5:
        result = rand7()
    return result


# 38
def rand7_from5():
    roll1 = rand5()
    roll2 = rand5()
    while roll1 in [4, 5] and roll2 in [1, 2]:
        roll1 = rand5()
        roll2 = rand5()
    return (roll1 + roll2) % 7 + 1


"""
  1  2  3  4  5
1 3  4  5  6  7
2 4  5  6  7  1
3 5  6  7  1  2
4 6  7  1  2  3
5 7  1  2  3  4

1 4
2 3
3 3
4 3
5 3
6 4
7 5
"""


# 39 result is that the drop needs to change every time, optimal is 14!
# drop every 25 => worst case 28
# drop every 10 => worst case 19
# drop every 15 => worst case 28
# drop every 25 => worst case 28


# 40
def find_dupes(lst):
    lst.sort()
    for i, num in enumerate(lst):
        if num == lst[i+1]:
            return num


def find_dupes_better(lst): # incomplete
    n = len(lst) - 1
    floor = 1
    cut = (n - floor) / 2
    part1 = 0
    part2 = 0
    while (n - floor) > 1:
        for num in lst:
            if num <= cut:
                part1 += 1
            else:
                part2 += 1
        if part1 > part2:
            n = cut
        else:
            floor = cut
        cut = (n - floor) / 2
        part1 = 0
        part2 = 0
    return n


# 42 essentially same, but more correct functions for os reading files and such
# including last edited time
def duped_files(root):
    visit = []
    seen = {}
    if root is None:
        return []
    visit.add(root)
    while visit:
        curr = visit.pop()
        for item in curr:
            if item.is_directory():
                visit.append(item)
            else:
                if seen.get(item.data):
                    seen[item.data] = (seen[item.data], item)
                else:
                    seen[item.data] = item
    return seen.values()


# 43
def merge(one, two):
    merged = []
    oneindex = 0
    twoindex = 0
    while oneindex < len(one) and twoindex < len(two):
        if one[oneindex] <= two[twoindex]:
            merged.append(one[oneindex])
            oneindex += 1
        else:
            merged.append(two[twoindex])
            twoindex += 1
    if oneindex < len(one):
        merged.extend(one[oneindex:])
    else:
        merged.extend(two[twoindex:])
    return merged


# 44 create a shortened url interface?
# data model: want a column for the shortened part of the url and one
# for the full length of the url, the shortened part should be indexed


# 45
def color_nodes(graph, d):
    colors = set(range(d + 1))
    for node in graph:
        illegal = set()
        for neighbor in node.neighbors:
            if neighbor == node:
                raise Exception("graph has a loop, problem impossible")
            illegal.add(neighbor.color)
        for color in colors:
            if color not in illegal:
                node.color = color
                break
