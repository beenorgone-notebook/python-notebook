[Dive into Python 3: Unit Testing](http://www.diveintopython3.net/unit-testing.html)
====================================================================================

[The rules for Roman numerals](http://www.diveintopython3.net/regular-expressions.html#romannumerals) lead to a number of interesting observations:

1.	There is only one correct way to represent a particular number as a Roman numeral.
2.	The converse is also true: if a string of characters is a valid Roman numeral, it represents only one number (that is, it can only be interpreted one way).
3.	There is a limited range of numbers that can be expressed as Roman numerals, specifically 1 through 3999. The Romans did have several ways of expressing larger numbers, for instance by having a bar over a numeral to represent that its normal value should be multiplied by 1000. For the purposes of this chapter, let’s stipulate that Roman numerals go from 1 to 3999.
4.	There is no way to represent 0 in Roman numerals.
5.	There is no way to represent negative numbers in Roman numerals.
6.	There is no way to represent fractions or non-integer numbers in Roman numerals.

What a `roman.py` module should do. It will have two main functions, `to_roman()` and `from_roman()`. The `to_roman()` function should take an integer from 1 to 3999 and return the Roman numeral representation as a string…

Now let’s do something a little unexpected: write a test case that checks whether the `to_roman()` function does what you want it to.

This is called *test-driven development*, or `TDD`. The set of two conversion functions — to_roman(), and later from_roman() — can be written and tested as a unit, separate from any larger program that imports them. Python has a framework for unit testing, the appropriately-named `unittest` module.

-	Before writing code, writing unit tests forces you to detail your requirements in a useful fashion.
-	While writing code, unit tests keep you from over-coding. When all the test cases pass, the function is complete.
-	When refactoring code, they can help prove that the new version behaves the same way as the old version.
-	When maintaining code, having tests will help you cover your ass when someone comes screaming that your latest change broke their old code. (“But sir, all the unit tests passed when I checked it in...”)
-	When writing code in a team, having a comprehensive test suite dramatically decreases the chances that your code will break someone else’s code, because you can run their unit tests first. (I’ve seen this sort of thing in code sprints. A team breaks up the assignment, everybody takes the specs for their task, writes unit tests for it, then shares their unit tests with the rest of the team. That way, nobody goes off too far into developing code that doesn’t play well with others.)

A single question
-----------------

A test case answers a single question about the code it is testing. A test case should be able to...

-	...run completely by itself, without any human input. **Unit testing is about automation.**
-	...determine by itself whether the function it is testing has passed or failed, without a human interpreting the results.
-	...run in isolation, separate from any other test cases (even if they test the same functions). **Each test case is an island.**

Given that, let’s build a test case for the first requirement:

1.	The `to_roman()` function should return the Roman numeral representation for all integers 1 to 3999.

```python
import roman1
import unittest

class KnownValues(unittest.TestCase):
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman1.to_roman(integer)
            self.assertEqual(numeral, result)

if __name__ == '__main__':
    unittest.main()
```

1\. To write a test case, first subclass the `TestCase` class of the `unittest` module. This class provides many useful methods which you can use in your test case to test specific conditions.

2\. `known_values` includes the lowest ten numbers, the highest number, every number that translates to a single-character Roman numeral, and a random sampling of other valid numbers. You don’t need to test every possible input, but you should try to test all the obvious edge cases.

3\. Every individual test is its own method.

-	A test method takes no parameters, returns no value, and must have a name beginning with the four letters `test`.
-	If a test method exits normally without raising an exception, the test is considered passed; if the method raises an exception, the test is considered failed.

4\. The `to_roman()` function hasn't been written yet, but you can call it in the test method.

-	Notice that you have now defined the `API` for the `to_roman()` function:
	-	it must take an integer (the number to convert) and return a string (the Roman numeral representation).
	-	If the `api` is different than that, this test is considered failed.
-	Also notice that you are not trapping any exceptions when you call `to_roman()`. This is intentional.
	-	`to_roman()` shouldn’t raise an exception when you call it with valid input, and these input values are all valid.
	-	If to_roman() raises an exception, this test is considered failed.

5\. Assuming the `to_roman()` function was defined correctly, called correctly, completed successfully, and returned a value, the last step is to check whether it returned the *right* value. This is a common question, and the `TestCase` class provides a method, `assertEqual`, to check whether two values are equal. If the result returned from `to_roman()` (`result`) does not match the known value you were expecting (`numeral`), `assertEqual` will raise an exception and the test will fail. If the two values are equal, `assertEqual` will do nothing. If every value returned from to_roman() matches the known value you expect, `assertEqual` never raises an exception, so `test_to_roman_known_values` eventually exits normally, which means `to_roman()` has passed this test.

Once you have a test case, you can start coding the `to_roman()` function.

-	First, you should stub it out as an empty function and make sure the tests fail.
-	If the tests succeed before you’ve written any code, your tests aren’t testing your code at all!
-	Unit testing is a dance: tests lead, code follows.

> Write a test that fails, then code until it passes.

```python
# roman1.py

def to_roman(n):
    '''convert integer to Roman numeral'''
    pass
```

At this stage, you want to define the `api` of the `to_roman()` function, but you don’t want to code it yet. (Your test needs to fail first.) To stub it out, use the Python reserved word `pass`, which does precisely nothing.

```
======================================================================
FAIL: test_to_roman_known_values (__main__.KnownValues)
to_roman should give known result with known input
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-into/examples/romantest1.py", line 73, in test_to_roman_known_values
    self.assertEqual(numeral, result)
AssertionError: 'I' != None

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
[Finished in 0.4s]
```

1\. Running the script runs `unittest.main()`, which runs each test case. Each test case is a method within a class in `romantest.py`. There is no required organization of these test classes; they can each contain a single test method, or you can have one class that contains multiple test methods. The only requirement is that each test class must inherit from `unittest.TestCase`.

2\. For each test case, the `unittest` module will print out the `docstring` of the method and whether that test passed or failed. As expected, this test case fails.

3\. For each failed test case, `unittest` displays the trace information showing exactly what happened. In this case, the call to `assertEqual()` raised an `AssertionError` because it was expecting `to_roman(1)` to return `'I'`, but it didn’t. (Since there was no explicit return statement, the function returned `None`, the Python null value.)

4\. After the detail of each test, `unittest` displays a summary of how many tests were performed and how long it took.

5\. Overall, the test run failed because at least one test case did not pass. When a test case doesn’t pass, `unittest` distinguishes between failures and errors. A failure is a call to an `assertXYZ` method, like `assertEqual` or `assertRaises`, that fails because the asserted condition is not true or the expected exception was not raised. An error is any other sort of exception raised in the code you’re testing or the unit test case itself.

*Now*, finally, you can write the `to_roman()` function.

```python
roman_numeral_map = (('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1))

def to_roman():
    '''convert integer to Roman numeral'''
    result =''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result
```

1\. `roman_numeral_map` is a tuple of tuples which defines three things:

-	the character representations of the most basic Roman numerals;
-	the order of the Roman numerals (in descending value order, from `M` all the way down to `I`);
-	the value of each Roman numeral.

Each inner tuple is a pair of (numeral, value). It’s not just single-character Roman numerals; it also defines two-character pairs like `CM` (“one hundred less than one thousand”). This makes the `to_roman()` function code simpler.

2\. Here’s where the rich data structure of `roman_numeral_map` pays off, because you don’t need any special logic to handle the subtraction rule. To convert to Roman numerals, simply iterate through `roman_numeral_map` looking for the largest integer value less than or equal to the input. Once found, add the Roman numeral representation to the end of the output, subtract the corresponding integer value from the input, lather, rinse, repeat.

```
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
[Finished in 0.19s]
python_3--dive-into/python_3--dive-into_c9-unit-testing.md210:302
LF
Insert
UTF-84 SpacesGitHub Markdown1 update
```

The `to_roman()` function passes the “known values” test case. It’s not comprehensive, but it does put the function through its paces with a variety of inputs, including inputs that produce every single-character Roman numeral, the largest possible input (3999), and the input that produces the longest possible Roman numeral (3888). At this point, you can be reasonably confident that the function works for any good input value you could throw at it. WHAT ABOUT BAD INPUT?

Halt and Catch Fire
-------------------

It is not enough to test that functions succeed when given good input; you must also test that they fail when given bad input. And not just any sort of failure; they must fail in the way you expect.

```python
>>> import roman1
>>> roman1.to_roman(4000)
'MMMM'
>>> roman1.to_roman(5000)
'MMMMM'
>>> roman1.to_roman(9000)
'MMMMMMMMM'
```

That’s definitely not what you wanted — that’s not even a valid Roman numeral! In fact, each of these numbers is outside the range of acceptable input, but the function returns a bogus value anyway. Silently returning bad values is *baaaaaaad*; if a program is going to fail, it is far better if it fails quickly and noisily. “Halt and catch fire,” as the saying goes.

> The Pythonic way to halt and catch fire is to raise an exception.

The question to ask yourself is, “How can I express this as a testable requirement?” How’s this for starters:

-	The `to_roman()` function should raise an `OutOfRangeError` when given an integer greater than `3999`.

```python
import unittest, roman2
class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 4000)
```

1\. Like the previous test case, you create a class that inherits from unittest.TestCase. You can have more than one test per class, but I chose to create a new class here because this test is something different than the last one. We’ll keep all the good input tests together in one class, and all the bad input tests together in another.

2\. Like the previous test case, the test itself is a method of the class, with a name starting with `test`.

3\. The `unittest.TestCase` class provides the `assertRaises` method, which takes the following arguments:

-	the exception you’re expecting,
-	the function you’re testing, and
-	the arguments you’re passing to that function.

(If the function you’re testing takes more than one argument, pass them all to `assertRaises`, in order, and it will pass them right along to the function you’re testing.)

In this last line of code, instead of calling `to_roman()` directly and manually checking that it raises a particular exception (by wrapping it in a `try...except` block), the `assertRaises` method has encapsulated all of that for us. All you do is tell it what exception you’re expecting (`roman2.OutOfRangeError`), the function (`to_roman()`), and the function’s arguments (`4000`). The `assertRaises` method takes care of calling `to_roman()` and checking that it raises `roman2.OutOfRangeError`.

Also note that you’re passing the `to_roman()` function itself as an argument; you’re not calling it, and you’re not passing the name of it as a string. Everything in Python is an object

So what happens when you run the test suite with this new test?

```
======================================================================
ERROR: test_too_large (__main__.ToRomanBadInput)
to_roman should fail with large input
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-into/examples/romantest2.py", line 78, in test_too_large
    self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 4000)
AttributeError: module 'roman1' has no attribute 'OutOfRangeError'

----------------------------------------------------------------------
Ran 2 tests in 0.053s

FAILED (errors=1)
[Finished in 0.261s]
```

1\. A unit test actually has three return values: pass, fail, and error. “Error” means that the code didn’t even execute properly.

2\. Why didn’t the code execute properly? The traceback tells all. The module you’re testing doesn’t have an exception called `OutOfRangeError`. To solve this problem, you need to define the `OutOfRangeError` exception in `roman2.py`.

```python
class OutOfRangeError(ValueError):
    pass
```

1\. Exceptions are classes. An “out of range” error is a kind of value error — the argument value is out of its acceptable range. So this exception inherits from the built-in `ValueError` exception. This is not strictly necessary (it could just inherit from the base Exception class), but it feels right.

2\. Exceptions don’t actually do anything, but you need at least one line of code to make a class. Calling `pass` does precisely nothing, but it’s a line of Python code, so that makes it a class.

Run the test suite again.

```
======================================================================
FAIL: test_too_large (__main__.ToRomanBadInput)
to_roman should fail with large input
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-into/examples/romantest2.py", line 78, in test_too_large
    self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 4000)
AssertionError: OutOfRangeError not raised by to_roman

----------------------------------------------------------------------
Ran 2 tests in 0.017s

FAILED (failures=1)
[Finished in 0.23s]
```

Now you can write the code to make this test pass.

```python
def to_roman(n):
    '''convert integer to Roman numeral'''
    if n > 3999:
        raise OutOfRangeError('number out of range (must be less than 4000)')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result
```

This make the test pass.

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
[Finished in 0.163s]
```

More Halting, More Fire
-----------------------

Along with testing numbers that are too large, you need to test numbers that are too small. As we noted in our functional requirements, Roman numerals cannot express 0 or negative numbers.

```python
>>> import roman2
>>> roman2.to_roman(0)
''
>>> roman2.to_roman(-1)
''
```

Let’s add tests for each of these conditions.

```python
class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, 4000)

    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, 0)

    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, -1)
