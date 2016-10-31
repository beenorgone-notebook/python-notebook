# Functional Programming in Python by David Mertz - Chap I: (Avoiding) Flow Control

<!-- toc orderedList:0 -->

- [Functional Programming in Python by David Mertz - Chap I: (Avoiding) Flow Control](#functional-programming-in-python-by-david-mertz-chap-i-avoiding-flow-control)
	- [Encapsulation](#encapsulation)
	- [Comprehensions & Generators](#comprehensions-generators)
	- [Recursion](#recursion)
	- [Eliminating Loops](#eliminating-loops)
		- [Eliminating `for` loops](#eliminating-for-loops)
	- [Eliminating `while` loops](#eliminating-while-loops)
	- [Eliminating Recursion](#eliminating-recursion)

<!-- tocstop -->

 Imperative style:

- Based on:

  - classes and methods
  - `for` or `while` loops,
  - assignment of state variables within those loops,
  - modification of data structures
  - branch statements (`if`/`else`/`elif` or `try`/`except`/`finally`)

- Natural and easy to reason about.

- Problem:

  - side effect (come with state variables and mutable data structures)
  - difficult to reason accurately about what state data is in a given point in a program.

- One solution: focus on describing "what" a data collections consist of. Ask yourself: "Here's some data, what do I need to do with it?"

## Encapsulation

Put the data construction in a more isolated place--i.e., in a function or method.

```python
# Imperative way:
# configure the data to start with
collection = get_initial_state()
state_var = None
for datum in data_set:
    if condition(state_var):
        state_var = calculate_from(datum)
        new = modify(datum, state_var)
        collection.add_to(new)
    else:
        new = modify_differently(datum)
        collection.add_to(new)

# Now actually work with the data
for thing in collection:
    process(thing)

# Functional version:
# tuck away construction of data
def make_collection(data_set):
    collection = get_initial_state()
    state_var = None
    for datum in data_set:
        if condition(state_var):
            state_var = calculate_from(datum, state_var)
            new = modify(datum, state_var)
            collection.add_to(new)
        else:
        new = modify_differently(datum)
        collection.add_to(new)
    return collection

# Now actually work with the data
for thing in make_collection(data_set):
    process(thing)
```

The focus shifted from "How do we construct `collection`" to "What does `make_collection` create?"

## Comprehensions & Generators

```python
# Imperative way:
collection = list()
for datum in data_set:
    if condition(datum):
        collection.append(datum)
    else:
        new = modify(datum)
        collection.append(new)

# Somewhat more compactly we could write this as:
collection = [d if condition(d) else modify(d) for d in data_set]
```

The focus shifted from "What is the state of `collection` at this point in the loop" to thinking of what `collection` is.

## Recursion

- little to recommend this approach in Python
- Python lacks an internal feature called _tail call elimination_
- Good practice: when a problem offers itself to a "divide and conquer" on two halves of larger collection. In that case, the recursion depth is only `O(log N)` of the size of the collection. ex: Quick sort algorithms
- Not good: use recursion merely for "iteration by other means".

```python
def quicksort(lst):
    "Quicksort over a list-like sequence"
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    pivots = [x for x in lst if x == pivot]
    smaller = quicksort([x for x in lst if x < pivot])
    larger = quicksort([x for x in lst if x > pivot])
    return smaller + pivots + larger
```

## Eliminating Loops

### Eliminating `for` loops

use `map()`-based "loop": `map(func, it)` instead of statement-based "loop".

## Eliminating `while` loops

```python
# statement-based while loop
while <cond>:
    <pre-suite>
    if <break_condition>:
        break
    else:

# FP-style recursive while loop
def while_block():
    <pre-suite>
    if <break_condition>:
        return 1
    else:
        <suite>
    return 0

while_FP = lambda: (<cond> and while_block()) or while_FP()
while_FP()
```

```python
# imperative version of "echo()"
def echo_IMP():
    while 1:
        x = input("IMP -- ")
        if x == 'quit':
            break
        else:
            print(x)

echo_IMP()

# Now let’s remove the while loop for the functional version:
# FP version of "echo()"
def identity_print(x):  # "identity with side-effect"
    print(x)
    return x

echo_FP = lambda: identity_print(input("FP -- "))=='quit' or echo_FP()

echo_FP()
```

## Eliminating Recursion

Perform "recursion without recursion" by using `functools.reduce()` or other *folding* operations.
