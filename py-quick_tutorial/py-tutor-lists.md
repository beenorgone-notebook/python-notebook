Python List: Methods
====================

**Contents:**

1.	Creating a List
2.	Slicing a List
3.	Adding Items To A List
4.	Searching For Values In A List
5.	Removing Items from a List
6.	Lists In A Boolean Context

Creating a List
---------------

```python
a_list = ['a', 'b', 'mpilgrim', 'z', 'example']  
a_list
#['a', 'b', 'mpilgrim', 'z', 'example']
a_list[0]
#'a'
a_list[4]
#'example'
a_list[-1]
#'example'
a_list[-3]
#'mpilgrim'
```

`a_list[-n] == a_list[len(a_list) - n]`

Use List Comprehensions

```python
a_list = [1, 9, 8, 4]
[i * 2 for i in a_list]
#[2, 18, 16, 8]
a_list
#[1, 9, 8, 4]
#A list comprehension creates a new list; it does not change the original list.
```

Use `list()`:

```python
list('abc')
#['a', 'b', 'c']
a_dict = {'a':1}
list(a_dict)
#['a']
```

Slicing a List
--------------

```python
a_list
#['a', 'b', 'mpilgrim', 'z', 'example']
a_list[1:3]
#['b', 'mpilgrim']
a_list[1:-1]
#['b', 'mpilgrim', 'z']
a_list[0:3]
#['a', 'b', 'mpilgrim'] # the 1st three items of the list, starting at `a_list[0]`, up to but not including `a_list[3]`
a_list[:3]
#['a', 'b', 'mpilgrim']
a_list[3:]
#['z', 'example']
a_list[:]
#['a', 'b', 'mpilgrim', 'z', 'example']
```

Adding Items To A List
----------------------

```python
a_list = ['a']
#a_list = a_list + [2.0, 3]
#Don't use it with large list
a_list
#['a', 2.0, 3]
a_list.append(True)
a_list
#['a', 2.0, 3, True]
a_list.extend(['four', 'Ω'])
a_list
#['a', 2.0, 3, True, 'four', 'Ω']
a_list.insert(0, 'Ω')
a_list
#['Ω', 'a', 2.0, 3, True, 'four', 'Ω']
```

Searching For Values In A List
------------------------------

```python
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
a_list.count('new')
#2
'new' in a_list
#True
'c' in a_list
#False
a_list.index('mpilgrim')
#3
a_list.index('new')
#2
a_list.index('c')
#Traceback (most recent call last):
#  File "<pyshell#84>", line 1, in <module>
#    a_list.index('c')
#ValueError: 'c' is not in list
```

Removing Items from a List
--------------------------

If you know item's index, use `del`.

```python
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
del a_list[1]
a_list
#['a', 'new', 'mpilgrim', 'new']
a_list[1]
#'new'
```

Don't know the positional index? You can remove items by value.

```python
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
a_list.remove('new')
a_list
#['a', 'b', 'mpilgrim', 'new']
a_list.remove('new')
#['a', 'b', 'mpilgrim']
a_list.remove('new')
#Traceback (most recent call last):
#  File "<pyshell#95>", line 1, in <module>
#    a_list.remove('new')
#ValueError: list.remove(x): x not in list
```

The `pop()` method is yet another way to remove items from a list, but with a twist.

```python
a_list = ['a', 'b', 'new', 'mpilgrim']
a_list.pop()
#'mpilgrim'
a_list
#['a', 'b', 'new']
a_list.pop(1)
#'b'
a_list
#['a', 'new']
a_list.pop()
#'new'
a_list.pop()
#'a'
a_list.pop()
#Traceback (most recent call last):
#  File "<pyshell#103>", line 1, in <module>
#    a_list.pop()
#IndexError: pop from empty list
```

Lists In A Boolean Context
--------------------------

-	In a boolean context, an empty list is false.
-	Any list with at least one item is true.
-	Any list with at least one item is true. The value of the items is irrelevant.
