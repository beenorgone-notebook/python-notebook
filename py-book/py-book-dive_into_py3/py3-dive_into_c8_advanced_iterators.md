# Dive into Python 3: Advanced Iterators

<http://www.diveintopython3.net/advanced-iterators.html>

<!-- toc -->

- [Dive into Python 3: Advanced Iterators](#dive-into-python-3-advanced-iterators)
	- [Finding all occurrences of a pattern](#finding-all-occurrences-of-a-pattern)
	- [Finding the unique items in a sequence](#finding-the-unique-items-in-a-sequence)
	- [Making Assertions](#making-assertions)
	- [Generator Expressions](#generator-expressions)
	- [Calculating Permutations... The Lazy Way!](#calculating-permutations-the-lazy-way)
	- [Other fun stuff in the `itertools` module](#other-fun-stuff-in-the-itertools-module)
	- [A new kind of string manipulation](#a-new-kind-of-string-manipulation)
	- [Evaluating Arbitrary Strings As Python Expressions](#evaluating-arbitrary-strings-as-python-expressions)
	- [Putting It All Together](#putting-it-all-together)
	- [Further Reading](#further-reading)

<!-- tocstop -->

 Just as regular expressions put strings on steroids, the `itertools` module puts iterators on steroids. Let's see a classic puzzle:

```
HAWAII + IDAHO + IOWA + OHIO == STATES
510199 + 98153 + 9301 + 3593 == 621246

H = 5
A = 1
W = 0
I = 9
D = 8
O = 3
S = 6
T = 2
E = 4
```

Puzzles like this are called _cryptarithms_ or _alphametics_. The letters spell out actual words, but if you replace each letter with a digit from 0–9, it also "spells" an arithmetic equation. The trick is to figure out which letter maps to each digit. All the occurrences of each letter must map to the same digit, no digit can be repeated, and no "word" can start with the digit 0.

> The most well-known alphametic puzzle is SEND + MORE = MONEY.

In this chapter, we'll dive into an incredible Python program originally written by Raymond Hettinger. This program solves alphametic puzzles _in just 14 lines of code_.

```python
import re
import itertools

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)
```

```python
alphametics.solve('SEND + MORE == MONEY')
#'9567 + 1085 == 10652'
alphametics.solve('PIG + FOX == LOVE')
#'254 + 809 == 1063'
alphametics.solve('BOOB + BIG == NOBRAIN')
#nothing
```

## Finding all occurrences of a pattern

The first thing this alphametics solver does is find all the letters (A–Z) in the puzzle using `findall()` and `upper()` function.

## Finding the unique items in a sequence

Sets make it trivial to find the unique items in a sequence.

```python
a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
set(a_list)
#{'sixth', 'The', "sheep's", 'sick', "sheik's"}
a_string = 'EAST IS EAST'
set(a_string)
#{'A', ' ', 'E', 'I', 'S', 'T'}
words = ['SEND', 'MORE', 'MONEY']
''.join(words)
#Return a string which is the concatenation of the strings in `words`.
#The separator between elements is `` (no separator).
#'SENDMOREMONEY'
set(''.join(words))
#{'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
```

Given a list, a string or a list of string, using `set()` with some twists we can return all the unique characters in them, with no duplicates.

## Making Assertions

Like many programming languages, Python has an `assert` statement. Here's how it works.

```python
assert 1 + 1 == 2
assert 1 + 1 == 3
#Traceback (most recent call last):
#  File "<pyshell#25>", line 1, in <module>
#    assert 1 + 1 == 3
#AssertionError
assert 2+2 == 5, "Only for very large values of 2"
#Traceback (most recent call last):
#  File "<pyshell#27>", line 1, in <module>
#    assert 2+2 == 5, "Only for very large values of 2"
#AssertionError: Only for very large values of 2
```

1\. The `assert` statement is followed by any valid Python expression. In this case, the expression `1 + 1 == 2` evaluates to `True`, so the `assert` statement does nothing.

2\. However, if the Python expression evaluates to `False`, the assert statement will raise an `AssertionError`.

3\. You can also include a human-readable message that is printed if the `AssertionError` is raised.

Therefore, this line of code:

```python
assert len(unique_characters) <= 10, 'Too many letters'
```

... is equivalent to this:

```python
if len(unique_characters) > 10:
    raise AssertionError('Too many letters')
```

The alphametics solver uses this exact assert statement to bail out early if the puzzle contains more than ten unique letters. Since each letter is assigned a unique digit, and there are only ten digits, a puzzle with more than ten unique letters can not possibly have a solution.

## Generator Expressions

A generator expression is like a generator function without the function.

```python
unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
gen = (ord(c) for c in unique_characters)
gen
#<generator object <genexpr> at 0x7f79255fceb8>
gen()
#Traceback (most recent call last):
#  File "<pyshell#31>", line 1, in <module>
#    gen()
#TypeError: 'generator' object is not callable
next(gen)
#78
next(gen)
#79
next(gen)
#68
next(gen)
#82
print(gen)
#<generator object <genexpr> at 0x7f79255fceb8>
tuple(gen)
#(77, 69, 83, 89)
gen
#<generator object <genexpr> at 0x7f79255fceb8>
next(gen)
#Traceback (most recent call last):
#  File "<pyshell#40>", line 1, in <module>
#    next(gen)
#StopIteration
gen
#<generator object <genexpr> at 0x7f79255fceb8>
tuple(ord(c) for c in unique_characters)
#(78, 79, 68, 82, 77, 69, 83, 89)
```

1\. A generator expression is like an anonymous function that yields values. _The expression itself looks like a list comprehension, but it's wrapped in parentheses instead of square brackets._

2\. The generator expression returns... an iterator.

3\. Calling `next(gen)` returns the next value from the iterator.

4\. If you like, you can iterate through all the possible values and return a tuple, list, or set, by passing the generator expression to `tuple()`, `list()`, or `set()`.

```python
unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
gen = (ord(c) for c in unique_characters)
tuple(gen)
#(78, 79, 68, 82, 77, 69, 83, 89)
next(gen)
#Traceback (most recent call last):
#  File "<pyshell#47>", line 1, in <module>
#    next(gen)
#StopIteration
```

> Using a generator expression instead of a list comprehension can save both `cpu` and `ram`. If you're building an list just to throw it away (e.g. passing it to `tuple()` or `set()`), use a generator expression instead!

Here's another way to accomplish the same thing, using a generator function:

```python
def ord_map(a_string):
    for c in a_string:
        yield ord(c)

gen = ord_map(unique_characters)
```

The generator expression is more compact but functionally equivalent.

## Calculating Permutations... The Lazy Way!

> In mathematics, the notion of permutation relates to _the act of arranging all the members of a set into some sequence or order, or if the set is already ordered, rearranging (reordering) its elements_, a process called permuting. These differ from combinations, which are selections of some members of a set where order is disregarded. For example, written as tuples, there are six permutations of the set {1,2,3}, namely: (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), and (3,2,1). These are all the possible orderings of this three element set. As another example, an anagram of a word, all of whose letters are different, is a permutation of its letters. In this example, the letters are already ordered in the original word and the anagram is a reordering of the letters. The study of permutations of finite sets is a topic in the field of combinatorics. ([Permutations, Wikipedia](https://www.wikiwand.com/en/Permutation))

The idea is that you take a list of things (could be numbers, could be letters, could be dancing bears) and find all the possible ways to split them up into smaller lists. All the smaller lists have the same size, which can be as small as 1 and as large as the total number of items.

```python
import itertools
perms = itertools.permutations([1,2,3],2)
next(perms)
#(1, 2)
next(perms)
#(1, 3)
next(perms)
#(2, 1)
next(perms)
#(2, 3)
next(perms)
#(3, 1)
next(perms)
#(3, 2)
next(perms)
#Traceback (most recent call last):
#  File "<pyshell#70>", line 1, in <module>
#    next(perms)
#StopIteration
perms2 = itertools.permutations([2,1,4])
next(perms2)
#(2, 1, 4)
next(perms2)
#(2, 4, 1)
next(perms2)
#(1, 2, 4)
```

The `permutations()` function takes a sequence (here a list of three integers) and a number, which is the number of items you want in each smaller group. The function returns an iterator, which you can use in a `for` loop or any old place that iterates.

The `permutations()` function doesn't have to take a list. It can take any sequence -- even a string.

```python
perms = itertools.permutations('ABC',3)
>>> next(perms)
('A', 'B', 'C')
>>> next(perms)
('A', 'C', 'B')
>>> next(perms)
('B', 'A', 'C')
>>> next(perms)
('B', 'C', 'A')
>>> next(perms)
('C', 'A', 'B')
>>> next(perms)
('C', 'B', 'A')
>>> next(perms)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    next(perms)
StopIteration
>>> list(perms)
[]
>>> list(itertools.permutations('ABC',3))
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

1\. A string is just a sequence of characters. For the purposes of finding permutations, the string `'ABC'` is equivalent to the list `['A', 'B', 'C']`.

2\. Since the `permutations()` function always returns an iterator, an easy way to debug permutations is to pass that iterator to the built-in `list()` function to see all the permutations immediately.

## Other fun stuff in the `itertools` module

```python
>>> list(itertools.product('ABC', '123'))
[('A', '1'), ('A', '2'), ('A', '3'), ('B', '1'), ('B', '2'), ('B', '3'), ('C', '1'), ('C', '2'), ('C', '3')]
>>> list(itertools.combinations('ABC', 2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

1\. The `itertools.product()` function returns an iterator containing the Cartesian product of two sequences.

2\. The `itertools.combinations()` function returns an iterator containing all the possible combinations of the given sequence of the given length.

- This is like the `itertools.permutations()` function, except combinations don't include items that are duplicates of other items in a different order.
- So `itertools.permutations('ABC', 2)` will return both `('A', 'B')` and `('B', 'A')` (among others), but itertools.combinations `('ABC', 2)` will not return `('B', 'A')` because it is a duplicate of `('A', 'B')` in a different order.

```python
>>> names = list(open('favorite-people.txt', encoding='utf-8'))
>>> names
['Dora\n', 'Ethan\n', 'Wesley\n', 'John\n', 'Anne\n', 'Mike\n', 'Chris\n', 'Sarah\n', 'Alex\n', 'Lizzie\n']
>>> names = [name.rstrip() for name in names]
>>> names
['Dora', 'Ethan', 'Wesley', 'John', 'Anne', 'Mike', 'Chris', 'Sarah', 'Alex', 'Lizzie']
>>> names = sorted(names)
>>> names
['Alex', 'Anne', 'Chris', 'Dora', 'Ethan', 'John', 'Lizzie', 'Mike', 'Sarah', 'Wesley']
>>> names = sorted(names, key=len)
>>> names
['Alex', 'Anne', 'Dora', 'John', 'Mike', 'Chris', 'Ethan', 'Sarah', 'Lizzie', 'Wesley']
```

1\. Unfortunately (for this example), the `list(open(filename))` idiom also includes the carriage returns at the end of each line. This list comprehension uses the `rstrip()` string method to strip trailing whitespace from each line. (Strings also have an `lstrip()` method to strip leading whitespace, and a `strip()` method which strips both.)

**Read more** here:

- <http://python-reference.readthedocs.io/en/latest/docs/str/rstrip.html>
- <http://python-reference.readthedocs.io/en/latest/docs/str/strip.html>
- <http://python-reference.readthedocs.io/en/latest/docs/str/lstrip.html>

2\. The `sorted()` function takes a list and returns it sorted. By default, it sorts alphabetically.

But the `sorted()` function can also take a function as the key parameter, and it sorts by that key. In this case, the sort function is `len()`, so it sorts by `len(each item)`. Shorter names come first, then longer, then longest.

**Read more** here: <https://docs.python.org/3/howto/sorting.html>

Continuing from the previous interactive shell...

```python
import itertools
>>> groups = itertools.groupby(names,len)
>>> groups
<itertools.groupby object at 0x7fc00d6788b8>
>>> list(groups)
[(4, <itertools._grouper object at 0x7fc00d67ef98>), (5, <itertools._grouper object at 0x7fc00d67b5c0>), (6, <itertools._grouper object at 0x7fc00d67b5f8>)]
>>> groups = itertools.groupby(names, len)
>>> for name_length, name_iter in groups:
    print('Names with {0:d} letters:'.format(name_length))
    for name in name_iter:
        print(name)

Names with 4 letters:
Alex
Anne
Dora
John
Mike
Names with 5 letters:
Chris
Ethan
Sarah
Names with 6 letters:
Lizzie
Wesley
```

1\. The `itertools.groupby()` function takes a sequence and a key function, and returns an iterator that generates pairs. Each pair contains the result of `key_function(each item)` and another iterator containing all the items that shared that key result.

2\. Calling the `list()` function "exhausted" the iterator, i.e. you've already generated every item in the iterator to make the list. There's no "reset" button on an iterator; you can't just start over once you've exhausted it. If you want to loop through it again (say, in the upcoming `for` loop), you need to call `itertools.groupby()` again to create a new iterator.

3\. In this example, given a list of names _already sorted by length_, `itertools.groupby(names, len)` will put all the 4-letter names in one iterator, all the 5-letter names in another iterator, and so on. The `groupby()` function is completely generic; it could group strings by first letter, numbers by their number of factors, or any other key function you can think of.

> The `itertools.groupby()` function only works if the input sequence is already sorted by the grouping function. In the example above, you grouped a list of names by the len() function. That only worked because the input list was already sorted by length.

```python
>>> list(range(0, 3))
[0, 1, 2]
>>> list(range(10, 13))
[10, 11, 12]
>>> list(itertools.chain(range(0, 3), range(10, 13)))        
[0, 1, 2, 10, 11, 12]
>>> list(zip(range(0, 3), range(10, 13)))                    
[(0, 10), (1, 11), (2, 12)]
>>> list(zip(range(0, 3), range(10, 14)))                    
[(0, 10), (1, 11), (2, 12)]
>>> list(itertools.zip_longest(range(0, 3), range(10, 14)))  
[(0, 10), (1, 11), (2, 12), (None, 13)]
```

1\. The `itertools.chain()` function takes two iterators and returns an iterator that contains all the items from the first iterator, followed by all the items from the second iterator. (Actually, it can take any number of iterators, and it chains them all in the order they were passed to the function.)

2\. The `zip()` function does something prosaic that turns out to be extremely useful: it takes any number of sequences and returns an iterator which returns tuples of the first items of each sequence, then the second items of each, then the third, and so on.

3\. The `zip()` function stops at the end of the shortest sequence. `range(10, 14)` has 4 items (10, 11, 12, and 13), but `range(0, 3)` only has 3, so the `zip()` function returns an iterator of 3 items.

4\. On the other hand, the `itertools.zip_longest()` function stops at the end of the longest sequence, inserting `None` values for items past the end of the shorter sequences.

How does it relate to the alphametics solver?

```python
>>> characters = ('S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y')
>>> guess = ('1', '2', '0', '3', '4', '5', '6', '7')
>>> tuple(zip(characters, guess))
(('S', '1'), ('M', '2'), ('E', '0'), ('D', '3'), ('O', '4'), ('N', '5'), ('R', '6'), ('Y', '7'))
>>> dict(zip(characters, guess))
{'D': '3', 'N': '5', 'E': '0', 'R': '6', 'M': '2', 'S': '1', 'Y': '7', 'O': '4'}
```

1\. Given a list of letters and a list of digits (each represented here as 1-character strings), the `zip` function will create a pairing of letters and digits, in order.

2\. That data structure happens to be exactly the right structure to pass to the `dict()` function to create a dictionary that uses letters as keys and their associated digits as values. (This isn't the only way to do it, of course. You could use a dictionary comprehension to create the dictionary directly).

3\. The alphametics solver uses this technique to create a dictionary that maps letters in the puzzle to digits in the solution, for each possible solution.

```python
characters = tuple(ord(c) for c in sorted_characters)
digits = tuple(ord(c) for c in '0123456789')
...
for guess in itertools.permutations(digits, len(characters)):
    ...
    equation = puzzle.translate(dict(zip(characters, guess)))
```

BUT WHAT IS THIS `translate()` METHOD?

## A new kind of string manipulation

```python
>>> translation_table = {ord('A'): ord('O')}  
>>> translation_table                         
{65: 79}
>>> 'MARK'.translate(translation_table)       
'MORK'
```

1\. String translation starts with a translation table, which is just a dictionary that maps one character to another. Actually, "character" is incorrect -- the translation table really maps one _byte_ to another.

2\. Remember, bytes in Python 3 are integers. The `ord()` function returns the `ascii` value of a character, which, in the case of A–Z, is always a byte from 65 to 90.

3\. The `translate()` method on a string takes a translation table and runs the string through it. That is, it replaces all occurrences of the keys of the translation table with the corresponding values. In this case, "translating" `MARK` to `MORK`.

What does this have to do with solving alphametic puzzles? As it turns out, everything.

```python
>>> characters = tuple(ord(c) for c in 'SMEDONRY')
>>> characters
(83, 77, 69, 68, 79, 78, 82, 89)
>>> guess = tuple(ord(c) for c in '91570682')
>>> guess
(57, 49, 53, 55, 48, 54, 56, 50)
>>> translation_table = dict(zip(characters, guess))
>>> translation_table
{82: 56, 83: 57, 68: 55, 69: 53, 89: 50, 77: 49, 78: 54, 79: 48}
>>> 'SEND + MORE == MONEY'.translate(translation_table)
'9567 + 1085 == 10652'
```

1\. Using a generator expression, we quickly compute the byte values for each character in a string. `characters` is an example of the value of `sorted_characters` in the `alphametics.solve()` function.

2\. Using another generator expression, we quickly compute the byte values for each digit in this string. The result, `guess`, is of the form returned by the `itertools.permutations()` function in the `alphametics.solve()` function.

3\. This translation table is generated by zipping characters and guess together and building a dictionary from the resulting sequence of pairs. This is exactly what the `alphametics.solve()` function does inside the `for` loop.

4\. Finally, we pass this translation table to the `translate()` method of the original puzzle string. This converts each letter in the string to the corresponding digit (based on the letters in `characters` and the digits in `guess`). The result is a valid Python expression, as a string.

That's pretty impressive. But what can you do with a string that happens to be a valid Python expression?

## Evaluating Arbitrary Strings As Python Expressions

After all that fancy string manipulation, we're left with a string like `'9567 + 1085 == 10652'`. But that's a string, and what good is a string? Enter `eval()`, the universal Python evaluation tool.

```python
>>> eval('1 + 1 == 2')
True
>>> eval('1 + 1 == 3')
False
>>> eval('9567 + 1085 == 10652')
True
>>> eval('"A" + "B"')
'AB'
>>> eval('"MARK".translate({65: 79})')
'MORK'
>>> eval('"AAAAA".count("A")')
5
>>> eval('["*"] * 5')
['*', '*', '*', '*', '*']
>>> x = 5
>>> eval("x * 5")         
25
>>> eval("pow(x, 2)")     
25
>>> import math
>>> eval("math.sqrt(x)")  
2.2360679774997898
```

```python
>>> import subprocess
>>> eval ("subprocess.getoutput('ls ~')")
'Desktop\nDocuments\nDownloads\nFoxitSoftware\nMusic\nPictures\nPublic\nTemplates\nVideos'
```

- The subprocess module allows you to run arbitrary shell commands and get the result as a Python string.
- Arbitrary shell commands can have permanent consequences.

It's even worse than that, because there's a global `__import__()` function that takes a module name as a string, imports the module, and returns a reference to it. Combined with the power of `eval()`, you can construct a single expression that will wipe out all your files:

```python
>>> eval("__import__('subprocess').getoutput('rm /some/random/file')")
```

`eval()` IS EVIL

the evil part is evaluating arbitrary expressions from untrusted sources. You should only use `eval()` on trusted input. Of course, the trick is figuring out what's "trusted." But here's something I know for certain: you should **NOT** take this alphametics solver and put it on the Internet as a fun little web service. Don't make the mistake of thinking, "Gosh, the function does a lot of string manipulation before getting a string to evaluate; _I can't imagine_ how someone could exploit that." Someone WILL figure out how to sneak nasty executable code past all that string manipulation ([stranger things have happened](http://www.securityfocus.com/blogs/746)), and then you can kiss your server goodbye.

But surely there's some way to evaluate expressions safely? To put `eval()` in a sandbox where it can't access or harm the outside world? Well, yes and no.

```python
>>> x = 5
>>> eval("x * 5",{},{})
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    eval("x * 5",{},{})
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
>>> eval("x * 5",{"x":x}, {})
25
>>> import math
>>> eval("math.sqrt(x)", {"x": x}, {})
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    eval("math.sqrt(x)", {"x": x}, {})
  File "<string>", line 1, in <module>
NameError: name 'math' is not defined
>>> eval("math.sqrt(x)", {"x": x}, {"math": math})
2.23606797749979
```

1\. The second and third parameters passed to the `eval()` function act as the global and local namespaces for evaluating the expression. In this case, they are both empty, which means that when the string `"x * 5"` is evaluated, there is no reference to `x` in either the global or local namespace, so `eval()` throws an exception.

2\. You can selectively include specific values in the global namespace by listing them individually. Then those -- and only those -- variables will be available during evaluation.

3\. Even though you just imported the math module, you didn't include it in the namespace passed to the `eval()` function, so the evaluation failed.

```python
>>> eval("pow(5,2)", {}, {})
25
>>> eval("__import__('math').sqrt(5)", {}, {})
2.23606797749979
```

1\. All of Python's built-in functions are still available during evaluation. So `pow(5, 2)` works, because `5` and `2` are literals, and `pow()` is a built-in function.

2\. Unfortunately (and if you don't see why it's unfortunate, read on), the `__import__()` function is also a built-in function, so it works too.

Yeah, that means you can still do nasty things, even if you explicitly set the global and local namespaces to empty dictionaries when calling `eval()`:

```python
eval("__import__('subprocess').getoutput('rm /some/random/file')", {}, {})
```

Is there _any_ way to use `eval()` safely? Well, yes and no.

```python
>>>eval("__import__('math').sqrt(5)", {"__builtins__":None}, {})
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    eval("__import__('math').sqrt(5)", {"__builtins__":None}, {})
  File "<string>", line 1, in <module>
TypeError: 'NoneType' object is not subscriptable

>>> eval("__import__('subprocess').getoutput('rm -rf /')", {"__builtins__":None}, {})
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    eval("__import__('subprocess').getoutput('rm -rf /')", {"__builtins__":None}, {})
  File "<string>", line 1, in <module>
TypeError: 'NoneType' object is not subscriptable
```

1\. To evaluate untrusted expressions safely, you need to define a global namespace dictionary that maps `"__builtins__"` to `None`, the Python null value. Internally, the "built-in" functions are contained within a pseudo-module called `"__builtins__"`. This pseudo-module (i.e. the set of built-in functions) is made available to evaluated expressions unless you explicitly override it.

2\. Be sure you've overridden `__builtins__`. Not `__builtin__`, `__built-ins__`, or some other variation that will work just fine but expose you to catastrophic risks.

So `eval()` is safe now? Well, yes and no.

```python
>>> eval("2 ** 2147483647",
...     {"__builtins__":None}, {})
```

Even without access to `__builtins__`, you can still launch a denial-of-service attack. For example, trying to raise `2` to the `2147483647th` power will spike your server's cpu utilization to 100% for quite some time. (If you're trying this in the interactive shell, press `Ctrl-C` a few times to break out of it.) Technically this expression will return a value eventually, but in the meantime your server will be doing a whole lot of nothing.

In the end, it is possible to safely evaluate untrusted Python expressions, for some definition of "safe" that turns out not to be terribly useful in real life. It's fine if you're just playing around, and it's fine if you only ever pass it trusted input. But anything else is just asking for trouble.

## Putting It All Together

To recap: this program solves alphametic puzzles by brute force, i.e. through an exhaustive search of all possible solutions. To do this, it...

1. Finds all the letters in the puzzle with the `re.findall()` function
2. Find all the unique letters in the puzzle with sets and the `set()` function
3. Checks if there are more than 10 unique letters (meaning the puzzle is definitely unsolvable) with an `assert` statement
4. Converts the letters to their `ASCII` equivalents with a generator object
5. Calculates all the possible solutions with the `itertools.permutations()` function
6. Converts each possible solution to a Python expression with the `translate()` string method
7. Tests each possible solution by evaluating the Python expression with the `eval()` function
8. Returns the first solution that evaluates to `True`

...in just 14 lines of code.

## Further Reading

- [`itertools` module](http://docs.python.org/3.1/library/itertools.html)
- [`itertools` -- Iterator functions for efficient looping](http://www.doughellmann.com/PyMOTW/itertools)
- [Watch Raymond Hettinger's "Easy AI with Python" talk](http://blip.tv/file/1947373) at PyCon 2009
- [Recipe 576615: Alphametics solver](http://code.activestate.com/recipes/576615), Raymond Hettinger's original alphametics solver for Python 2
- [More of Raymond Hettinger's recipes](http://code.activestate.com/recipes/users/178123) in the ActiveState Code repository
- [Alphametics on Wikipedia](http://en.wikipedia.org/wiki/Verbal_arithmetic)
- [Alphametics Index](http://www.tkcs-collins.com/truman/alphamet/index.shtml), including [lots of puzzles](http://www.tkcs-collins.com/truman/alphamet/alphamet.shtml) and [a generator to make your own](http://www.tkcs-collins.com/truman/alphamet/alpha_gen.shtml)
