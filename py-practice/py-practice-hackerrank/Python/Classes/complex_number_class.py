from functools import wraps


def method_argtypes_check(*argtypes):
    '''method arguments type checker'''
    def _argtypes_check(method):
        '''Take the method'''
        @wraps(method)
        def __argtypes_check(self_arg, *method_args):
            '''Take arguments'''
            if len(argtypes) != len(method_args):
                raise TypeError('expected {} but get {} arguments'.format(
                    len(argtypes), len(method_args)))
            for argtype, method_arg in zip(argtypes, method_args):
                if not isinstance(method_arg, argtype):
                    raise TypeError('expected {} but get {}'.format(
                        argtypes, tuple(type(method_arg)
                                        for method_arg in method_args)))
            return method(self_arg, *method_args)
        return __argtypes_check
    return _argtypes_check


class ComplexNumber:

    @method_argtypes_check(float, float)
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.img * other.img,
                             self.real * other.img + self.img * other.real)

    def __truediv__(self, other):
        try:
            return self.__mul__(ComplexNumber(other.real, -1 * other.img)).__mul__(ComplexNumber(1.0 / (other.mod().real)**2, 0.0))
        except ZeroDivisionError as e:
            print(e)
            return None

    def mod(self):
        return ComplexNumber(pow(self.real**2 + self.img**2, 0.5), 0.0)

    def __str__(self, precision=2):
        return str(("%." + "%df" % precision) % float(self.real)) + ('+' if self.img >= 0 else '-') + str(("%." + "%df" % precision) % float(abs(self.img))) + 'i'

A = ComplexNumber(*map(float, input().strip().split()))
B = ComplexNumber(*map(float, input().strip().split()))

print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A.mod())
print(B.mod())
