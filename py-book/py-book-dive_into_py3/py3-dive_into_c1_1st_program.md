[Dive into Python 3: First Prorgram](http://www.diveintopython3.net/your-first-python-program.html)
===================================================================================================

Python functions do not specify the datatype of their return value; they don’t even specify whether or not they return a value. (In fact, every Python function returns a value; if the function ever executes a return statement, it will return that value, otherwise it will return `None`, the Python null value.)

In Java and other statically-typed languages, you must specify the datatype of the function return value and each function argument. In Python, you never explicitly specify the datatype of anything. Based on what value you assign, Python keeps track of the datatype internally.

Optional and Named Arguments
----------------------------

Python allows function arguments to have default values; if the function is called without the argument, the argument gets its default value. Furthermore, arguments can be specified in any order by using named arguments.

**Default parameter values are evaluated from left to right when the function definition is executed.** This means that the expression is evaluated once, when the function is defined, and that the same "pre-computed" value is used for each call. This is especially important to understand when a default parameter is a mutable object, such as a list or a dictionary: if the function modifies the object (e.g. by appending an item to a list), the default value is in effect modified. This is generally not what was intended. A way around this is to use "None" as the default, and explicitly test for it in the body of the function, e.g.:

```python
def whats_on_the_telly(penguin=None):
   if penguin is None:
       penguin = []
   penguin.append("property of the zoo")
   return penguin
```

Writing Readable Code
---------------------

You can document a Python function by giving it a documentation string (docstring for short).

```python
def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
```

A `docstring`, if it exists, must be the first thing defined in a function (that is, on the next line after the function declaration). You don’t technically need to give your function a `docstring`, but you always should.

The `import` search path
------------------------

```python
import sys
sys.path
#['', '/home/beenorgone', '/usr/bin', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']
sys
#<module 'sys' (built-in)>
sys.path.insert(0, 'home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples')
sys.path
#['home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples', '', '/home/beenorgone', '/usr/bin', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']
```

1\. `sys.path` is a list of directory names that constitute the current search path. Python will look through these directories (in this order) for a `.py` file whose name matches what you’re trying to import.

2\. Not all modules are stored as `.py` files. Some are built-in modules; they are actually baked right into Python itself. Built-in modules behave just like regular modules, but their Python source code is not available, because they are not written in Python! (Like Python itself, these built-in modules are written in C.)

3\. You can add a new directory to Python’s search path at runtime by adding the directory name to `sys.path`, and then Python will look in that directory as well, whenever you try to import a module. The effect lasts as long as Python is running:

```python
sys.path.insert(0, new_path)
```

Everything is an Object
-----------------------

```python
import humansize #import `humansize` as a module.
print(humansize.approximate_size(4096,True))
#4.0 KiB
print(humansize.approximate_size.__doc__)
#Convert a file size to human-readable form.

#    Keyword arguments:
#    size -- file size in bytes
#    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
#                                if False, use multiples of 1000

#    Returns: string
```

1\. When you want to use functions defined in imported modules, you need to include the module name. So you can’t just say `approximate_size`; it must be `humansize.approximate_size`. If you’ve used classes in Java, this should feel vaguely familiar.

> `import` in Python is like require in Perl. Once you import a Python module, you access its functions with `module.function`; once you require a Perl module, you access its functions with `module::function`.

2\. Instead of calling the function as you would expect to, you asked for one of the function’s attributes, `__doc__`.

What's an Object?
-----------------

*Everything in Python is an object*, and everything can have attributes and methods. All functions have a built-in attribute `__doc__`, which returns the `docstring` defined in the function’s source code. The `sys` module is an object which has (among other things) an attribute called `path`. And so forth.

Some objects have neither attributes nor methods, but they could. Not all objects are subclassable. But everything is an object in the sense that it can be assigned to a variable or passed as an argument to a function.

In Python, functions are *first-class objects*. You can pass a function as an argument to another function. Modules are *first-class objects*. You can pass an entire module as an argument to a function. Classes are *first-class objects*, and individual instances of a class are also *first-class objects*.

Indenting Code
--------------

Python functions have no explicit begin or end, and no curly braces to mark where the function code starts and stops. The only delimiter is a colon (`:`) and the indentation of the code itself.

Code blocks are defined by their indentation. By “code block,” I mean functions, if statements, for loops, while loops, and so forth. Indenting starts a block and unindenting ends it.

One major benefit is that all Python programs look similar, since indentation is a language requirement and not a matter of style. This makes it easier to read and understand other people’s Python code.

> Python uses carriage returns to separate statements and a colon and indentation to separate code blocks. c++ and Java use semicolons to separate statements and curly braces to separate code blocks.

Exceptions
----------

What is an exception? Usually it’s an error, an indication that something went wrong. (Not all exceptions are errors, but never mind that for now.) Some programming languages encourage the use of error return codes, which you *check*. Python encourages the use of exceptions, which you *handle*.

When an error occurs in the Python Shell, it prints out some details about the exception and how it happened, and that’s that. This is called an *unhandled* exception. When the exception was raised, there was no code to explicitly notice it and deal with it, so it bubbled its way back up to the top level of the Python Shell, which spits out some debugging information and calls it a day. In the shell, that's no big deal, but if that happened while your actual Python program was running, the entire program would come to a screeching halt if nothing handles the exception. Maybe that’s what you want, maybe it isn’t.

An exception doesn’t need to result in a complete program crash, though. Exceptions can be *handled*. Sometimes an exception is really because you have a bug in your code (like accessing a variable that doesn’t exist), but sometimes an exception is something you can anticipate. If you’re opening a file, it might not exist. If you’re importing a module, it might not be installed. If you’re connecting to a database, it might be unavailable, or you might not have the correct security credentials to access it. If you know a line of code may raise an exception, you should handle the exception using a *try...except* block.

Python uses `try...except` blocks to handle exceptions, and the `raise` statement to generate them.

```python
if size < 0:
    raise ValueError('number must be non-negative')
```

Catching Import Errors
----------------------

One of Python’s built-in exceptions is `ImportError`, which is raised when you try to import a module and fail. This can happen for a variety of reasons, but the simplest case is when the module doesn’t exist in your import search path. You can use this to include optional features in your program.

```python
try:
  import chardet
except ImportError:
  chardet = None
```

Another common use of the ImportError exception is when two modules implement a common api, but one is more desirable than the other. (Maybe it’s faster, or it uses less memory.) You can try to import one module but fall back to a different module if the first import fails.

```python
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
```

By the end of this `try..except` block, you have imported some module and named it `etree`. Since both modules implement a common `api`, the rest of your code doesn’t need to keep checking which module got imported. And since the module that did get imported is always called `etree`, the rest of your code doesn’t need to be littered with `if` statements to call differently-named modules.

Unbound Variables
-----------------

Python will not let you do is reference a variable that has never been assigned a value. Trying to do so will raise a `NameError` exception.

```python
x
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'x' is not defined
x = 1
x
#1
```

Everything Is Case-Sensitive
----------------------------

All names in Python are case-sensitive: variable names, function names, class names, module names, exception names.

Running Scripts
---------------

Python modules are objects and have several useful attributes. You can use this to easily test your modules as you write them, by including a special block of code that executes when you run the Python file on the command line. Take the last few lines of `humansize.py`:

```python
if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
```

all modules have a built-in attribute `__name__`. A module’s `__name__` depends on how you’re using the module. If you import the module, then `__name__` is the module’s filename, without a directory path or file extension.

```python
humansize.__name__
#'humansize'
```

But you can also run the module directly as a standalone program, in which case `__name__` will be a special default value, `__main__`.
