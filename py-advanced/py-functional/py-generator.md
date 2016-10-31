# Advanced Generator

## Resources

Generators: The Final Frontier by David Beazley

## Mini-Reference

### Generator definition

```python
def generator():
    ...
    yield
    ...
    return result
```

### Generator instance operations

```python
gen = generator()
next(gen)                       # Advance to next yield
gen.send(item)                  # Send an item
gen.close()                     # Terminate
gen.throw(exc, val, tb)         # Raise exception
result = yield from gen         # Delegate
```

## Generator Delegate

`yield from gen` - Delegate to a subgenerator

```python
def generator():
    ...
    yield value
    ...
    return result

def func():
    result = yield from generator()
```

- Allows generators to call other generators
- Operations take place at the current yield
- Return value (if any) is returned

```python
def chain(x,y):
    yield from x
    yield from y

a = [1,2,3]
b = [4,5,6]
for x in chain(a, b):
    print(x, end=' ')
# 1 2 3 4 5 6

c = [7,8,9]
for x in chain(a, chain(b,c)):
    print(x, end=' ')
# 1 2 3 4 5 6 7 8 9
```
