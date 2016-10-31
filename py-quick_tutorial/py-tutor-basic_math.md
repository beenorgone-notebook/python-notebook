Python Quick References: Basic Math
===================================

**Contents:**

1.	Booleans
2.	Numbers
3.	Coercing Integers To Floats And Vice-Versa
4.	Common Numerical Operations
5.	Fractions
6.	Trigonometry
7.	Numbers In A Boolean Context

Booleans
--------

```Python
True + True
#2
True - False
#1
True * False
#0
True / False
#Traceback (most recent call last):
#  File "<pyshell#56>", line 1, in <module>
#    True / False
#ZeroDivisionError: division by zero
```

Numbers
-------

You can use the `type()` function to check the type of any value or variable.

Similarly, you can use the `isinstance()` function to check whether a value or variable is of a given type.

Adding an `int` to an `int` yields an `int`. Adding an `int` to a `float` yields a `float`. Python coerces the `int` into a `float` to perform the addition, then returns a `float` as the result.

Coercing Integers To Floats And Vice-Versa
------------------------------------------

```python
float(2)
#2.0
int(2.0)
#2
int(2.5)
#2
int(-2.5)
#-2
1.12345678901234567890  
#1.1234567890123457
type(1000000000000000)  
#<class 'int'>
```

Common Numerical Operations
---------------------------

```python
11 / 2
#5.5
11 // 2
#5
−11 // 2
#−6
11.0 // 2
#5.0
11 ** 2
#121
11 % 2
#1
```

Fractions
---------

```python
import fractions
x = fractions.Fraction(1, 3)
x
#Fraction(1, 3)
x * 2
#Fraction(2, 3)
fractions.Fraction(6, 4)
#Fraction(3, 2)
fractions.Fraction(0, 0)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "fractions.py", line 96, in __new__
#    raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
#ZeroDivisionError: Fraction(0, 0)
```

Trigonometry
------------

```python
import math
math.pi
#3.141592653589793
math.sin(math.pi / 2)
#1.0
math.tan(math.pi/4)
#0.9999999999999999
```

**Note**: Python does not have infinite precision. `tan(π / 4)` should return `1.0`, not 0.99999999999999999.

Numbers In A Boolean Context
----------------------------

Zero values are false, and non-zero values are true.
