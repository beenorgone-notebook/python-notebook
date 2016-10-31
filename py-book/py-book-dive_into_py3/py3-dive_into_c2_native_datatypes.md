# [Dive into Python 3: Native Datatypes](http://www.diveintopython3.net/native-datatypes.html)

<!-- toc orderedList:0 -->

 - [Dive into Python 3: Native Datatypes](#dive-into-python-3-native-datatypeshttpwwwdiveintopython3netnative-datatypeshtml)

  - [Booleans](#booleans)
  - [Numbers](#numbers)
  - [Coercing Integers To Floats And Vice-Versa](#coercing-integers-to-floats-and-vice-versa)
  - [Common Numerical Operations](#common-numerical-operations)
  - [Fractions](#fractions)
  - [Trigonometry](#trigonometry)
  - [Numbers In A Boolean Context](#numbers-in-a-boolean-context)
  - [Lists](#lists)

    - [Creating a List](#creating-a-list)
    - [Slicing a List](#slicing-a-list)
    - [Adding Items To A List](#adding-items-to-a-list)
    - [Searching For Values In A List](#searching-for-values-in-a-list)
    - [Removing Items from a List](#removing-items-from-a-list)
    - [Lists In A Boolean Context](#lists-in-a-boolean-context)

  - [Tuples](#tuples)

    - [Tuples In A Boolean Context](#tuples-in-a-boolean-context)
    - [Assigning Multiple Values At Once](#assigning-multiple-values-at-once)

  - [Sets](#sets)

    - [Creating A Set](#creating-a-set)
    - [Modifying A Set](#modifying-a-set)
    - [Removing Items From A Set](#removing-items-from-a-set)
    - [Common Set Operations](#common-set-operations)
    - [Sets In A Boolean Context](#sets-in-a-boolean-context)

  - [Dictionaries](#dictionaries)

    - [Creating A Dictionary](#creating-a-dictionary)
    - [Modifying A Dictionary](#modifying-a-dictionary)
    - [Dictionaries In A Boolean Context](#dictionaries-in-a-boolean-context)

  - [None](#none)
  - [Further Reading](#further-reading)

<!-- tocstop -->

 Python has many native datatypes. Here are the important ones:

1. **Booleans** are either `True` or `False`.
2. **Numbers** can be integers (`1` and `2`), floats (`1.1` and `1.2`), fractions (`1/2` and `2/3`), or even complex numbers.
3. **Strings** are sequences of Unicode characters, e.g. an `html` document.
4. **Bytes** and **byte arrays**, e.g. a `jpeg` image file.
5. **Lists** are ordered sequences of values.
6. **Tuples** are ordered, immutable sequences of values.
7. **Dictionaries** are unordered bags of key-value pairs.
8. **Sets** are unordered bags of values.

## Booleans

Booleans are either true or false. Due to some legacy issues left over from Python 2, booleans can be treated as numbers. `True` is `1`; `False` is `0`.

```python
True + True
#2
True - False
#1
True * False
#0
True / False
#Traceback (most recent call last):
#  File "<pyshell#56>", line 1, in <module>
#    True / False
#ZeroDivisionError: division by zero
```

## Numbers

You can use the `type()` function to check the type of any value or variable.

Similarly, you can use the `isinstance()` function to check whether a value or variable is of a given type.

Adding an `int` to an `int` yields an `int`. Adding an `int` to a `float` yields a `float`. Python coerces the `int` into a `float` to perform the addition, then returns a `float` as the result.

## Coercing Integers To Floats And Vice-Versa

```python
float(2)
#2.0
int(2.0)
#2
int(2.5)
#2
int(-2.5)
#-2
1.12345678901234567890  
#1.1234567890123457
type(1000000000000000)  
#<class 'int'>
```

> Python 2 had separate types for `int` and `long`. The `int` datatype was limited by `sys.maxint`, which varied by platform but was usually `2^32-1`. Python 3 has just one integer type, which behaves mostly like the old `long` type from Python 2\. See pep 237 for details.

## Common Numerical Operations

> In Python 2, the `/` operator usually meant integer division, but you could make it behave like floating point division by including a special directive in your code. In Python 3, the `/` operator always means floating point division. See pep 238 for details.

```python
11 / 2
#5.5
11 // 2
#5
−11 // 2
#−6
11.0 // 2
#5.0
11 ** 2
#121
11 % 2
#1
```

## Fractions

```python
import fractions
x = fractions.Fraction(1, 3)
x
#Fraction(1, 3)
x * 2
#Fraction(2, 3)
fractions.Fraction(6, 4)
#Fraction(3, 2)
fractions.Fraction(0, 0)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "fractions.py", line 96, in __new__
#    raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
#ZeroDivisionError: Fraction(0, 0)
```

## Trigonometry

```python
import math
math.pi
#3.141592653589793
math.sin(math.pi / 2)
#1.0
math.tan(math.pi/4)
#0.9999999999999999
```

The math module has a constant for `π`, the ratio of a circle's circumference to its diameter.

The math module has all the basic trigonometric functions, including `sin()`, `cos()`, `tan()`, and variants like `asin()`.

**Note**: Python does not have infinite precision. `tan(π / 4)` should return `1.0`, not 0.99999999999999999.

## Numbers In A Boolean Context

Zero values are false, and non-zero values are true.

## Lists

> A list in Python is much more than an array in Java (although it can be used as one if that's really all you want out of life). A better analogy would be to the ArrayList class, which can hold arbitrary objects and can expand dynamically as new items are added.

### Creating a List

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

```python
a_list[-n] == a_list[len(a_list) - n]
```

### Slicing a List

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

### Adding Items To A List

There are four ways to add items to a list.

```python
a_list = ['a']
#a_list = a_list + [2.0, 3]    
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

1. The `+` operator concatenates lists to create a new list. A list can contain any number of items; there is no size limit (other than available memory). However, if memory is a concern, you should be aware that list concatenation creates a second list in memory. In this case, that new list is immediately assigned to the existing variable `a_list`. So this line of code is really a two-step process -- concatenation then assignment -- which can (temporarily) consume a lot of memory when you're dealing with large lists.
2. The `append()` method adds a single item to the end of the list.
3. Lists are implemented as classes. "Creating" a list is really instantiating a class. As such, a list has methods that operate on it. The `extend()` method takes one argument, a list, and appends each of the items of the argument to the original list.
4. The `insert()` method inserts a single item into a list. The first argument is the index of the first item in the list that will get bumped out of position.

A list can contain items of any datatype, and the items in a single list don't all need to be the same type. List items do not need to be unique.

The difference between `append()` and `extend()`.

```python
a_list = ['a', 'b', 'c']
a_list.extend(['d', 'e', 'f'])
a_list
#['a', 'b', 'c', 'd', 'e', 'f']
a_list.append(['g', 'h', 'i'])  
a_list
#['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i']]
```

### Searching For Values In A List

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

The `index()` method raises an exception if it doesn't find the value in the list. This is notably different from most languages, which will return some invalid index (like `-1`). While this may seem annoying at first, I think you will come to appreciate it. It means your program will crash at the source of the problem instead of failing strangely and silently later. Remember, `-1` is a valid list index. If the `index()` method returned `-1`, that could lead to some not-so-fun debugging sessions!

### Removing Items from a List

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

1. When called without arguments, the `pop()` list method removes the last item in the list and returns the value it removed.
2. You can pop arbitrary items from a list. Just pass a positional index to the `pop()` method. It will remove that item, shift all the items after it to "fill the gap," and return the value it removed.
3. Calling `pop()` on an empty list raises an exception.

### Lists In A Boolean Context

You can also use a list in a boolean context:

1. In a boolean context, an empty list is false.
2. Any list with at least one item is true.
3. Any list with at least one item is true. The value of the items is irrelevant.

## Tuples

A tuple is an immutable list. A tuple can not be changed in any way once it is created. In practical terms, tuples have no methods that would allow you to change (add, remove) them.

```python
a_tuple = ("a", "b", "mpilgrim", "z", "example")
```

So what are tuples good for?

1. Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with it is iterate through it, use a tuple instead of a list.
2. It makes your code safer if you "write-protect" data that doesn't need to be changed. Using a tuple instead of a list is like having an implied assert statement that shows this data is constant, and that special thought (and a specific function) is required to override that.
3. Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.

> Tuples can be converted into lists, and vice-versa. The built-in `tuple()` function takes a list and returns a tuple with the same elements, and the `list()` function takes a tuple and returns a list. In effect, `tuple()` freezes a list, and `list()` thaws a tuple.

### Tuples In A Boolean Context

```python
type((False))
#<class 'bool>
type((False,))
#<class 'tuple'>
```

1. In a boolean context, an empty tuple is false.
2. Any tuple with at least one item is true.
3. Any tuple with at least one item is true. The value of the items is irrelevant. But what's that comma doing there?
4. To create a tuple of one item, you need a comma after the value. Without the comma, Python just assumes you have an extra pair of parentheses, which is harmless, but it doesn't create a tuple.

### Assigning Multiple Values At Once

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

## Sets

A set is an unordered "bag" of unique values. A single set can contain values of any immutable datatype. Once you have two sets, you can do standard set operations like union, intersection, and set difference.

### Creating A Set

```python
a_set = {1}
a_set
#{1}
type(a_set)
#<class 'set'>
a_set = {1,2}
a_set
#{1, 2}
```

1. To create a set with one value, put the value in curly brackets
2. To create a set with multiple values, separate the values with commas and wrap it all up with curly brackets.
3. You can also create a set out of a list.

```python
a_list = ['a','b','mpilgrim',True,False,42]
a_set = set(a_list)
a_set
#{False, True, 42, 'b', 'a', 'mpilgrim'}
a_list
#['a', 'b', 'mpilgrim', True, False, 42]
```

You can create an empty set. Call `set()` with no arguments. Due to historical quirks carried over from Python 2, you can not create an empty set with two curly brackets. This actually creates an empty dictionary, not an empty set.

```python
a_set = set()
a_set
#set()
type(a_set)
#<class 'set'>
not_sure = {}
type(not_sure)
#<class 'dict'>
not_sure
#{}
```

### Modifying A Set

There are two different ways to add values to an existing set: the `add()` method, and the `update()` method.

```python
a_set = {1, 2}
a_set.add(4)
#{1, 2, 4}
a_set.add(1)
a_set
#{1, 2, 4}
```

1. The `add()` method takes a single argument, which can be any datatype, and adds the given value to the set.
2. Sets are bags of _unique values_. If you try to add a value that already exists in the set, it will do nothing. It won't raise an error; it's just a no-op.

```python
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

### Removing Items From A Set

There are three ways to remove individual values from a set. The first two, `discard()` and `remove()`, have one subtle difference.

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
```

1. The `discard()` method takes a single value as an argument and removes that value from the set.
2. If you call the `discard()` method with a value that doesn't exist in the set, it does nothing. No error; it's just a no-op.
3. The `remove()` method also takes a single value as an argument, and it also removes that value from the set.
4. Here's the difference: if the value doesn't exist in the set, the `remove()` method raises a `KeyError` exception.

Like lists, sets have a `pop()` method.

```python
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
#KeyError: 'pop from an empty set'
```

1. The `pop()` method removes a single value from a set and returns the value. However, since sets are unordered, there is no "last" value in a set, so there is no way to control which value gets removed. It is completely arbitrary.
2. The `clear()` method removes all values from a set, leaving you with an empty set. This is equivalent to `a_set = set()`, which would create a new empty set and overwrite the previous value of the a_set variable.
3. Attempting to pop a value from an empty set will raise a `KeyError` exception.

### Common Set Operations

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
```

1. To test whether a value is a member of a set, use the `in` operator. This works the same as lists.
2. The `union()` method returns a new set containing all the elements that are in either set.
3. The `intersection()` method returns a new set containing all the elements that are in both sets.
4. The `difference()` method returns a new set containing all the elements that are in `a_set` but not `b_set`.
5. The `symmetric_difference()` method returns a new set containing all the elements that are in exactly one of the sets.

```python
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

### Sets In A Boolean Context

1. In a boolean context, an empty set is false.
2. Any set with at least one item is true.
3. Any set with at least one item is true. The value of the items is irrelevant.

## Dictionaries

A dictionary is an unordered set of key-value pairs. When you add a key to a dictionary, you must also add a value for that key. (You can always change the value later.) Python dictionaries are optimized for retrieving the value when you know the key, but not the other way around.

> A dictionary in Python is like a hash in Perl 5\. In Perl 5, variables that store hashes always start with a `%` character. In Python, variables can be named anything, and Python keeps track of the datatype internally.

### Creating A Dictionary

```python
a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
a_dict
#{'database': 'mysql', 'server': 'db.diveintopython3.org'}
a_dict['server']
#'db.diveintopython3.org'
a_dict['database']
#'mysql'
a_dict['db.diveintopython3.org']
#Traceback (most recent call last):
#  File "<pyshell#42>", line 1, in <module>
#    a_dict['db.diveintopython3.org']
#KeyError: 'db.diveintopython3.org'
```

### Modifying A Dictionary

```python
a_dict
#{'server': 'db.diveintopython3.org', 'database': 'mysql'}
a_dict['database'] = 'blog'
a_dict
#{'server': 'db.diveintopython3.org', 'database': 'blog'}
a_dict['user'] = 'mark'  
a_dict
#{'server': 'db.diveintopython3.org', 'user': 'mark', 'database': 'blog'}
a_dict['user'] = 'dora'
a_dict
#{'server': 'db.diveintopython3.org', 'user': 'dora', 'database': 'blog'}
```

Assigning a value to an existing dictionary key simply replaces the old value with the new one.

### Dictionaries In A Boolean Context

1. In a boolean context, an empty dictionary is false.
2. Any dictionary with at least one key-value pair is true.

## None

`None` is a special constant in Python. `None` is not the same as False. `None` is not `0`. `None` is not an empty string. Comparing `None` to anything other than `None` will always return `False`.

`None` is the only null value. It has its own datatype (`NoneType`). You can assign `None` to any variable, but you can not create other `NoneType` objects. All variables whose value is `None` are equal to each other.

In a boolean context, `None` is false and `not None` is true.

## Further Reading

- [Boolean operations](http://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Numeric types](http://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-long-complex)
- [Sequence types](http://docs.python.org/3/library/stdtypes.html#sequence-types-str-unicode-list-tuple-buffer-xrange)
- [Set types](http://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Mapping types](http://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [`fractions` module](http://docs.python.org/3/library/fractions.html)
- [`math` module](http://docs.python.org/3/library/math.html)
- [`pep` 237: Unifying Long Integers and Integers](http://www.python.org/dev/peps/pep-0237)
- [`pep` 238: Changing the Division Operator](http://www.python.org/dev/peps/pep-0238)
