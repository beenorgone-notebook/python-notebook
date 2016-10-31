# https://www.hackerrank.com/challenges/map-and-lambda-expression

from functools import wraps


def memoize(func):
    '''Add memoize feature to function'''
    cache = func.cache = {}

    @wraps(func)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoizer


@memoize
def n_fibonaccis(n):
    '''return n first fibonacci numbers'''
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

N = int(input().strip())
CUBE_OF_FIBS = map(lambda x: x ** 3, n_fibonaccis(N))
print(list(CUBE_OF_FIBS))
