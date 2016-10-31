Python Quick References: Tuples
===============================

**Contents:**

1.	Tuples
2.	Tuples In A Boolean Context
3.	Assigning Multiple Values At Once

Tuples
------

A tuple is an immutable list. A tuple can not be changed in any way once it is created. In practical terms, tuples have no methods that would allow you to change (add, remove) them.

To make a tuple:

```python
a_tuple = ("a", "b", "mpilgrim", "z", "example")

other_tuple = tuple(["a", "b", "mpilgrim", "z", "example"])
tuple('bac')
#('b', 'a', 'c')

an_one_item_tuple = ('a',)
#To create a tuple of one item, you need a comma after the value.
```

So what are tuples good for?

1.	**Tuples are faster than lists**. If you’re defining a constant set of values and all you’re ever going to do with it is iterate through it, use a tuple instead of a list.
2.	**It makes your code safer if you “write-protect” data that doesn’t need to be changed.** Using a tuple instead of a list is like having an implied assert statement that shows this data is constant, and that special thought (and a specific function) is required to override that.
3.	**Some tuples can be used as dictionary keys** (specifically, tuples that contain immutable values like strings, numbers, and other tuples). **Lists can never be used as dictionary keys, because lists are not immutable.**

Tuples In A Boolean Context
---------------------------

1.	In a boolean context, an empty tuple is false.
2.	Any tuple with at least one item is true.

Assigning Multiple Values At Once
---------------------------------

in Python, you can use a tuple to assign multiple values at once.

```python
v = ('a', 2, True)
(x, y, z) = v
x
#'a'
y
#2
z
#True

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)  
MONDAY
#0
TUESDAY
#1
SUNDAY
#6
```
