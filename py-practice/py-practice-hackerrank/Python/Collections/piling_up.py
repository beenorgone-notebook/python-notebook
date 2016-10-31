# https://www.hackerrank.com/challenges/piling-up

from collections import deque


def stackable(cubes):
    if not cubes:
        return 'No'
    elif len(cubes) == 1:
        return 'Yes'
    else:
        stack = [max(cubes.pop(), cubes.popleft())]
        while len(cubes) > 1:
            right_most = cubes.pop()
            left_most = cubes.popleft()
            picked_cube = max(left_most, right_most)
            if picked_cube <= stack[-1]:
                stack.append(picked_cube)
            else:
                return 'No'
        if not cubes:
            return 'Yes'
        else:
            if cubes[0] <= stack[-1]:
                stack.append(cubes[0])
                return 'Yes'
            else:
                return 'No'


T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    cubes = deque(map(int, input().strip().split()))
    print(stackable(cubes))


# not using deque, imperative version:
T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    cubes = tuple(map(int, input().strip().split()))
    i = 0
    while i < n - 1 and cubes[i] >= cubes[i + 1]:
        i += 1
    while i < n - 1 and cubes[i] <= cubes[i + 1]:
        i += 1
    if i == n - 1:
        print('Yes')
    else:
        print('No')


'''
FUNCTIONAL (BUT SLOW) VERSION:
To change while loop to functional version, use recursion.

def func(my_list, z):

    if z == len(my_list):
        return something
    else:
        # do something else
        return func(my_list, z+1)

In this version, we use tail-call recursion
(Which might be best if Python support tail-call optimization).
To know more about tail-call optimization in Python,
read this 'What have we gained?' in this document:
http://blog.moertel.com/posts/2013-05-11-recursive-to-iterative.html
'''


def test_then_change_arg(tracking_arg, change_func, test_func,
                         *args, **kwargs):
    if test_func(tracking_arg, *args, **kwargs):
        return test_then_change_arg(change_func(tracking_arg),
                                    change_func, test_func,
                                    *args, **kwargs)
    else:
        return tracking_arg


def add_one(arg):
    return arg + 1


def stackable(cubes):
    i = 0
    n = len(cubes)

    def test_one(k, cubes, n):
        return k < n - 1 and cubes[k] >= cubes[k + 1]

    def test_two(k, cubes, n):
        return k < n - 1 and cubes[k] <= cubes[k + 1]

    j = test_then_change_arg(i, add_one, test_one, cubes, n)
    m = test_then_change_arg(j, add_one, test_two, cubes, n)
    if m == n - 1:
        return 'Yes'
    else:
        return 'No'

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    cubes = tuple(map(int, input().strip().split()))
    print(stackable(cubes))
