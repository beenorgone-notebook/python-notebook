# Implement a queue that sorts items by a given priority and always
# returns the item with the highest priority on each pop operation.
# SOLUTION: Using heapq

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heapq will sort items based on -priority, self._index.
        # self._index is needed because item could be unorderable.
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

'''
class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
'''

'''Discussion

The queue consists of tuples of the form `(-priority, index, item)`.
The `priority` value is negated to get the queue to sort items
from highest priority to lowest priority. This is opposite of the
normal heap ordering, which sorts from lowest to highest value.

The role of the `index` variable is to properly order items with
the same priority level. By keeping a constantly increasing index,
the items will be sorted according to the order in which they were inserted.
However, the index also serves an important role in making
the comparison operations work for items that have the same priority level.

Instances of `Item` in the example can’t be ordered. For example:

    >>> a = Item('foo')
    >>> b = Item('bar')
    >>> a < b
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unorderable types: Item() < Item()

If you make `(priority, item)` tuples, they can be compared
as long as the priorities are different.
However, if two tuples with equal priorities are compared,
the comparison fails as before. For example:

    >>> a = (1, Item('foo'))
    >>> b = (5, Item('bar'))
    >>> a < b
    True
    >>> c = (1, Item('grok'))
    >>> a < c
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unorderable types: Item() < Item()

By introducing the extra index and making `(priority, index, item)` tuples,
you avoid this problem entirely since no two tuples will ever
have the same value for index (and Python never bothers to
compare the remaining tuple values once the result of comparison
can be determined)
'''
