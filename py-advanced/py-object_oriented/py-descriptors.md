# Python Descriptors

<!-- toc orderedList:0 -->

- [Python Descriptors](#python-descriptors)
	- [Resources](#resources)
	- [Introduction](#introduction)
		- [Descriptor Protocol](#descriptor-protocol)
		- [Property](#property)

<!-- tocstop -->

 ## Resources

[How-To Guide for Descriptors](http://users.rcn.com/python/download/Descriptor.htm)

[Python Descriptors](http://informit.com/articles/printerfriendly/1309289)

[Descriptor HowTo Guide -- Python 3.5.2 documentation](https://docs.python.org/3/howto/descriptor.html)

Descriptors in Programming in Python 3 book by Mark Summerfield

[Understanding `__get__` and `__set__` and Python descriptors - Stack Overflow](http://stackoverflow.com/questions/3798835/understanding-get-and-set-and-python-descriptors)

## Introduction

A descriptor: an object attribute with "binding behavior", one whose attribute access has been overridden by methods in the descriptor protocol. Those methods are `__get__`, `__set__`, and `__delete__`. If any of those methods are defined for an object, it is said to be a descriptor.

Descriptor instances are used to represent the attributes of other classes. For example, if we had a descriptor class called `MyDescriptor`, we might define a class that used it like this:

```python
class MyClass:
    a = MyDescriptor("a")
    b = MyDescriptor("b")
```

Descriptors are a powerful, general purpose protocol. They are the mechanism behind properties, methods, static methods, class methods, and `super()`.

The key to understanding descriptors is that although we create an instance of a descriptor in a class as a class attribute, Python accesses the descriptor through the class's instances.

### Descriptor Protocol

```
descr.__get__(self, obj, type=None) --> value

descr.__set__(self, obj, value) --> None

descr.__delete__(self, obj) --> None
```

If an object defines both `__get__` and `__set__`, it is considered a _data descriptor_.

Descriptors that only define `__get__` are called _non-data descriptors_

To make a read-only data descriptor, define both `__get__` and `__set__` with the `__set__` raising an `AttributeError` when called.

Defining the `__set__` method with an exception raising placeholder is enough to make it a data descriptor.

```python
class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating' , self.name
        self.val = val

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
m.x
#Retrieving var "x"
#10
m.x = 20
#Updating var "x"
m.x
#Retrieving var "x"
#20
m.y
#5
```

### Property

Implement `property()` in terms of the descriptor protocol:

```python
class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError, "unreadable attribute"
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError, "can't set attribute"
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError, "can't delete attribute"
        self.fdel(obj)
```
