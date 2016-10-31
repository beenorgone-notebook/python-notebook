# Functional Programming in Python - Chap III: Lazy Evaluation

<!-- toc orderedList:0 -->

 - [Functional Programming in Python - Chap III: Lazy Evaluation](#functional-programming-in-python-chap-iii-lazy-evaluation)

<!-- tocstop -->

 ## `itertools` and `more_itertools` modules

`itertools`:

- `zip()`, `map()`, `filter()`, `range()`, `count()`, `tee()`, `accumulate()`, ...
- Chaining Iterables: `chain()`, `chain.from_iterable()`, ...
- ...

### `more_itertools` module

```python
import more_itertools

# more_itertools.chunked(iterable, n)
# Break an iterable into lists of a given length:
list(more_itertools.chunked(range(7), 3))
# [[0, 1, 2], [3, 4, 5], [6]]

# more_itertools.collate(*iterables, key=lambda a: a, reverse=False)
# Return a sorted merge of the items from each of several already-sorted iterables.
list(more_itertools.collate('ACDZ', 'AZ', 'JKL'))
# ['A', 'A', 'C', 'D', 'J', 'K', 'L', 'Z', 'Z']

# more_itertools.consumer(func)
# Coroutine decorator

# more_itertools.first(iterable, [,default])
# Return the 1st item of an iterable, `default` if there is none.
# If default is not provided and there are no items in the iterable,
# raise ValueError.
more_itertools.first(xrange(4))
# 0
more_itertools.first(xrange(0), -1)
# -1

# more_itertools.ilen(iterable)
# Return the number of items in iterable. It consumes the iterable.

# more_itertools.iterate(func, start)
# return `start`, `func(start)`, `func(func(start))`, ...
from itertools import islice
list(islice(more_itertools.iterate(lambda x: 2*x, 1), 10))
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# class more_itertools.peekable(iterable)
# Wrapper for an iterator to allow 1-item lookahead
p = more_itertools.peekable(xrange(2))
p.peek()  # 0
p.next()  # 0
# Pass peek() a default value, and
# it will be returned in the case where the iterator is exhausted:
p = peekable([])
p.peek('hi')
# 'hi'

# more_itertools.with_iter(context_manager)
# Wrap an iterable in a `with` statement, so it closes once exhausted.
# Any context manager which returns an iterable is a candidate for `with_iter`
upper_lines = (line.upper() for line in more_itertools.with_iter(open('foo')))

# more_itertools.take(n, iterable)
# Return 1st n items of the iterable as a list.
more_itertools.take(3, range(10))  # [0, 1, 2]
more_itertools.take(5, range(3))  # [0, 1, 2]
# Effectively a short replacement for next based iterator consumption
# when you want more than one item, but less than the whole iterator.

# more_itertools.tabulate(func, start=0)
# Return an iterator mapping the function over linear input.
# The start argument will be increased by 1 each time
# the iterator is called and fed into the function.
t = tabulate(lambda x: x**2, -3)
more.itertools.take(4, t)  # [9, 4, 1, 0]
more_itertools.take(10, t)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# more_itertools.consume(iterator, n=None)
# Advance the iterator n-steps ahead. If n is None, consume entirely.

# more_itertools.nth(iterable, n, default=None)
# Returns the nth item or a default value.

# more_itertools.quantify(iterable, pred=<type 'bool'>)
# Return the how many times the predicate is true
more_itertools.quantify([True, False, True])  # 2

# more_itertools.padnone(iterable)
# Returns the sequence of elements and then returns None indefinitely.
# Useful for emulating the behavior of the built-in map() function.
more_itertools.take(5, more_itertools.padnone(range(3)))
# [0, 1, 2, None, None]

# more_itertools.ncycles(iterable, n)
# Returns the sequence elements n times
list(more_itertools.ncycles(['a', 'b'], 3))
# ['a', 'b', 'a', 'b', 'a', 'b']

# more_itertools.dotproduct(vec1, vec2)
# Returns the dot product of the two iterables
more_itertools.dotproduct([10, 10], [20, 20])
# 400

# more_itertools.flatten(listOfLists)
# Return an iterator flattening one level of nesting in a a list of lists
list([flatten([[0,1], [2,3]]))  # [0, 1, 2, 3]

....
```
