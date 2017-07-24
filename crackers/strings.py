# 1.1
def is_unique(thing):
    """if string has all unique characters"""
    if len(thing) > 256:
        return False
    result = [False] * 256
    for char in thing:
        if result[ord(char)]:
            return False
        result[ord(char)] = True
    return True

def is_unique2(thing):
    """no additional data structures"""
    thing.sort()
    for i in xrange(len(thing)-1):
        if thing[i] == thing[i+1]:
            return False
    return True

# 1.2
def is_permutation(foo, bar):
    if foo.sort() == bar.sort():
        return True
    return False

def is_permutation2(foo, bar):
    if len(foo) != len(bar):
        return False
    counts = [0] * 256
    for char in foo:
        counts[ord(char)] += 1
    for char in bar:
        counts[ord(char)] -= 1
        if counts[ord(char)] < 0:
            return False
    return True

# 1.3 urlify a string with %20
def url(thing):
    parts = ["%20" if x == " " else x for x in thing]
    return "".join(parts)

# 1.4 palindrome permutation
def perm_pal(thing):
    odd = 0
    counts = {s:0 for s in al}
    for char in thing:
        if char != " ":
            counts[char] += 1
            if counts[char] % 2:
                odd += 1
            else:
                odd -= 1
    if odd < 2:
        return True
    return False

# 1.5 find if string will be equal with insertion deletion or replacement
def potential_equal(foo, bar):
    original = len(foo)
    new = len(bar)
    if original == new:
        return can_replace(foo, bar, new)
    elif original < new:
        return can_insert(bar, foo, original)
    elif new < original:
        return can_insert(foo, bar, new)
    else:
        return False

def can_replace(ori, diff, distance):
    num = 0
    for i in xrange(distance):
        if ori[i] != diff[i]:
            num +=1
    if num < 2:
        return True
    return False

def can_insert(longer, short, distance):
    shift = 0
    for i in xrange(distance):
        if shift == 0:
            if short[i]!=longer[i]:
                if short[i] != longer[i+1]:
                    return False
                shift +=1
        elif shift == 1:
            if short[i]!=longer[i+1]:
                return False
    return True

# 1.6

# 1.7

# 1.8

# 1.9
