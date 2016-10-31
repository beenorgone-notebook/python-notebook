class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

fib = Fib(10)
iter(fib)
print(next(fib))


def Fib(n):
    '''Fibonacci generator function'''
    a, b = 0, 1
    while a < n:
        val = (yield b)
        # If value provided, change fibonacci number
        if val is not None:
            a, b = val, b + val
        else:
            a, b = b, a + b

'''
>>> f = Fib(39)
>>> f.send(9)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    f.send(9)
TypeError: can't send non-None value to a just-started generator
>>> next(f)
1
>>> f.send(9)
10
>>> next(f)
19
>>> next(f)
29
>>>
'''


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer


@memoize
def Fib(n):
    '''Fibonacci generator function combine with memoize technique'''
    a, b = 0, 1
    while a < n:
        val = (yield b)
        # If value provided, change fibonacci number
        if val is not None:
            a, b = val, b + val
        else:
            a, b = b, a + b
