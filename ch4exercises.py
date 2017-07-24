def findfactorial(num):
    if num == 1:
        return 1
    count = num * findfactorial(num - 1)
    return count


def fib(end):
    if end < 3:
        return 1
    return fib(end-1) + fib(end-2)
