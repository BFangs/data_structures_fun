# 8.1 child running up stairs can hop either 1,2,3 steps, how many ways?
memo = {}
def hops(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo.get(n, -1) >= 0:
        return memo[n]
    memo[n] = hops(n-1, memo) + hops(n-2, memo) + hops(n-3, memo)
    return memo[n]

# 8.2

# 8.3

# 8.4
def powerset(thing):
    pass

# 8.5 recursively multiply without *
def mult(x, y):
    if y == 0:
        return 0
    return x + mult(x, y-1)

# 8.6

# 8.7

# 8.8

# 8.9

# 8.10

# 8.11

# 8.12

# 8.13

# 8.14
