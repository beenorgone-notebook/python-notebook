# Writing Idiomatic Python - Chap 1: Control Structures and Functions

<!-- toc orderedList:0 -->

- [Writing Idiomatic Python - Chap 1: Control Structures and Functions](#writing-idiomatic-python-chap-1-control-structures-and-functions)
	- [If Statements](#if-statements)
		- [Avoid comparing directly to `True`, `False`, or `None`](#avoid-comparing-directly-to-true-false-or-none)
		- [Avoid repeating variable name in compound `if` statement](#avoid-repeating-variable-name-in-compound-if-statement)
		- [Avoid placing conditional branch code on the same line as the colon](#avoid-placing-conditional-branch-code-on-the-same-line-as-the-colon)
	- [`For` loops](#for-loops)
		- [Use the `enumerate` function in loops instead of creating an "index" variable](#use-the-enumerate-function-in-loops-instead-of-creating-an-index-variable)
		- [Use the `in` keyword to iterate over an iterable](#use-the-in-keyword-to-iterate-over-an-iterable)
		- [Use `else` to execute code after a `for` loop concludes](#use-else-to-execute-code-after-a-for-loop-concludes)
	- [Functions](#functions)
		- [Avoid using `''`, `[]`, and `{}` as default parameters to functions](#avoid-using-and-as-default-parameters-to-functions)
		- [Use `*args` and `**kwargs` to accept arbitrary arguments](#use-args-and-kwargs-to-accept-arbitrary-arguments)

<!-- tocstop -->

 ## If Statements

### Avoid comparing directly to `True`, `False`, or `None`

All of the following are considered `False`:

- `None`
- `False`
- zero for numeric types
- empty sequences
- empty dictionaries
- a value of 0 or `False` returned when either `__len__` or `__nonzero__` is called.

Comparison against `None` should always use `is` or `is not`, not `==`.

### Avoid repeating variable name in compound `if` statement

```python
name = 'Tom'
is_generic_name = name in ('Tom', 'Dick', 'Harry')
# True
```

### Avoid placing conditional branch code on the same line as the colon

## `For` loops

### Use the `enumerate` function in loops instead of creating an "index" variable

```python
my_container = ['Larry', 'Moe', 'Curly']
for index, element in enumerate(my_container):
    print('{} {}'.format(index, element))
```

### Use the `in` keyword to iterate over an iterable

### Use `else` to execute code after a `for` loop concludes

The `for ... else` allows you to check for a condition in a `for` loop, `break` if the condition holds for an element, `else` take some action if the condition did not hold for any of the elements being looped over.

```python
for user in get_all_users
    print('Checking {}'.format(user))
    for email_address in user.get_all_email_addresses():
        if email_is_malformed(email_address):
            print('Has a malformed email address!')
            break
    else:
        print('All email addresses are valid!')
```

## Functions

### Avoid using `''`, `[]`, and `{}` as default parameters to functions

prefer `names=None` to `names=[]` for default parameters to Functions.

The default value [of a function] is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

```python
# Harmful way
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
'''
[1]
[1, 2]
[1, 2, 3]
'''

# Idiomatic
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
'''
[1]
[2]
[3]
'''
```

### Use `*args` and `**kwargs` to accept arbitrary arguments

Oftentimes, functions need to accept an arbitrary list of positional parameters and/or keyword parameters, use a subset of them, and forward the rest to another function. Using `*args` and `**kwargs` as parameters allows a function to accept an arbitrary list of positional and keyword arguments, respectively.

The idiom is also useful when maintaining backwards compatibility in an API. If our function accepts arbitrary arguments, we are free to add new arguments in a new version while not breaking existing code using fewer arguments. As long as everything is properly documented, the "actual" parameters of a function are not of much consequence.

```python
#Harmful way:
def make_api_call(foo, bar, baz):
    if baz in ('Unicorn', 'Oven', 'New York'):
        return foo(bar)
    else:
        return bar(foo)
# I need to add another parameter to `make_api_call`
# without breaking everyone's existing code.
# I have two options...

def so_many_options():
    # I can tack on new parameters, but only if I make
    # all of them optional...
    def make_api_call(foo, bar, baz, qux=None, foo_polarity=None, baz_coefficient=None, quux_capacitor=None, bar_has_hopped=None, true=None, false=None, file_not_found=None):
        # ... and so on ad infinitum
        return file_not_found

def version_graveyard():
    # ... or I can create a new function each time the signature
    # changes.
    def make_api_call_v2(foo, bar, baz, qux):
        return make_api_call(foo, bar, baz) - qux
def make_api_call_v3(foo, bar, baz, qux, foo_polarity):
    if foo_polarity != 'reversed':
        return make_api_call_v2(foo, bar, baz, qux)
    return None

#Idiomatic
def make_api_call(foo, bar, baz):
    if baz in ('Unicorn', 'Oven', 'New York'):
        return foo(bar)
    else :
        return bar(foo)

# I need to add another parameter to `make_api_call`
# without breaking everyone's existing code.
# Easy...
def new_hotness():
    def make_api_call(foo, bar, baz, *args, **kwargs):
        # Now I can accept any type and number of arguments
        # without worrying about breaking existing code.
        baz_coefficient = kwargs['the_baz']
        # I can even forward my args to a different function without
        # knowing their contents!
        return baz_coefficient in new_function(args)
```
