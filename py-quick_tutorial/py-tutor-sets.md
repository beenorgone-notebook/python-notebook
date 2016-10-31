Python Quick References: Sets
=============================

**Contents:**

1.	Creating A Set
2.	Modifying A Set
3.	Removing Items From A Set
4.	Common Set Operations
5.	Sets In A Boolean Context

Creating A Set
--------------

A set is an unordered “bag” of unique values. A single set can contain values of any immutable datatype

```python
a_set = {1}
a_set
#{1}
type(a_set)
#<class 'set'>
a_set = {1,2}
a_set
#{1, 2}

a_list = ['a','b','mpilgrim',True,False,42]
a_set = set(a_list)
a_set
#{False, True, 42, 'b', 'a', 'mpilgrim'}
a_list
#['a', 'b', 'mpilgrim', True, False, 42]

#Use Set Comprehensions
{2**x for x in range(10)}
#{32, 1, 2, 4, 8, 64, 128, 256, 16, 512}

empty_set = set()
#you can not create an empty set with two curly brackets. This actually creates an empty dictionary, not an empty set.
not_sure = {}
type(not_sure)
#<class 'dict'>
```

Modifying A Set
---------------

```python
a_set = {1, 2}
a_set.add(4)
#{1, 2, 4}
a_set.add(1)
a_set
#{1, 2, 4}

a_set = {1, 2, 3}
a_set.update({2, 4, 6})
a_set
#{1, 2, 3, 4, 6}
a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})
a_set
#{1, 2, 3, 4, 5, 6, 8, 9, 13}
a_set.update([10, 20, 30])
a_set
#{1, 2, 3, 4, 5, 6, 8, 9, 10, 13, 20, 30}
```

Removing Items From A Set
-------------------------

```python
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
a_set
#{1, 3, 36, 6, 10, 45, 15, 21, 28}
a_set.discard(10)
a_set
#{1, 3, 36, 6, 45, 15, 21, 28}
a_set.discard()
#Traceback (most recent call last):
#  File "<pyshell#4>", line 1, in <module>
#    a_set.discard()
#TypeError: discard() takes exactly one argument (0 given)
a_set.discard(10)

a_set
#{1, 3, 36, 6, 45, 15, 21, 28}
a_set.remove(21)
a_set
#{1, 3, 36, 6, 45, 15, 28}
a_set.remove(21)
#Traceback (most recent call last):
#  File "<pyshell#9>", line 1, in <module>
#    a_set.remove(21)
#KeyError: 21

#Like lists, sets have a pop() method:
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
a_set
#{1, 3, 36, 6, 10, 45, 15, 21, 28}
a_set.pop()
#1
a_set.pop()
#3
a_set
#{36, 6, 10, 45, 15, 21, 28}
a_set.pop(3)
#Traceback (most recent call last):
#  File "<pyshell#15>", line 1, in <module>
#    a_set.pop(3)
#TypeError: pop() takes no arguments (1 given)

a_set.clear()
a_set
#set()
a_set.pop()
#Traceback (most recent call last):
#  File "<pyshell#18>", line 1, in <module>
#    a_set.pop()
#KeyError: 'pop from an empty set
```

Common Set Operations
---------------------

```python
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
30 in a_set
#True
31 in a_set
#False

b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.union(b_set)
#{1, 2, 195, 4, 5, 3, 6, 8, 9, 76, 12, 15, 17, 18, 21, 30, 51, 127}
b_set.union(a_set) == a_set.union(b_set)
#True

a_set.intersection(b_set)
#{9, 2, 21, 12, 5}
b_set.intersection(a_set) == a_set.intersection(b_set)
#True

a_set.difference(b_set)
#{195, 4, 76, 51, 30, 127}
b_set.difference(a_set)
#{1, 3, 6, 8, 15, 17, 18}
b_set.difference(a_set) == a_set.difference(b_set)
#False

a_set.symmetric_difference(b_set)
#{1, 3, 195, 6, 4, 8, 76, 15, 17, 18, 51, 30, 127}
b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set)
#True
#The `symmetric_difference()` method returns a new set containing all the elements that are in exactly one of the sets.

a_set = {1,2,3}
b_set = {1,2,3,4}
a_set.issubset(b_set)
#True
b_set.issubset(a_set)
#False
a_set.issubset(a_set)
#True
a_set.add(5)
a_set.issubset(b_set)
#False
b_set.issubset(a_set)
#False
```

Sets In A Boolean Context
-------------------------

1.	In a boolean context, an empty set is false.
2.	Any set with at least one item is true.
3.	Any set with at least one item is true. The value of the items is irrelevant.
