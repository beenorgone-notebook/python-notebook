# Functional Programming in Python by David Mertz - Chap IV: Higher-Order Functions

<!-- toc orderedList:0 -->

 - [Functional Programming in Python by David Mertz - Chap IV: Higher-Order Functions](#functional-programming-in-python-by-david-mertz-chap-iv-higher-order-functions)

<!-- tocstop -->

 ## Basic higher-order functions (HOFs):

`map()`, `filter()`, `functools.reduce()`, `functools.partial()`, ...

```python
# map() and filter() are also a special cases of reduce().
add5 = lambda n: n + 5
reduce(lambda l, x: l + [add5(x)], range(10), [])
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# simpler: map(add5, range(10))

isOdd = lambda n: n % 2
reduce(lambda l, x: l + [x] if isOdd(x) else l, range(10), [])
# [1, 3, 5, 7, 9]
# simpler: filter(isOdd, range(10))
```

## Utility HOFs

```python
def compose(*funcs):
    """Return a new function s.t.
        compose(f,g,...)(x) == f(g(...(x)))"""
    def inner(data, funcs=funcs):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner
```
