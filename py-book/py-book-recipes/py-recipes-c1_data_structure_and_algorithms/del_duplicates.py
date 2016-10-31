# Removing the duplicate values in a sequence,
# but preserve the order of the remaining items.


# Solution for hashable sequence
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# Solution for unhashable types (such as dicts)
def dedupe(items, key=None):
    seen = set()
    for item in items:
        if key is None:
            val = item
        else:
            # the purpose of the key argument is to specify a
            # function that converts sequence items into a
            # hashable type for the purposes of duplicate detection.
            val = key(item)
        if val not in seen:
            yield item
            seen.add(val)


# Solution use itertools
from itertools import filterfalse


def dedupe(iterable, key=None):
    '''List unique elements, preserving order.
    Remember all elements ever seen.'''
    seen = set()
    if key is None:
        for item in filterfalse(seen.__contains__, iterable):
            seen.add(item)
            yield item
    else:
        for item in iterable:
            val = key(item)
            if val not in seen:
                yield item
                seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))


'''Discussion

The use of a generator function in this recipe reflects the fact
that you might want the function to be extremely general
purpose—not necessarily tied directly to list processing.
For example, if you want to read a file,
eliminating duplicate lines, you could simply do this:

    with open(somefile,'r') as f:
        for line in dedupe(f):
        ...

The specification of a key function mimics similar functionality
in built-in functions such as sorted() , min() , and max() .
'''
