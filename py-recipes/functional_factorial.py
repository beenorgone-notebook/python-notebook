import functools
from operator import mul


def medium_runtime(n):
    '''Run a function n times and  print out medium runtime.'''
    def _medium_runtime(func):
        @functools.wraps(func)
        def __medium_runtime(*args, **kwargs):
            from timeit import default_timer as timer
            start = timer()
            for _ in range(n):
                x = func(*args, **kwargs)
            end = timer()
            print("Medium Runtime Is: {}".format((end - start) / n))
            return x
        return __medium_runtime
    return _medium_runtime


def memoize(obj):
    "Apply memoization technique for obj."
    cache = obj.cache = {}

    def _memoize(*args, **kwargs):
        arg_str = str(*args) + str(**kwargs)
        if arg_str not in cache:
            cache[arg_str] = obj(*args, **kwargs)
        return cache[arg_str]
    return _memoize


@medium_runtime(50)
@memoize
def factorial(n):
    return functools.reduce(mul, range(1, n + 1), 1)

print(factorial(3000))
print(factorial(1000))
print(factorial(100))
print(factorial(202))
