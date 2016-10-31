[Dive into Python 3: Closures & Generators](http://www.diveintopython3.net/generators.html)
===========================================================================================

**Problem**: Let’s design a Python library that automatically pluralizes English nouns.

We’ll start with just these four rules, but keep in mind that you’ll inevitably need to add more:

1.	If a word ends in S, X, or Z, add ES.
2.	If a word ends in a noisy H, add ES; if it ends in a silent H, just add S.
	-	What’s a noisy H? One that gets combined with other letters to make a sound that you can hear. So coach becomes coaches and rash becomes rashes, because you can hear the CH and SH sounds when you say them.
	-	But cheetah becomes cheetahs, because the H is silent.
3.	If a word ends in Y that sounds like I, change the Y to IES; if the Y is combined with a vowel to sound like something else, just add S. So vacancy becomes vacancies, but day becomes days.
4.	If all else fails, just add S and hope for the best.

Use Regex
---------

```python
def plural(noun):
	if re.search('[sxz]$', noun):
		return re.sub('$', 'es', noun)
	elif re.search('[^aeioudgkprt]h$', noun):
		return re.sub('$', 'es', noun)
	elif re.search('[^aeiou]y$', noun):
		return re.sub('y$', 'ies',noun)
	else:
		return noun + 's'
```

The `^` as the first character inside the square brackets means something special: negation. `[^abc]` means “any single character except a, b, or c”. So `[^aeioudgkprt]` means any character except a, e, i, o, u, d, g, k, p, r, or t. Then that character needs to be followed by h, followed by end of string. You’re looking for words that end in H where the H can be heard.

A List Of Functions
-------------------

```python
import re

def match_sxz(noun):
    return re.search('[sxz]$', noun)

def apply_sxz(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

def apply_h(noun):
    return re.sub('$', 'es', noun)

def match_y(noun):
    return re.search('[^aeiou]y$', noun)

def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

rules = ((match_sxz, apply_sxz),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
         )

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
```

The reason this technique works is that **everything in Python is an object, including functions**. The `rules` data structure contains functions — not names of functions, but actual function objects. When they get assigned in the `for` loop, then `matches_rule` and `apply_rule` are actual functions that you can call.

The benefit here is that the `plural()` function is now simplified. It takes a sequence of rules, defined elsewhere, and iterates through them in a generic fashion.

1.	Get a match rule
2.	Does it match? Then call the apply rule and return the result.
3.	No match? Go to step 1.

The rules could be defined anywhere, in any way. The `plural()` function doesn’t care.

A List Of Patterns
------------------

```python
import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

patterns = \
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')
  )
rules = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
```

A File Of Patterns
------------------

You’ve factored out all the duplicate code and added enough abstractions so that the pluralization rules are defined in a list of strings. The next logical step is to take these strings and put them in a separate file, where they can be maintained separately from the code that uses them.

```txt
[sxz]$               $    es
[^aeioudgkprt]h$     $    es
[^aeiou]y$          y$    ies
$                    $    s
```

```python
import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

rules = []
with open('plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_and_apply_functions(
                pattern, search, replace))

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
```

1.	The global `open()` function opens a file and returns a file object. In this case, the file we’re opening contains the pattern strings for pluralizing nouns.
2.	The `with` statement creates what’s called a *context*: when the `with` block ends, Python will automatically close the file, even if an exception is raised inside the `with` block.
3.	The `for line in <fileobject>` idiom reads data from the open file, one line at a time, and assigns the text to the `line` variable.
4.	Each line in the file really has three values, but they’re separated by whitespace (tabs or spaces, it makes no difference). To split it out, use the `split()` string method.
	1.	The first argument to the `split()` method is None, which means “split on any whitespace (tabs or spaces, it makes no difference).”
	2.	The second argument is `3`, which means “split on whitespace 3 times, then leave the rest of the line alone.”  
	3.	A line like `[sxz]$ $ es` will be broken up into the list `['[sxz]$', '$', 'es']`, which means that pattern will get `[sxz]$`, search will get `$`, and replace will get `es`.

The improvement here is that you’ve completely separated the pluralization rules into an external file, so it can be maintained separately from the code that uses it. Code is code, data is data, and life is good.

Generators
----------

> In computer science, a generator is a special routine that can be used to control the iteration behavior of a loop. In fact, all generators are iterators. A generator is very similar to a function that returns an array, in that a generator has parameters, can be called, and generates a sequence of values. However, instead of building an array containing all the values and returning them all at once, a generator yields the values one at a time, which requires less memory and allows the caller to get started processing the first few values immediately. In short, a generator looks like a function but behaves like an iterator. - [Generator (computer programming)](https://www.wikiwand.com/en/Generator_(computer_programming)) via Wikipedia.

Wouldn’t it be grand to have a generic `plural()` function that parses the rules file? Get rules, check for a match, apply appropriate transformation, go to next rule. That’s all the `plural()` function has to do, and that’s all the `plural()` function should do.

```python
def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename='plural5-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))
```

How the heck does *that* work? Let look at an interactive example of `yield` first:

```python
def make_counter(x):
	print('entering make_counter')
	while True:
		yield x
		print('incrementing x')
		x = x + 1

counter = make_counter(2)
counter
#<generator object make_counter at 0x7f1966e0d7d8>
next(counter)
#entering make_counter
#2
next(counter)
#incrementing x
#3
next(counter)
#incrementing x
#4
```

1.	The presence of the `yield` keyword in `make_counter` means that this is not a normal function. It is a special kind of function which generates values one at a time. You can think of it as a resumable function. Calling it will return a *generator* that can be used to generate successive values of `x`.
2.	The `make_counter()` function returns a generator object.
3.	The `next()` function takes a generator object and returns its next value. The first time you call `next()` with the `counter` generator, it executes the code in `make_counter()` up to the first `yield` statement, then returns the value that was yielded. In this case, that will be `2`, because you originally created the generator by calling `make_counter(2)`.
4.	Repeatedly calling `next()` with the same generator object resumes exactly where it left off and continues until it hits the next `yield` statement. All variables, local state, &c. are saved on `yield` and restored on `next()`. The next line of code waiting to be executed calls `print()`, which prints `incrementing x`. After that, the statement `x = x + 1`. Then it loops through the `while` loop again, and the first thing it hits is the statement `yield x`, which saves the state of everything and returns the current value of `x` (now `3`).
5.	The second time you call `next(counter)`, you do all the same things again, but this time `x` is now `4`.

**`yield` pauses a function. `next()` resumes where it left off.**

### A Fibonacci Generator

```python
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
```

```python
from fibonacci import fib
for n in fib(1000):
	print(n, end=', ')
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
list(fib(1000))
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
```

This is a useful idiom: pass a generator to the `list()` function, and it will iterate through the entire generator (just like the `for` loop in the previous example) and return a list of all the values.

### A Plural Rule Generator

Go back to `plural5.py` above.

```python
def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename='plural5-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))
```

What do you yield? Two functions, built dynamically with your old friend, `build_match_and_apply_functions()`, which is identical to the previous examples. In other words, `rules()` is a generator that spits out match and apply functions *on demand*.

Since `rules()` is a generator, you can use it directly in a `for` loop. The first time through the `for` loop, you will call the `rules()` function, which will open the pattern file, read the first line, dynamically build a match function and an apply function from the patterns on that line, and yield the dynamically built functions. The second time through the `for` loop, you will pick up exactly where you left off in `rules()` (which was in the middle of the `for line in pattern_file` loop). The first thing it will do is read the next line of the file (which is still open), dynamically build another match and apply function based on the patterns on that line in the file, and yield the two functions.

**What have you gained** over stage 4? Startup time. In stage 4, when you imported the plural4 module, it read the entire patterns file and built a list of all the possible rules, before you could even think about calling the `plural()` function. With generators, you can do everything lazily: you read the first rule and create functions and try them, and if that works you don’t ever read the rest of the file or create any other functions.

**What have you lost?** Performance! Every time you call the `plural()` function, the `rules()` generator starts over from the beginning — which means re-opening the patterns file and reading from the beginning, one line at a time.

What if you could have the bests:

1.	minimal startup cost (don't execute any code on `import`\)
2.	maximum performance (don't build the same functions over and over again)
3.	keep the rules in a separate file (because code is code and data is data)
4.	never have to read the same line twice.

To do that, you’ll need to build your own iterator. But before you do that, you need to learn about Python classes.

Further Reading
---------------

-	[PEP 255: Simple Generators](http://www.python.org/dev/peps/pep-0255/)
-	[Understanding Python’s “with” statement](http://effbot.org/zone/python-with-statement.htm)
-	[Closures in Python](http://ynniv.com/blog/2007/08/closures-in-python.html)
-	[Fibonacci numbers](http://en.wikipedia.org/wiki/Fibonacci_number)
-	[Generator (computer programming)](https://www.wikiwand.com/en/Generator_(computer_programming)) via Wikipedia.
