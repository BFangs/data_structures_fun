# 2.1
def remove_dup(lst):
    seen = set()
    curr = lst.head
    prev = None
    while curr:
        if curr.data in seen:
            prev.next = curr.next
        else:
            seen.add(curr.data)
            prev = curr
        curr = curr.next
    return lst

def remove_dup2(lst):
    """no additional memory"""
    curr = lst.head
    while curr:
        run = curr
        while run.next:
            if run.next.data == curr.data:
                run.next == run.next.next
            run = run.next
        curr = curr.next
    return lst

# 2.2 find kth element from the tail
def find_k(lst, k):
    curr = lst.head
    k = curr
    count = 0
    while count != k:
        k = k.next
        count += 1
        if k == None:
            return None
    while k.next != None:
        k = k.next
        curr = curr.next
    return curr.data

def recurse_k(lst, k):
    pass


# 2.3 only have access to a single node, delete it
def del_node(node):
    try:
        node.data = node.next.data
        node.next = node.next.next
    except:
        print "tail node, not possible"


# 2.4 pivot linked list elements around a value x
def partition(lst, x):
    curr = lst.head
    lst.tail = curr
    while curr:
        hold = curr.next
        print hold
        if curr.data < x:
            curr.next = lst.head
            lst.head = curr
        else:
            lst.tail.next = curr
            lst.tail = curr
        curr = hold
    lst.tail.next = None
    return lst


# 2.5

# 2.6

# 2.7

# 2.8
