from cytoolz.curried import *
from cytoolz.itertoolz import *

# toolz.itertoolz.remove(predicate, seq)

# toolz.itertoolz.accumulate(binop, seq, initial=no_default)
# See also: itertools.accumulate()

# toolz.itertoolz.groupby(key, seq)
# See also: countby()
print(groupby(len, ['cat', 'mouse', 'dog']))
# {3: ['cat', 'dog'], 5: ['mouse']}

# toolz.merge_sorted(*seqs, **kwargs)
# Merge and sort a collection of sorted collections
# Work lazily
# The “key” function used to sort the input may be passed as a keyword.
print(list(merge_sorted([2, 3], [1, 3], key=lambda x: x // 3)))
# [2, 1, 3, 3]

# toolz.itertoolz.interleave(seqs, pass_exceptions=())
# Both the individual sequences and the sequence of sequences may be infinite
# Work lazily
print(list(interleave([[1, 2], [3, 4]])))  # [1, 3, 2, 4]

# toolz.itertoolz.unique(seq, key=None)

# toolz.itertoolz.isiterable(x)

# toolz.itertoolz.isdistinct(seq)

# toolz.itertoolz.take(n, seq)
print(list(take(2, [1, 2, 3, 4, 5])))  # [1, 2]
# See also: drop tail

# toolz.itertoolz.take_nth(n, seq)
# Take every nth item in seq
print(list(take_nth(2, [1, 2, 3, 4, 5, 6])))  # [1, 3, 5]

# toolz.itertoolz.drop(n, seq)
# The sequence following the first n elements
# See also: take tail
print(list(drop(2, [1, 2, 3, 4, 6])))  # [3, 4, 6]

# toolz.itertoolz.first(seq) - The 1st element in a sequence

# toolz.itertoolz.second(seq) - The 2nd element in a sequence

# toolz.itertoolz.nth(n, seq) - The nth element in a sequence

# toolz.itertoolz.last(seq) - The last element in a sequence

# toolz.itertoolz.get(ind, seq, default=no_default)
# Get element in a sequence or dict. See also: pluck()
print(get(1, 'ABC'))  # B
print(get([1, 2], 'ABC'))  # ('B', 'C')
phonebook = {'Alice': '555-1234',
             'Bob': '555-5678',
             'Charlie': '555-9999'}
print(get(['Alice', 'Bob'], phonebook))  # ('555-1234', '555-5678')

# toolz.itertoolz.concat(seqs)
# Concatenate zero or more iterables, any of which may be infinite.
# An infinite sequence will prevent the rest of the arguments from being
# included.
# See also: itertools.chain.from_iterable
print(list(concat([[], [1], [2, 3]])))  # [1, 2, 3]

# toolz.itertoolz.concatv(*seqs) - Variadic version of concat
# See also: itertools.chain
print(list(concatv([], ['a'], ['b', 'c'])))  # ['a', 'b', 'c']

# toolz.itertoolz.mapcat(func, seqs)
# Apply func to each sequence in seqs, concatenating results
print(list(mapcat(lambda s: [c.upper() for c in s],
                  [['a', 'b'], ['c', 'd', 'e']])))
# ['A', 'B', 'C', 'D', 'E']

# toolz.itertoolz.cons(el, seq)
# Add `el` to beginning of (possible infinite) sequence seq.
print(list(cons(1, [2, 3])))  # [1, 2, 3]

# toolz.itertoolz.interpose(el, seq)
# Introduce `el` between each pair of elements in seq
print(list(interpose('a', [1, 2, 3])))  # [1, 'a', 2, 'a', 3]

# toolz.itertoolz.frequencies(seq)
# Find number of occurences of each value in seq
# See also: countby() groupby()
print(frequencies(['cat', 'cat', 'ox', 'dog', 'pig', 'pig', 'cat']))
{'pig': 2, 'dog': 1, 'cat': 3, 'ox': 1}


# toolz.itertoolz.reduceby(key, binop, seq, init='__no__default__')
# Perform a simultaneous groupby and reduction. Equivalent to:
'''def reduction(group):
    return reduce(binop, group, init)

groups = groupby(key, seq)
result = valmap(reduction, groups)'''
# the former does not build the intermediate groups,
# so it operate in much less space. Suitable for larger datasets.

# toolz.itertoolz.iterate(func, x) - Return x, func(x), func(func(x)), ...

# toolz.itertoolz.sliding_window(n, seq)
# A sequence of overlapping subsequences
print(list(sliding_window(2, [1, 2, 3, 4])))  # [(1, 2), (2, 3), (3, 4)]
mean = lambda seq: sum(seq) / len(seq)
print(list(map(mean, sliding_window(2, [1, 2, 3, 4]))))  # [1.5, 2.5, 3.5]

# toolz.itertoolz.partition(n, seq, pad='__no__pad__')
# partition sequence into tuples of length n
# See also: partition_all()
print(list(partition(2, [1, 2, 3, 4])))  # [(1, 2), (3, 4)]
# If the length of `seq` is not evenly divisible by `n`
# the final tuple is dropped if pad is not specified,
# or filled to length n by pad:
print(list(partition(2, range(5))))  # [(0, 1), (2, 3)]
print(list(partition(2, range(5), pad=None)))
# [(0, 1), (2, 3), (4, None)]

# toolz.itertoolz.count(seq) - Count the number of items in seq
# Work lazily. See also: len()
# Not to be confused with itertools.count()

# toolz.itertoolz.pluck (ind, seqs, default='__no__default__')
# plucks an element or several elements from each item in a sequence.
# `pluck` maps `itertoolz.get` over a sequence and returns one
# or more elements of item in the sequence. Equivalent to:
#       map(curried.get(ind), seqs)
# See also: get map
data = [{'id': 1, 'name': 'Cheese'}, {'id': 2, 'name': 'Pies'}]
print(list(pluck('name', data)))  # ['Chees', 'Pies']
print(list(pluck([0, 1], [[1, 2, 3], [4, 5, 7]])))  # [(1, 2), (4, 5)]

# toolz.itertoolz.join(leftkey, leftseq, rightkey, rightseq, left_default='__no__default__', right_default='__no__default__')
# Join two sequences on common attributes
# This is a semi-streaming operation:
# - The LEFT sequence is fully evaluated and placed into memory.
# - The RIGHT sequence is evaluated lazily and so can be arbitrarily large.
# Specify outer joins with keyword arguments `left_default` and/or
# `right_default`.
friends = [('Alice', 'Edith'),
           ('Alice', 'Zhao'),
           ('Edith', 'Alice'),
           ('Zhao', 'Alice'),
           ('Zhao', 'Edith')]
cities = [('Alice', 'NYC'),
          ('Dan', 'Syndey'),
          ('Alice', 'Chicago'),
          ('Edith', 'Paris'),
          ('Edith', 'Berlin'),
          ('Zhao', 'Shanghai')]
# In what cities do people have friends?
result = join(second, friends, first, cities)
# or result = join(1, friends, 0, cities)
for ((a, b), (c, d)) in sorted(unique(result)):
    print((a, d))
'''('Alice', 'Berlin')
('Alice', 'Paris')
('Alice', 'Shanghai')
('Edith', 'Chicago')
('Edith', 'NYC')
('Zhao', 'Chicago')
('Zhao', 'NYC')
('Zhao', 'Berlin')
('Zhao', 'Paris')'''

identity = lambda x: x
print(list(join(identity, [1, 2, 3],
                identity, [1, 2, 4],
                left_default=None, right_default=None)))
# [(1, 1), (2, 2), (None, 4), (3, None)]


# toolz.itertoolz.tail(n, seq) - The last n elements of a sequence.
# See also: drop take

# toolz.itertoolz.diff(*seqs, **kwargs)
# Return those items that differ between sequences
# Accept `default` value and `key` function.
print(list(diff([1, 2, 3], [1, 2, 10, 100])))  # [(3, 10)]
print(list(diff([1, 2, 3], [1, 2, 10, 100], default=None)))
# [(3, 10), (None, 100)]
print(list(diff(['apples', 'bananas'], ['Apples', 'Oranges'], key=str.lower)))
# [('bananas', 'Oranges')]

# toolz.itertoolz.topk (k, seq, key=None)
# Find the k largest elements of a sequence.
# Work lazily in `n*log(k)` time. Accept `key` function.
# See also: heapq.nlargest()

# toolz.itertoolz.peek(seq) - Retrieve the next element of a sequence.
# Returns the 1st element and an iterable equivalent to the original sequence.
seq = range(5)
first, seq = peek(seq)
print(first, list(seq))  # 0 [0, 1, 2, 3, 4]

# toolz.itertoolz.random_sample(prob, seq, random_state=None)
# Return elements from a sequence with probability of prob
# Returns a lazy iterator of random items from seq.

# toolz.recipes.countby(key, seq)
# Count elements of a collection by a key function.
# See also: groupby
print(countby(len, ['cat', 'mouse', 'dog']))  # {3: 2, 5: 1}

# toolz.recipes.partitionby(func, seq)
# Partition a sequence according to a function.
# when traversing s, every time the output of func changes
# a new list is started and that
# and subsequent items are collected into that list.
# See also: groupby itertools.groupby
over_ten = lambda x: x > 10
print(list(partitionby(over_ten, [1, 2, 1, 99, 88, 33, -1, 2, 10, 3, 99])))
# [(1, 2, 1), (99, 88, 33), (-1, 2, 10, 3), (99,)]

# toolz.functoolz.identity(x) - Return x

# toolz.functoolz.thread_first (val, *forms)
# toolz.functoolz.thread_last (val, *forms)
# Thread value through a sequence of functions/forms
double = lambda x: 2 * x
inc = lambda x: x + 1
print(thread_first(1, inc, double))  # 4
print(thread_last(1, inc, double))  # 4
# If the function expects more than one input you can specify
# those inputs in a tuple. The value is used as the first input (with
# thread_first) or last input( with thread_last).
add = lambda x, y: x + y
powr = lambda x, y: x**y
print(thread_first(1, (add, 4), (pow, 2)))  # 25 -- pow(add(1, 4), 2)
print(thread_last(1, (add, 4), (pow, 2)))  # 32 -- pow(2, add(4, 1))
# in general:
# `thread_first(x, f, (g, y, z))` expand to `g(f(x), y, z)`
# `thread_last(x, f, (g, y, z))` expand to `g(y, z, f(x))`


# toolz.functoolz.memoize - Cache a function's result
# Trades memory for speed. Only use on pure functions.
# Can be used as a decorator
# Use the `cache` keyword to provide a dict-like object as an initial cache
@memoize(cache={(1, 2): 3})  #
def add(x, y):
    return x + y
# It's possible to provide a `key(args, kwargs)` function that
# calculates keys used for the cache, which receives an `args` tuple
# and `kwargs` dict as input.

# toolz.functoolz.compose(*funcs) - Compose functions to operate in series
# `compose(f, g, h)(x, y)` is equivalent to `f(g(h(x,y)))`
# See also: pipe()
print(compose(double, inc)(1))  # 4

# toolz.functoolz.pipe(data, *funcs)
# Pipe a value through a sequence of functions.
# `pipe(data, f, g, h)` is equivalent to `h(g(f(data)))`
# like pipes in UNIX: `$ cat data | f | g | h`
# See also: compose thread_first thread_last

# toolz.functoolz.complement(func)
# Convert a predicate function to its logical complement
iseven = lambda n: n % 2 == 0
isodd = complement(iseven)
print(iseven(2), isodd(2))  # True False

# class toolz.functoolz.juxt(*funcs) - juxtaposition
# Creates a function that calls several functions with the same arguments
print(juxt(inc, double)(10))  # (11, 20)
print(juxt([inc, double])(10))  # (11, 20)

# toolz.functoolz.do(func, x) - Run `func` on `x`, returns `x`
# Because the results of `func` are not returned,
# only the side effects of `func` are relevant.
# Logging functions can be made by composing `do` with a storage function
# like `list.append` or `file.write`
log = []
inc = compose(inc, do(log.append))
# must use: from cytoolz.curried import do
print(inc(1), log)  # 2 [1]
print(inc(11), log)  # 12 [1, 11]


# class toolz.functoolz.curry(*args, **kwargs)
# Curry a callable function. Work as a decorator.
# Supports keyword arguments
# See also: http://toolz.readthedocs.org/en/latest/curry.html
@curry
def f(x, y, a=10): return a * (x + y)
add = f(a=1)
print(add(2, 3))  # 5

# toolz.functoolz.flip - Call the function call with the arguments flipped
# Curried.
div = lambda a, b: a / b
print(flip(div, 2, 1))  # 0.5
div_by_two = flip(div, 2)
print(div_by_two(4))  # 2
# Particularly useful for built in functions and
# functions defined in C extensions that accept positional only arguments.
# For example: isinstance, issubclass.
data = [1, 'a', 'b', 2, 1.5, object(), 3]
only_ints = list(filter(flip(isinstance, int), data))
print(only_ints)  # [1, 2, 3]

# class toolz.functoolz.excepts(exc, func, handler=<function return_none>)
# A wrapper to make `func` catch exceptions and dispatch to a handler.
excepting = excepts(
    ValueError,
    lambda a: [1, 2].index(a),
    lambda _: -1,
)
print(excepting(3))  # -1

# toolz.dicttoolz.merge(*dicts, **kwargs)
# Merge a collection of dictionaries.
print(merge({1: 'one', 2: 'two'}))  # {1: 'one', 2: 'two'}
# Later dictionaries have precedence.
print(merge({1: 2, 3: 4}, {3: 3, 4: 4}))  # {1: 2, 3: 3, 4: 4}
# See also: merge_with

# toolz.dicttoolz.merge_with(func, *dicts, **kwargs)
# Merge dictionaries and apply function to combined values.
print(merge_with(sum, {1: 1, 2: 2}, {1: 10, 2: 20}))
# {1: 11, 2: 22}
print(merge_with(double, {1: 1, 2: 2}, {2: 20, 3: 30}))
# {1: [1, 1], 2: [2, 20, 2, 20], 3: [30, 30]}

# toolz.dicttoolz.valmap(func, d, factory=<type 'dict'>)
# Apply function to values of dictionary.

# toolz.dicttoolz.keymap(func, d, factory=<type 'dict'>)
# Apply function to keys of dictionary

# toolz.dicttoolz.itemmap(func, d, factory=<type 'dict'>)
# Apply function to items of dictionary.

# toolz.dicttoolz.valfilter(predicate, d, factory=<type 'dict'>)
# Filter items in dictionary by value.

# toolz.dicttoolz.keyfilter(predicate, d, factory=<type 'dict'>)
# Filter items in dictionary by key.

# toolz.dicttoolz.itemfilter(predicate, d, factory=<type 'dict'>)
# Filter items in dictionary by item.

# toolz.dicttoolz.assoc(d, key, value, factory=<type 'dict'>)
# Return a new dict with new key value pair.
# Does not modify the initial dictionary.

# toolz.dicttoolz.dissoc(d, *keys)
# Return a new dict with the given key(s) removed.
print(dissoc({'x': 1}, 'y'))  # {'x': 1} -- Ignores missing keys

# toolz.dicttoolz.assoc_in(d, keys, value, factory=<type 'dict'>)
# Return a new dict with new, potentially nested, key value pair.
purchase = {'name': 'Alice',
            'order': {'items': ['Apple', 'Orange'],
                      'costs': [0.50, 1.25]},
            'credit card': '5555-1234-1234-1234'}
print(assoc_in(purchase, ['order', 'costs'], [0.25, 1.00]))
'''{'credit card': '5555-1234-1234-1234', 'name': 'Alice',
    'order': {'costs': [0.25, 1.00],
                 'items': ['Apple', 'Orange']}}'''

# toolz.dicttoolz.update_in(d, keys, func, default=None, factory=<type 'dict'>)
# Update value in a (potentially) nested dictionary.
# `d` - dictionary on which to operate
# `keys` - list or tuple giving the location of the value to be changed in `d`
# `func` - function to operate on that value
print(update_in({'a': 0}, ['a'], inc))  # {'a', 1}
transaction = {'name': 'Alice',
               'purchase': {'items': ['Apple', 'Orange'],
                            'costs': [0.50, 1.25]},
               'credit card': '5555-1234-1234-1234'}
print(update_in(transaction, ['purchase', 'costs'], sum))
'''{'name': 'Alice',
    'purchase': {'costs': 1.75, 'items': ['Apple', 'Orange']},
    'credit card': '5555-1234-1234-1234'}'''
# updating a value when k0 is not in d
print(update_in({}, [1, 2, 3], str, default="bar"))
# {1: {2: {3: 'bar'}}}
print(update_in({1: 'foo'}, [2, 3, 4], inc, 0))
# {1: 'foo', 2: {3: {4: 1}}}

# toolz.dicttoolz.get_in(keys, coll, default=None, no_default=False)
# Returns `coll[i0][i1]...[iX]` where `[i0, i1, ..., iX]==keys`.
# If coll[i0][i1]...[iX] cannot be found, returns default, unless
# `no_default` is specified, then it raises KeyError or IndexError.
# `get_in` is a generalization of`operator.getitem`
# for nested data structures such as lists and dictionaries.
# See also: itertoolz.get operator.getitem
print(get_in(['purchase', 'items', 0], transaction))  # Apple
print(get_in(['name'], transaction))  # Alice
print(get_in(['purchase', 'total'], transaction))  # None
print(get_in(['purchase', 'items', 10], transaction))  # None
print(get_in(['purchase', 'total'], transaction, default=0))  # 0

# class toolz.sandbox.core.EqualityHashKey(key, item)
# Create a hash key that uses equality comparisons between items.