```

```python
def to_roman(n):
    '''convert integer to Roman numeral'''
    if not (0 < n < 4000):                                              ①
        raise OutOfRangeError('number out of range (must be 1..3999)')  ②

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result
```

`(0 < n < 4000)` is a nice Pythonic shortcut.

And One More Thing…
-------------------

There was one more functional requirement for converting numbers to Roman numerals: dealing with non-integers.

```python
>>> import roman3
>>> roman3.to_roman(0.5)  
''
>>> roman3.to_roman(1.0)  
'I'
```

First, define a `NotIntegerError` exception.

```python
class ToRomanBadInput(unittest.TestCase):
    .
    .
    .
    def test_non_integer(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(roman4.NotIntegerError, roman4.to_roman, 0.5)
```

Now check that the test fails properly. Then write the code that makes the test pass.

```python
def to_roman(n):
    '''convert integer to Roman numeral'''
    if not (0 < n < 4000):
        raise OutOfRangeError('number out of range (must be 1..3999)')
    if not isinstance(n, int):                                          
        raise NotIntegerError('non-integers can not be converted')      

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result
```

Finally, check that the code does indeed make the test pass.

```
test_to_roman_known_values (__main__.KnownValues)
to_roman should give known result with known input ... ok
test_negative (__main__.ToRomanBadInput)
to_roman should fail with negative input ... ok
test_non_integer (__main__.ToRomanBadInput)
to_roman should fail with non-integer input ... ok
test_too_large (__main__.ToRomanBadInput)
to_roman should fail with large input ... ok
test_zero (__main__.ToRomanBadInput)
to_roman should fail with 0 input ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

It's time to move on to `from_roman()`

A Pleasing Symmetry
-------------------
