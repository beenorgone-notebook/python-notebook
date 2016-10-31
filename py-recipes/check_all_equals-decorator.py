from itertools import groupby


def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def check_all_equals(func):
    def _check_all_equals(iterable):
        g = groupby(iterable)
        if next(g, True) and not next(g, False):
            return func(iterable)
        else:
            raise ValueError('Items are created unequal.')
    return _check_all_equals


@check_all_equals
def print_if_equal(iterable):
    print(iterable)


a = list(range(10))
b = [1] * 12

print_if_equal(b)
print_if_equal(a)
