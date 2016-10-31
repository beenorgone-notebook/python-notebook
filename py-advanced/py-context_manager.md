# Python: Context Manager

<!-- toc orderedList:0 -->

- [Python: Context Manager](#python-context-manager)
	- [Resources](#resources)
	- [Basic](#basic)
		- [About `__enter__()` and `__exit__()`](#about-__enter__-and-__exit__)
	- [`contextlib` -- Utilities for with-statement contexts](#contextlib-utilities-for-with-statement-contexts)
		- [Utilities](#utilities)
			- [`contextlib.contextmanager`](#contextlibcontextmanager)
			- [`contextlib.closing(thing)`](#contextlibclosingthing)
			- [`contextlib.suppress(*exceptions)`](#contextlibsuppressexceptions)
			- [`contextlib.redirect_stdout(new_target)` and `contextlib.redirect_stderr(new_target)`](#contextlibredirect_stdoutnew_target-and-contextlibredirect_stderrnew_target)
			- [_class_ `contextlib.ContextDecorator`](#_class_-contextlibcontextdecorator)
			- [_class_ `contextlib.ExitStack`](#_class_-contextlibexitstack)
				- [Why `ExitStack` ?](#why-exitstack)
				- [Callback](#callback)
				- [`enter_context(cm)`](#enter_contextcm)
				- [`push(exit)`](#pushexit)
				- [`callback(callback, *args, **kwds)`](#callbackcallback-args-kwds)
				- [`pop_all()`](#pop_all)
				- [`close()`](#close)
		- [Examples and Recipes](#examples-and-recipes)
			- [Supporting a variable number of context managers](#supporting-a-variable-number-of-context-managers)

<!-- tocstop -->

 ## Resources

[Hitchhiker's Guide to Python - Context Manager](http://docs.python-guide.org/en/latest/writing/structure/#context-managers)

[contextlib -- Utilities for with-statement contexts](https://docs.python.org/3/library/contextlib.html)

- [Context Manager Type](https://docs.python.org/3/library/stdtypes.html#typecontextmanager)
- [With Statement Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
- [Callback (computer programming) - Wiki](https://wikiwand.com/en/Callback_(computer_programming))

[Resource management in Python 3](http://www.wefearchange.org/2013/05/resource-management-in-python-33-or.html)

On `ExitStack`:

- [On the Beauty of Python's ExitStack -- Nikolaus Rath's Website](https://www.rath.org/on-the-beauty-of-pythons-exitstack.html)

## Basic

Context Manager: a Python object that provides _extra contextual information_ to an action.

It run a callable upon initiating the context using the `with` statement, as well as running a callable upon completing all the code inside the with block. The most well known example of using a context manager is shown here, opening on a file:

```python
with open('file.txt') as f:
    contents = f.read()
```

Invoking `open` ensures that `f`'s `close` method will be called at some point.

Two ways to implement:

```python
# Class version
class CustomOpen(object):
    def __init__(self, filename):
      self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()

# the generator approach using Python’s own `contextlib`:
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()
```

### About `__enter__()` and `__exit__()`

`__enter__` should return an object that is assigned to the variable after as. By default it is `None`, and is optional. A common pattern is to return `self` and keep the functionality required within the same class.

`__exit__` is called on the original Context Manager object, not the object returned by `__enter__`.

If an error is raised in `__init__` or `__enter__` then the code block is never executed and `__exit__` is not called.

Once the code block is entered, `__exit__` is always called, even if an exception is raised in the code block.

If `__exit__` returns `True`, the exception is suppressed.

## `contextlib` -- Utilities for with-statement contexts

### Utilities

#### `contextlib.contextmanager`

A decorator that can be used to define a factory function for `with` statement context managers, without needing to create a class or separate `__enter__()` and `__exit__()` methods.

```python
from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

'''
with tag("h1"):
        print("foo")

<h1>
foo
</h1>
'''
```

#### `contextlib.closing(thing)`

Make an 'opener' -- ex: urlopen, ... -- behaves like `with open()`. Equivalent to:

```python
from contextlib import contextmanager

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

# And lets you write code like this:
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)
```

#### `contextlib.suppress(*exceptions)`

Retur a context manager that suppresses any of `*exceptions` if they occur in the body of a `with` statement. Equivalent to:

```python
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

# Example:
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')
```

#### `contextlib.redirect_stdout(new_target)` and `contextlib.redirect_stderr(new_target)`

Temporarily redirecting `sys.stdout` or `sys.stderr` to another file of file-like object.

```python
from contextlib import redirect_stdout, redirect_stderr

f = io.StringIO():
with redirect_stdout(f):
    help(pow)
s = f.getvalue()

# redirect the output to a regular file
with open('help.txt', 'w') as f:
    with redirect_stderr(f):
        help(pow)
```

#### _class_ `contextlib.ContextDecorator`

A _base class_ that enables a context manager to also be used as a decorator.

Context managers inheriting from `ContextDecorator` have to implement `__enter__` and `__exit__` as normal. `__exit__` retains its optional exception handling even when used as a decorator.

#### _class_ `contextlib.ExitStack`

A context manager which helps us combine other context managers and cleanup functions.

```python
# a set of files may easily be handled in a single `with` statement as follows:
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    # All opened files will automatically be closed at the end of the
    # `with` statement, even if attemps to open files later in the list
    # raise an exception
```

##### Why `ExitStack` ?

Without `with` (or context managers) we will have problems:

1. The cleanup code is far away from the allocation code.
2. When the number of resources increases, indentation levels (or jump labels) accumulate, making things hard to read.
3. Impossible to managing a dynamic number of resources.

`with` solution is far from optimal:

1. still need to implement resource-specific context managers
2. must allocate all the resources at the same time to get rid of extra indentation.
3. can't deal with dynamic number of resources.

`ExitStack` to the rescue:

1. Fixes all of the above issues

  1. acquisition and release are close to each other
  2. no extra indentation
  3. easily scales up to many resources

2. A stack of clean-up functions

3. Clean-up functions are not executed when the function returns, but when execution leaves the `with` block.

4. May raise exceptions without affecting execution of other clean-up functions.

##### Callback

> In computer programming, a **callback** is a piece of executable code that is passed as an argument to other code, which is expected to call back (execute) the argument at some convenient time. (Wikipedia)

> A "callback" is any function that is called by another function which takes the first function as a parameter. A lot of the time, a "callback" is a function that is called when something happens. That something can be called an "event" in programmer-speak. (Stackoverflow)

```python
def my_callback(val):
    print("function my_callback was called with {0}".format(val))

def caller(val, func):
    func(val)


for i in range(5):
    caller(i, my_callback)
```

##### `enter_context(cm)`

Enters a new context manager and adds its `__exit__()` method to the callback stack.

##### `push(exit)`

Adds a context manager's `__exit__()` method to the callback stack.

##### `callback(callback, *args, **kwds)`

Accepts an arbitrary callback function and arguments and adds it to the callback stack.

Unlike the other methods, callbacks added this way cannot suppress exceptions (as they are never passed the exception details).

The passed in callback is returned from the function, allowing this method to be used as a function decorator.

##### `pop_all()`

Transfers the callback stack to a fresh `ExitStack` instance and returns it. No callbacks are invoked by this operation - instead, they will now be invoked when the new stack is closed (either explicitly or implicitly at the end of a `with` statement).

```python
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    # Hold onto the close method, but don't call it yet.
    close_files = stack.pop_all().close
    # If opening any file fails, all previously opened files will be
    # closed automatically. If all files are opened successfully,
    # they will remain open even after the `with` statement ends.
    # close_files() can then be invoked explicitly to close them all.
```

##### `close()`

Immediately unwinds the callback stack, invoking callbacks in the reverse order of registration. For any context managers and exit callbacks registered, the arguments passed in will indicate that no exception occurred.

### Examples and Recipes

#### Supporting a variable number of context managers

```python
with ExitStack() as stack:
    for resource in resources:
        stack.enter_context(resource)
    if need_special_resource():
        special = acquire_special_resource()
        stack.callback(release_special_resource, special)
    # Perform operations that use the acquired resources
```
