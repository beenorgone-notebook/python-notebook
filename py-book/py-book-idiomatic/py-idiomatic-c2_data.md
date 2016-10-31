# Writing Idiomatic Python - Chap 2: Working with Data

<!-- toc orderedList:0 -->

- [Writing Idiomatic Python - Chap 2: Working with Data](#writing-idiomatic-python-chap-2-working-with-data)
	- [Lists](#lists)
		- [Use a list comprehensions to create a transformed version of an existing list](#use-a-list-comprehensions-to-create-a-transformed-version-of-an-existing-list)
		- [Use the `*` operator to represent the 'rest' of a list](#use-the-operator-to-represent-the-rest-of-a-list)
	- [Dictionaries](#dictionaries)
		- [Use the default parameter of `dict.get` to provide default values](#use-the-default-parameter-of-dictget-to-provide-default-values)
		- [Use a dict comprehension to build a dict clearly and efficiently](#use-a-dict-comprehension-to-build-a-dict-clearly-and-efficiently)
	- [Strings](#strings)
		- [Prefer the `format` function for formatting strings](#prefer-the-format-function-for-formatting-strings)
		- [Use `''.join` when creating a single string for list elements](#use-join-when-creating-a-single-string-for-list-elements)
		- [Chain string function to make a simple series of transformations more clear](#chain-string-function-to-make-a-simple-series-of-transformations-more-clear)
	- [Classes](#classes)
		- [Use underscores in function and variable names to help mark 'private' data](#use-underscores-in-function-and-variable-names-to-help-mark-private-data)
		- [Define `__str__` in a class to show a human-readable representation](#define-__str__-in-a-class-to-show-a-human-readable-representation)
	- [Sets](#sets)
		- [Use sets to eliminate duplicate entries from Iterable containers](#use-sets-to-eliminate-duplicate-entries-from-iterable-containers)
		- [Use a set comprehension to generate sets concisely](#use-a-set-comprehension-to-generate-sets-concisely)
		- [Understand and use the mathematical set operations](#understand-and-use-the-mathematical-set-operations)
	- [Generators](#generators)
		- [Use a generator to lazily load infinite sequences](#use-a-generator-to-lazily-load-infinite-sequences)
		- [Prefer a generator expression to a list comprehension for simple iteration](#prefer-a-generator-expression-to-a-list-comprehension-for-simple-iteration)
	- [Context Managers](#context-managers)
		- [Use a context manager to ensure resources are properly managed](#use-a-context-manager-to-ensure-resources-are-properly-managed)
	- [Tuples](#tuples)
		- [Use tuples to unpack data](#use-tuples-to-unpack-data)
		- [Use `_` as a placeholder for data in a tuple that should be ignored](#use-_-as-a-placeholder-for-data-in-a-tuple-that-should-be-ignored)
	- [Variables](#variables)
		- [Avoid using a temporary variable when performing a **swap** of two values](#avoid-using-a-temporary-variable-when-performing-a-swap-of-two-values)

<!-- tocstop -->

 ## Lists

### Use a list comprehensions to create a transformed version of an existing list

### Use the `*` operator to represent the 'rest' of a list

```python
some_list = ['a', 'b', 'c', 'd', 'e']

(first, second, *rest) = some_list
print(rest)
(first, *middle, last) = some_list
print(middle)
(*head, penultimate, last) = some_list
print(head)
```

## Dictionaries

### Use the default parameter of `dict.get` to provide default values

```python
# Harmful way
log_severity = None
if 'severity' in configuration:
    log_severity = configuration['severity']
else:
    log_severity = 'Info'

# Idiomatic
log_severity = configuration.get('severity', 'Info')
```

### Use a dict comprehension to build a dict clearly and efficiently

## Strings

### Prefer the `format` function for formatting strings

### Use `''.join` when creating a single string for list elements

```python
result_list = ['True', 'False', 'File not found'] result_string = ''.join(result_list)
```

### Chain string function to make a simple series of transformations more clear

"No more than three chained functions" is a good rule of thumb.

## Classes

### Use underscores in function and variable names to help mark 'private' data

### Define `__str__` in a class to show a human-readable representation

```python
# Harmful
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = (1, 2)
print(p)
#<__main__.Point object at 0x7fba7d10bd30>

# Idiomatic
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

p = Point(1, 2)
print(p)
#1, 2
```

## Sets

### Use sets to eliminate duplicate entries from Iterable containers

### Use a set comprehension to generate sets concisely

```python
# Harmful
users_first_names = set()
for user in users:
    users_first_names.add(user.first_name)

# Idiomatic
users_first_names = {user.first_name for user in users}
```

### Understand and use the mathematical set operations

Union, Intersection, Difference, Symmetric Difference

## Generators

### Use a generator to lazily load infinite sequences

A generator is a special type of coroutine which returns an iterable . The state of the generator is saved, so that the next call into the generator continues where it left off.

```python
def get_twitter_stream_for_keyword(keyword):
    """Now, 'get_twitter_stream_for_keyword' is a generator
    and will continue to generate Iterable pieces of data
    one at a time until 'can_get_stream_data(user)' is
    False (which may be never).
    """
    imaginary_twitter_api = ImaginaryTwitterAPI()
    while imaginary_twitter_api.can_get_stream_data(keyword):
    yield imaginary_twitter_api.get_stream(keyword)


# Because it's a generator, I can sit in this loop until
# the client wants to break out
for tweet in get_twitter_stream_for_keyword('#jeffknupp'):
    if got_stop_signal:
        break
    process_tweet(tweet)


def get_list_of_incredibly_complex_calculation_results(data):
    """A simple example to be sure, but now when the client
    code iterates over the call to
    'get_list_of_incredibly_complex_calculation_results',
    we only do as much work as necessary to generate the
    current item.
    """
    yield first_incredibly_long_calculation(data)
    yield second_incredibly_long_calculation(data)
    yield third_incredibly_long_calculation(data)
```

### Prefer a generator expression to a list comprehension for simple iteration

```python
# Harmful
for uppercase_name in [name.upper() for name in get_all_usernames()]:
    process_normalized_username(uppercase_name)

# Idiomatic
for uppercase_name in (name.upper() for name in get_all_usernames()):
    process_normalized_username(uppercase_name)
```

## Context Managers

### Use a context manager to ensure resources are properly managed

**context managers** (objects meant to be used with the with statement) can make resource management both safer and more explicit. The canonical example is file `IO`.

There are a number of classes in the standard library that support or use a context manager . In addition, user defined classes can be easily made to work with a context manager by defining `__enter__` and `__exit__` methods. Functions may be wrapped with context managers through the `contextlib` module.

```python
# Harmful

file_handle = open(path_to_file, 'r') for line in file_handle.readlines(): if raise_exception(line): print ('No! An Exception!')

# Idiomatic
with open(path_to_file, 'r') as file_handle:
    for line in file_handle:
        if raise_exception(line):
            print ('No! An Exception!')
```

## Tuples

### Use tuples to unpack data

### Use `_` as a placeholder for data in a tuple that should be ignored

```python
(name, age, _, _) = get_user_info(user)
if age > 21:
    output = '{name} can drink!'.format(name=name)
# "Clearly, only name and age are interesting"
```

## Variables

### Avoid using a temporary variable when performing a **swap** of two values

```python
# Harmful
foo = 'Foo'
bar = 'Bar'
temp = foo
foo = bar
bar = temp

# Idiomatic
foo = 'Foo'
bar = 'Bar'
(foo, bar) = (bar, foo)
```
