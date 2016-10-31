# Special Method Names

<http://www.diveintopython3.net/special-method-names.html>

<!-- toc orderedList:0 -->

- [Special Method Names](#special-method-names)
	- [Basics](#basics)
	- [Classes That Act Like Iterators](#classes-that-act-like-iterators)
	- [Computed Attributes](#computed-attributes)
	- [Classes That Act Like Functions](#classes-that-act-like-functions)
	- [Classes That Act Like Sets](#classes-that-act-like-sets)
	- [Classes That Act Like Dictionaries](#classes-that-act-like-dictionaries)
	- [Classes That Act Like Numbers](#classes-that-act-like-numbers)
	- [Classes That Can Be Compared](#classes-that-can-be-compared)
	- [Classes That Can Be Serialized](#classes-that-can-be-serialized)
	- [Classes That Can Be Used in a `with` Block](#classes-that-can-be-used-in-a-with-block)

<!-- tocstop -->

 ## Basics

You Want...                               | So You Write...          | And Python Calls...
----------------------------------------- | ------------------------ | ---------------------------
to initialize an instance                 | `x = MyClass()`          | `x.__init__()`
the "official" representation as a string | `repr(x)`                | `x.__repr__()`
the "informal" value as a string          | `str(x)`                 | `x.__str__()`
the "informal" value as a byte array      | `bytes(x)`               | `x.__bytes__()`
the value as a formatted string           | `format(x, format_spec)` | `x.__format__(format_spec)`

- The `__init__()` method is called after the instance is created. If you want to control the actual creation process, use the `__new__()` method.
- The `__str__()` method is also called when you `print(x)`.
- By convention, the `__repr__()` method should return a string that is a valid Python expression.

## Classes That Act Like Iterators

You Want...                            | So You Write... | And Python Calls...
-------------------------------------- | --------------- | --------------------
to iterate through a sequence          | `iter(seq)`     | `seq.__iter__()`
to get the next value from an iterator | `next(seq)`     | `seq.__next__()`
to create an iterator in reverse order | `reversed(seq)` | `seq.__reversed__()`

1. The `__iter__()` method is called whenever you create a new iterator. It's a good place to initialize the iterator with initial values.
2. The `__next__()` method is called whenever you retrieve the next value from an iterator.
3. The `__reversed__()` method is uncommon. It takes an existing sequence and returns an iterator that yields the items in the sequence in reverse order, from last to first.

a for loop can act on an iterator. In this loop:

```python
for x in seq:
    print(x)
```

Python 3 will call `seq.__iter__()` to create an iterator, then call the `__next__()` method on that iterator to get each value of x. When the `__next__()` method raises a `StopIteration` exception, the `for` loop ends gracefully.

## Computed Attributes

You Want...                                   | So You Write...         | And Python Calls...
--------------------------------------------- | ----------------------- | -------------------------------------
to get a computed attribute (unconditionally) | `x.my_property`         | `x.__getattribute__('my_property')`
to get a computed attribute (fallback)        | `x.my_property`         | `x.__getattr__('my_property')`
to set an attribute                           | `x.my_property = value` | `x.__setattr__('my_property', value)`
to delete an attribute                        | `del x.my_property`     | `x.__delattr__('my_property')`
to list all attributes and methods            | `dir(x)`                | `x.__dir__()`

1. If your class defines a `__getattribute__()` method, Python will call it on every reference to any attribute or method name (except special method names, since that would cause an unpleasant infinite loop).
2. If your class defines a `__getattr__()` method, Python will call it only after looking for the attribute in all the normal places. If an instance `x` defines an attribute color, `x.color` will not call `x.__getattr__('color')`; it will simply return the already-defined value of `x.color`.
3. The `__setattr__()` method is called whenever you assign a value to an attribute.
4. The `__delattr__()` method is called whenever you delete an attribute.
5. The `__dir__()` method is useful if you define a `__getattr__()` or `__getattribute__()` method. Normally, calling `dir(x)` would only list the regular attributes and methods. If your `__getattr__()` method handles a color attribute dynamically, `dir(x)` would not list color as one of the available attributes. Overriding the `__dir__()` method allows you to list color as an available attribute, which is helpful for other people who wish to use your class without digging into the internals of it.

The distinction between the `__getattr__()` and `__getattribute__()` methods is subtle but important. Here are examples:

```python
class Dynamo:
    def __getattr__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError

dyn = Dynamo()
dyn.color
#'PapayaWhip'
dyn.color = 'LemonChiffon'
dyn.color
#'LemonChiffon'

dyn.shape = 'a'
dyn.shape
#'a'
```

```python
class SuperDynamo:
    def __getattribute__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError

dyn = SuperDynamo()
dyn.color
#'PapayaWhip'
dyn.color = 'LemonChiffon'
dyn.color
#'PapayaWhip'

dyn.shape = 'a'
dyn.shape
'''Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    dyn.shape
  File "<pyshell#9>", line 6, in __getattribute__
    raise AttributeError
AttributeError'''
```

Even after explicitly setting `dyn.color`, the `__getattribute__()` method is still called to provide a value for `dyn.color`. If present, the `__getattribute__()` method is called unconditionally for every attribute and method lookup, even for attributes that you explicitly set after creating an instance.

> If your class defines a `__getattribute__()` method, you probably also want to define a `__setattr__()` method and coordinate between them to keep track of attribute values. Otherwise, any attributes you set after creating an instance will disappear into a black hole.

> You need to be extra careful with the `__getattribute__()` method, because it is also called when Python looks up a method name on your class.

```python
class Rastan:
    def __getattribute__(self, key):
        raise AttributeError
    def swim(self):
        pass

hero = Rastan()
hero.swim()
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in __getattribute__
AttributeError'''
```

When you call `hero.swim()`, Python looks for a `swim()` method in the Rastan class. This lookup goes through the `__getattribute__()` method, because all attribute and method lookups go through the `__getattribute__()` method. In this case, the `__getattribute__()` method raises an `AttributeError` exception, so the method lookup fails, so the method call fails.

## Classes That Act Like Functions

You can make an instance of a class callable -- exactly like a function is callable -- by defining the `__call__()` method.

## Classes That Act Like Sets

If your class acts as a container for a set of values -- that is, if it makes sense to ask whether your class "contains" a value -- then it should probably define the following special methods that make it act like a set.

You Want...                                  | So You Write... | And Python Calls...
-------------------------------------------- | --------------- | -------------------
the number of items                          | `len(s)`        | `s.__len__()`
to know whether it contains a specific value | `x in s`        | `s.__contains__(x)`

## Classes That Act Like Dictionaries

Extending the previous section a bit, you can define classes that not only respond to the "in" operator and the len() function, but they act like full-blown dictionaries, returning values based on keys.

You Want...                                 | So You Write...      | And Python Calls...
------------------------------------------- | -------------------- | --------------------------------
to get a value by its key                   | `x[key]`             | `x.__getitem__(key)`
to set a value by its key                   | `x[key] = value`     | `x.__setitem__(key, value)`
to delete a key-value pair                  | `del x[key]`         | `x.__delitem__(key)`
to provide a default value for missing keys | `x[nonexistent_key]` | `x.__missing__(nonexistent_key)`

## Classes That Act Like Numbers

Tell `x` to special methods:

You Want...             | So You Write... | And Python Calls...
----------------------- | --------------- | -------------------
addition                | `x + y`         | `x.__add__(y)`
subtraction             | `x - y`         | `x.__sub__(y)`
multiplication          | `x * y`         | `x.__mul__(y)`
division                | `x / y`         | `x.__truediv__(y)`
floor division          | `x // y`        | `x.__floordiv__(y)`
modulo (remainder)      | `x % y`         | `x.__mod__(y)`
floor division & modulo | `divmod(x, y)`  | `x.__divmod__(y)`
raise to power          | `x ** y`        | `x.__pow__(y)`
left bit-shift          | `x << y`        | `x.__lshift__(y)`
right bit-shift         | `x >> y`        | `x.__rshift__(y)`
bitwise and             | `x & y`         | `x.__and__(y)`
bitwise xor             | `x ^ y`         | `x.__xor__(y)`
bitwise or              |                 | `x.__or__(y)`

Tell `y` to special methods:

You Want...             | So You Write... | And Python Calls...
----------------------- | --------------- | --------------------
addition                | `x + y`         | `x.__radd__(y)`
subtraction             | `x - y`         | `x.__rsub__(y)`
multiplication          | `x * y`         | `x.__rmul__(y)`
division                | `x / y`         | `x.__rtruediv__(y)`
floor division          | `x // y`        | `x.__rfloordiv__(y)`
modulo (remainder)      | `x % y`         | `x.__rmod__(y)`
floor division & modulo | `divmod(x, y)`  | `x.__rdivmod__(y)`
raise to power          | `x ** y`        | `x.__rpow__(y)`
left bit-shift          | `x << y`        | `x.__rlshift__(y)`
right bit-shift         | `x >> y`        | `x.__rrshift__(y)`
bitwise and             | `x & y`         | `x.__rand__(y)`
bitwise xor             | `x ^ y`         | `x.__rxor__(y)`
bitwise or              |                 | `x.__ror__(y)`

If you're doing "in-place" operations, like `x /= 3`, there are even more special methods you can define.

You Want...                      | So You Write... | And Python Calls...
-------------------------------- | --------------- | --------------------
in-place addition                | `x + y`         | `x.__iadd__(y)`
in-place subtraction             | `x - y`         | `x.__isub__(y)`
in-place multiplication          | `x * y`         | `x.__imul__(y)`
in-place division                | `x / y`         | `x.__itruediv__(y)`
in-place floor division          | `x // y`        | `x.__ifloordiv__(y)`
in-place modulo (remainder)      | `x % y`         | `x.__imod__(y)`
in-place floor division & modulo | `divmod(x, y)`  | `x.__idivmod__(y)`
in-place raise to power          | `x ** y`        | `x.__ipow__(y)`
in-place left bit-shift          | `x << y`        | `x.__ilshift__(y)`
in-place right bit-shift         | `x >> y`        | `x.__irshift__(y)`
in-place bitwise and             | `x & y`         | `x.__iand__(y)`
in-place bitwise xor             | `x ^ y`         | `x.__ixor__(y)`
in-place bitwise or              |                 | `x.__ior__(y)`

Some more:

You Want...                            | So You Write... | And Python Calls...
-------------------------------------- | --------------- | -----------------------
negative number                        | `-x`            | `x.__neg__()`
positive number                        | `+x`            | `x.__pos__()`
absolute value                         | `abs(x)`        | `x.__abs__()`
inverse                                | `~x`            | `x.__invert__()`
complex number                         | `complex(x)`    | `x.__complex__()`
integer                                | `int(x)`        | `x.__int__()`
floating point number                  | `float(x)`      | `x.__float__()`
number rounded to nearest integer      | `round(x)`      | `x.__round__()`
number rounded to nearest n digits     | `round(x, n)`   | `x.__round__(n)`
smallest integer >= x                  | `math.ceil(x)`  | `x.__ceil__()`
largest integer <= x                   | `math.floor(x)` | `x.__floor__()`
truncate x to nearest integer toward 0 | `math.trunc(x)` | `x.__trunc__()`
number as a list index                 | `a_list[x]`     | `a_list[x.__index__()]`

## Classes That Can Be Compared

You Want...                      | So You Write... | And Python Calls...
-------------------------------- | --------------- | -------------------
equality                         | `x == y`        | `x.__eq__(y)`
inequality                       | `x != y`        | `x.__ne__(y)`
less than                        | `x < y`         | `x.__lt__(y)`
less than or equal to            | `x <= y`        | `x.__le__(y)`
greater than                     | `x > y`         | `x.__gt__(y)`
greater than or equal to         | `x >= y`        | `x.__ge__(y)`
truth value in a boolean context | `if x:`         | `x.__bool__()`

> If you define a `__lt__()` method but no `__gt__()` method, Python will use the `__lt__()` method with operands swapped. However, Python will not combine methods. For example, if you define a `__lt__()` method and a `__eq__()` method and try to test whether x <= y, Python will not call `__lt__()` and `__eq__()` in sequence. It will only call the `__le__()` method.

## Classes That Can Be Serialized

Python supports serializing and unserializing arbitrary objects. (Most Python references call this process "pickling" and "unpickling.")

You Want...                                             | So You Write...                          | And Python Calls...
------------------------------------------------------- | ---------------------------------------- | -----------------------------------
a custom object copy                                    | `copy.copy(x)`                           | `x.__copy__()`
a custom object deepcopy                                | `copy.deepcopy(x)`                       | `x.__deepcopy__()`
to get an object's state before pickling                | `pickle.dump(x, file)`                   | `x.__getstate__()`
to serialize an object                                  | `pickle.dump(x, file)`                   | `x.__reduce__()`
to serialize an object (new pickling protocol)          | `pickle.dump(x, file, protocol_version)` | `x.__reduce_ex__(protocol_version)`
control over how an object is created during unpickling | `x = pickle.load(file)`                  | `x.__getnewargs__()`
to restore an object's state after unpickling           | `x = pickle.load(file)`                  | `x.__setstate__()`

> To recreate a serialized object, Python needs to create a new object that looks like the serialized object, then set the values of all the attributes on the new object. The `__getnewargs__()` method controls how the object is created, then the `__setstate__()` method controls how the attribute values are restored.

## Classes That Can Be Used in a `with` Block

A `with` block defines a runtime context; you "enter" the context when you execute the `with` statement, and you "exit" the context after you execute the last statement in the block.

You Want...                                     | So You Write... | And Python Calls...
----------------------------------------------- | --------------- | --------------------------------------------
do something special when entering a with block | `with x`:       | `x.__enter__()`
do something special when leaving a with block  | `with x`:       | `x.__exit__(exc_type, exc_value, traceback)`
