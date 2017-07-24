import time
from functools import wraps


def time_that(something):
    """Outputs the time a function takes to execute."""
    def wrapper():
        t1 = time.time()
        something()
        t2 = time.time()
        return "Time it took to run: " + str((t2 - t1)) + "\n"
    return wrapper


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper
