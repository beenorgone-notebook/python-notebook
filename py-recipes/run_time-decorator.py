# 3. Use `functools.wraps` to preserve the function attributes
# including the docstring that you wrote.

# 1. Write a function decorator that can be used to measure
# the run time of a functions. Use `timeit.default_timer` to get time stamps.
import functools
from timeit import default_timer as timer


def runtime1(func):
    @functools.wraps(func)
    def _runtime(*args, **kwargs):
        start = timer()
        x = func(*args, **kwargs)
        end = timer()
        print("Run Time is {}".format(end - start))
        return x
    return _runtime


@runtime1
def add(a, b):
    return a + b

print(add(322, 3))


# 2. Make the decorator parameterized. It should take an integer
# that specifies how often the function has to be run.
# Make sure you divide the resulting run time by this number.
def check(*argtypes):
    '''Function argument type checker.'''
    def _check(func):
        '''Takes the function.'''
        @functools.wraps(func)
        def __check(*args):
            '''Takes the arguments'''
            if len(args) != len(argtypes):
                msg = 'Expected %d but got %d arguments' % (
                    len(argtypes), len(args))
                raise TypeError(msg)
            for arg, argtype in zip(args, argtypes):
                if not isinstance(arg, argtype):
                    msg = 'Expected %s but got %s' % (
                        argtypes, tuple(type(arg) for arg in args))
                    raise TypeError(msg)
            return func(*args)
        return __check
    return _check


@check(int)
def runtime2(times):
    def _runtime(func):
        @functools.wraps(func)
        def __runtime(*args, **kwargs):
            x = []
            start = timer()
            for _ in range(times):
                x.append(func(*args, **kwargs))
            end = timer()
            print('Average runtime is {}'.format((end - start) / times))
            return x
        return __runtime
    return _runtime


@runtime2(5)
def power(a, b):
    return pow(a, b)

print(power(322, 3))

# 4. Make the time measurement optional by using a global switch in the
# module that can be set to True or False to turn time measurement on or off.
TIME_LOG = False


@check(int)
def runtime3(times):
    def _runtime3(func):
        @functools.wraps(func)
        def __runtime3(*args, **kwargs):
            x = []
            if TIME_LOG:
                start = timer()
                for _ in range(times):
                    x.append(func(*args, **kwargs))
                end = timer()
                print('Average runtime is {}'.format((end - start) / times))
            else:
                for _ in range(times):
                    x.append(func(*args, **kwargs))
            return x
        return __runtime3
    return _runtime3


@runtime3(5)
def power(a, b):
    return pow(a, b)

print(power(4, 12))

TIME_LOG = True

print(power(4, 12))

# 5. Write another decorator that can be used with a class and registers
# every class that it decorates in a dictionary.

registry = {}


def decor_all_methods(decorator):
    def decorate(cls):
        '''for attr in cls.__dict__:  # there's propably a better way to do this
            if callable(getattr(cls, attr)) and attr != '__init__':
                setattr(cls, attr, decorator(getattr(cls, attr)))
                registry.setdefault(cls, []).append(attr)'''
        callable_attributes = {k: v for k,
                               v in cls.__dict__.items() if callable(v) and k != '__init__'}
        for name, func in callable_attributes.items():
            decorated = decorator(func)
            setattr(cls, name, decorated)
            registry.setdefault(cls, []).append(name)
        return cls
    return decorate


@decor_all_methods(runtime3(2))
class Math():
    '''decor all methos of Math class (except __init__) with runtime3 decorator which make the method run 2 times'''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def power(self):
        return pow(self.a, self.b)

m = Math(34, 12)
print(m.power())
print(registry)
