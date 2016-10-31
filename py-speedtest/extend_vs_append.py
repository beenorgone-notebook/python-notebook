def append(alist, iterable):
    for item in iterable:
        alist.append(item)

def extend(alist, iterable):
    alist.extend(iterable)

import timeit

print(min(timeit.repeat('lambda: append([], "abcdefghijklmnopqrstuvwxyz")', repeat=20, number=1000000)))
print(min(timeit.repeat('lambda: append([], "abcdefghijklmnopqrstuvwxyz")', repeat=20, number=1000000)))
print(max(timeit.repeat('lambda: append([], "abcdefghijklmnopqrstuvwxyz")', repeat=20, number=1000000)))
print(max(timeit.repeat('lambda: append([], "abcdefghijklmnopqrstuvwxyz")', repeat=20, number=1000000)))

print(min(timeit.repeat('lambda: append([], "a")', repeat=20, number=1000000)))
print(min(timeit.repeat('lambda: extend([], ["a"])', repeat=20, number=1000000)))
print(min(timeit.repeat('lambda: extend([], "a")', repeat=20, number=1000000)))
print(max(timeit.repeat('lambda: append([], "a")', repeat=20, number=1000000)))
print(max(timeit.repeat('lambda: extend([], ["a"])', repeat=20, number=1000000)))
print(max(timeit.repeat('lambda: extend([], "a")', repeat=20, number=1000000)))

'''
0.0933285720020649
0.09314376100155641
0.09545929099840578
0.09714219799934654

0.09300531600092654
0.09291150900025968
0.09264149699811242
0.09703555200030678
0.10708495500148274
0.121265007997863
'''
