import functools
import inspect


def argtypes_check(*argtypes):
    '''function arguments type checker'''
    def _argtypes_check(func):
        '''Take the function'''
        @functools.wraps(func)
        def __argtypes_check(*func_args):
            '''Take arguments'''
            if len(argtypes) != len(func_args):
                raise TypeError('expected {} but get {} arguments'.format(
                    len(argtypes), len(func_args)))
            for argtype, func_arg in zip(argtypes, func_args):
                if not isinstance(argtype, func_arg):
                    raise TypeError('expected {} but get {}'.format(
                        argtypes, tuple(type(func_arg) for func_arg in func_args)))
            return func(*func_args)
        return __argtypes_check
    return _argtypes_check


@argtypes_check(int, int)
def add(x, y):
    '''Add two integers.'''
    return x + y

# version 2:


def checkargs(function):
    def _f(*arguments):
        print(inspect.getfullargspec(function))
        for index, argument in enumerate(inspect.getfullargspec(function)[0]):
            if not isinstance(arguments[index], function.__annotations__[argument]):
                raise TypeError("{} is not of type {}".format(
                    arguments[index],
                    function.__annotations__[argument]))
        return function(*arguments)
    _f.__doc__ = function.__doc__
    return _f


def coerceargs(function):
    def _f(*arguments):
        new_arguments = []
        for index, argument in enumerate(inspect.getfullargspec(function)[0]):
            new_arguments.append(function.__annotations__[
                                 argument](arguments[index]))
        return function(*new_arguments)
    _f.__doc__ = function.__doc__
    return _f

if __name__ == "__main__":
    @checkargs
    def f(x: int, y: int):
        """
        A doc string!
        """
        return x, y

    @coerceargs
    def g(a: int, b: int):
        """
        Another doc string!
        """
        return a + b

    print(f(1, 2))
    try:
        print(f(3, 4.0))
    except TypeError as e:
        print(e)

    print(g(1, 2))
    print(g(3, 4.0))
