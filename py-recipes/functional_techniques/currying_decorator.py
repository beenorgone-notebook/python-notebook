import functools


def curried(n):
    def curry(fn):
        def _inner(*args):
            if len(args) < n:
                return curried(n - len(args))(functools.partial(fn, *args))
            return fn(*args)
        return _inner
    return curry


@curried(5)
def returnargs(*args):
    return args


@curried(4)
def multiply(a, b, c, d, e):
    print('Now we will have')
    return a * b * c * d * e


r = multiply(2, 3, 5, 8, 9)
print(r)
# Now we will have
# 2160

r1 = multiply(1)
print(r1)
# <function curried.<locals>.curry.<locals>._inner at 0x7fce820aed90>
print(r1(2, 3, 4, 5))
# Now we will have
# 120
