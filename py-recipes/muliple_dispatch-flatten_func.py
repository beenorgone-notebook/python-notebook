from collections import Iterable

from multipledispatch import dispatch


@dispatch(Iterable)
def flatten(L):
    return sum([flatten(x) for x in L], [])


@dispatch(str)
def flatten(x):
    return [x]


@dispatch(object)
def flatten(x):
    return [x]


a = [1, [2, 3], [4, [5, 6]], [[7, 8], [9, 10]]]
print(flatten([1, ['hello'], 3]))
# [1, 'hello', 3]
print(flatten(a))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
