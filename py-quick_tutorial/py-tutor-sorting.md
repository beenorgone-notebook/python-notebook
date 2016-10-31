# [Sorting HOWTO in Python](https://docs.python.org/3/howto/sorting.html)

Python lists have a built-in `list.sort()` method that modifies the list in-place. There is also a `sorted()` built-in function that builds a new sorted list from an iterable.

In this document, we explore the various techniques for sorting data using Python.

## Sorting Basics

```python
sorted([5, 2, 3, 1, 4])
#[1, 2, 3, 4, 5]

a = [5, 2, 3, 1, 4]
a.sort()
a
#[1, 2, 3, 4, 5]
```

`list.sort()` method is only defined for lists. In contrast, the `sorted()` function accepts any iterable.

```python
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
#[1, 2, 3, 4, 5]
```

## Key Functions

Both `list.sort()` and `sorted()` have a _key_ parameter to specify a function to be called on each list element prior to making comparisons.

```python
sorted("This is a test string from Andrew".split(), key=str.lower)
#['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```

The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record.

A common pattern is to sort complex objects using some of the object's indices as keys. For example:

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ]

sorted(student_tuples, key=lambda student: student[2]) # sort by age
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

The same technique works for objects with named attributes. For example:

```python
>>> class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age
        def __repr__(self):
            return repr((self.name, self.grade, self.age))

>>> student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

## Operator Module Functions

Python provides convenience functions to make accessor functions easier and faster. The `operator` module has `itemgetter()`, `attrgetter()`, and a `methodcaller()` function.

Using those functions, the above examples become simpler and faster:

```python
>>> from operator import itemgetter, attrgetter

>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

The `operator` module functions allow multiple levels of sorting. For example, to sort by _grade_ then by _age_:

```python
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

## Ascending and Descending

Both `list.sort()` and `sorted()` accept a **_reverse_** parameter with a boolean value. This is used to flag descending sorts. For example, to get the student data in reverse **_age_** order:

```python
>>> sorted(student_tuples, key=itemgetter(2), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

>>> sorted(student_objects, key=attrgetter('age'), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

## Sort Stability and Complex Sorts

Sorts are guaranteed to be [stable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability). That means that when multiple records have the same key, their original order is preserved.

```python
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> sorted(data, key=itemgetter(0))
[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
```

This wonderful property lets you build complex sorts in a series of sorting steps. For example, to sort the student data by descending **_grade_** and then ascending **_age_**, do the **_age_** sort first and then sort again using **_grade_**:

```python
>>> s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
>>> sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

The Timsort algorithm used in Python does multiple sorts efficiently because it can take advantage of any ordering already present in a dataset.

TODO: <https://docs.python.org/3/howto/sorting.html#the-old-way-using-decorate-sort-undecorate>

## The Old Way Using Decorate-Sort-Undecorate

This idiom is called Decorate-Sort-Undecorate after its three steps:

- First, the initial list is decorated with new values that control the sort order.
- Second, the decorated list is sorted.
- Finally, the decorations are removed, creating a list that contains only the initial values in the new order.
