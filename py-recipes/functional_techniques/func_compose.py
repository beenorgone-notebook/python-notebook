# https://mathieularose.com/function-composition-in-python/

from functools import reduce


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def compose1(*funcs):
    def compose_2_funcs(f, g):
        print('composing "{}" func of "{}" func'.format(f.__doc__,
                                                        g.__doc__))
        return lambda x: f(g(x))
    return reduce(compose_2_funcs, funcs, lambda x: x)


def pipeline(*fns):
    def compose(f1, f2):
        print('composing "{}" func of "{}" func'.format(f1.__doc__,
                                                        f2.__doc__))
        return lambda *args: f1(f2(*args))
    return reduce(compose, fns)

# Example
f = lambda z: z + 1
f.__doc__ = 'increase one'
g = lambda y: y * 2
g.__doc__ = 'double'
h = lambda x: x - 3
h.__doc__ = 'decrease three'

# Call the function x=10 : ((x-3)*2)+1 = 15
print(compose(f, g, h)(10))  # 15
print(compose(f, g, h).__doc__)  # None
print(compose(f, g, h).__name__)  # <lambda>
print(compose1(f, g, h)(10))
'''
composing "None" func of "increase one" func
composing "None" func of "double" func
composing "None" func of "decrease three" func
15
'''
print(pipeline(f, g, h)(10))
'''
composing "increase one" func of "double" func
composing "None" func of "decrease three" func
15
'''
