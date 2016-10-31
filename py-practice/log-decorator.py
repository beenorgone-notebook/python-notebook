''' Write a decorator which wraps functions to log function arguments
and the return value on each call. Provide support for both
positional and named arguments (your wrapper function should take
both *args and **kwargs and print them both):

>>> @logged
    def func(*args):
        return 3 + len(args)
>>> func(4, 4, 4)
you called func(4, 4, 4)
it returned 6
6
'''
# Function version
import functools


def logged(func):
    '''Print out the arguments before function call and after the
    call print out the returned value. Provide support for both
    positional and named arguments (your wrapper function should take
    both *args and **kwargs and print them both):
    '''
    def print_args(*args, **kwargs):
        '''print args, kwargs of func'''
        if kwargs:
            print_kwargs = ', '.join('{}={}'.format(*pair)
                                     for pair in kwargs.items())
            return print_kwargs
        elif args:
            print_args = ', '.join('{}'.format(arg) for arg in args)
            return print_args

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        print('you called {}({})'.format(
            func.__name__,
            print_args(*args, **kwargs)))
        val = func(*args, **kwargs)
        print('it returned {}'.format(val))
        return val
    return _wrapper


@logged
def superpower(x, y, z):
    '''power z of power of y of x'''
    return x ** y ** z

s = superpower(2, 3, 1)
print(superpower.__doc__)
# without @functools.wraps(func) it will print _wrapper's name
print(superpower.__name__)
print(superpower(x=2, y=4, z=2))


# Class version:


class Logged:

    def __init__(self, func):
        self.func = func

    def _print_args(*args, **kwargs):
        '''print args, kwargs of func'''
        if kwargs:
            print_kwargs = ', '.join('{}={}'.format(*pair)
                                     for pair in kwargs.items())
            return print_kwargs
        elif args:
            print_args = ', '.join('{}'.format(arg) for arg in args)
            return print_args

    def __call__(self, *args, **kwargs):
        print('you called {}({})'.format(
            self.func.__name__,
            print_args(*args, **kwargs)))
        val = self.func(*args, **kwargs)
        print('it returned {}'.format(val))
        return val


@logged
def superpower(x, y, z):
    '''power z of power of y of x'''
    return x ** y ** z

print(superpower(2, 3, 1))
print(superpower.__doc__)
print(superpower.__name__)
print(superpower(x=2, y=4, z=2))
