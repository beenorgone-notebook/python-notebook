# The Hitchhiker's Guide to Python Notes

<!-- toc orderedList:0 -->

 - [The Hitchhiker's Guide to Python Notes](#the-hitchhikers-guide-to-python-notes)

  - [Code Style](#code-stylehttpdocspython-guideorgenlatestwritingstyle)

    - [Function arguments](#function-arguments)

<!-- tocstop -->

 ## Resources

[Online version](http://docs.python-guide.org)

[PEP20 by Examples](http://artifex.org/~hblanks/talks/2011/pep20_by_example.pdf)

## [Code Style](http://docs.python-guide.org/en/latest/writing/style)

Write explicit and straightforward code

One statement per line

### Function arguments

When choosing keyword arguments, remember **YAGNI** ([You aren't gonna need it](https://www.wikiwand.com/en/You_aren't_gonna_need_it)) principle.

> It's harder to remove an optional arguments (and its logic inside the function) that was added "just in case" and is seemingly never used, than to add a new optional argument and its logic when needed

Careful with _arbitrary argument list_ and _arbitrary keyword argument dictionary_

> If a function receives a list of arguments of the same nature, it is often more clear to define it as a function of one argument, that argument being a list or any sequence.

--------------------------------------------------------------------------------

Prefix all "internals" with an underscore. Any method or property that is not intended to be used by client code should be prefixed with an underscore.

> If the client code breaks this rule and accesses these marked elements, any misbehavior or problems encountered if the code is modified is the responsibility of the client code.

### Returning values

Avoid `return` meaningful values from many output points in the body.

`return` as early as possible when the incorrect context has been detected. Having multiple such `return` statements is often necessary.

However, when a function has multiple main exit points, it becomes difficult to debug.

```python
def complex_function(a, b, c):
    if not a:
        return None  # Raising an exception might be better
    if not b:
        return None  # Raising an exception might be better
    # Some complex code trying to compute x from a, b and c
    # Resist temptation to return x if succeeded
    if not x:
        # Some Plan-B computation of x
    return x  # One single exit point for the returned value x will help
              # when maintaining the code.
```

### Idioms
