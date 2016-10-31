# https://www.hackerrank.com/challenges/itertools-product

# functional version
from functools import partial
from itertools import product

A, B = [map(int, input().strip().split(' ')) for _ in range(2)]

for i in product(A, B):
    print(i, end=' ')



def to_ints(input_list):
    return map(int, input_list)


def print_iterable(iterable):
    return tuple(map(print_one_line, iterable))

print_one_line = partial(print, end=' ')


A, B = [to_ints(input().strip().split()) for _ in range(2)]
AB = product(A, B)
print_iterable(AB)
