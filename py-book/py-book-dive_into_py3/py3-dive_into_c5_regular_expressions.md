[Dive into Python 3: Regular Expressions](http://www.diveintopython3.net/regular-expressions.html)
==================================================================================================

In Python, strings have methods for searching and replacing: `index()`, `find()`, `split()`, `count()`, `replace()`, &c. But these methods are limited to the simplest of cases. For example, the `index()` method looks for a single, hard-coded substring, and the search is always case-sensitive. To do case-insensitive searches of a string s, you must call `s.lower()` or `s.upper()` and make sure your search strings are the appropriate case to match. The `replace()` and `split()` methods have the same limitations.

If your goal can be accomplished with string methods, you should use them. They’re fast and simple and easy to read. But if you find yourself using a lot of different string functions with if statements to handle special cases, or if you’re chaining calls to `split()` and `join()` to slice-and-dice your strings, you may need to move up to regular expressions.

Regular expressions are a powerful and (mostly) standardized way of searching, replacing, and parsing text with complex patterns of characters. Although the regular expression syntax is tight and unlike normal code, the result can end up being more readable than a hand-rolled solution that uses a long chain of string functions.

Case Study: Street Addresses
----------------------------

**Problem**: Standardize a street address so that 'ROAD' is always abbreviated as 'RD.'

```python
s = '100 NORTH MAIN ROAD'
s.replace('ROAD', 'RD.')
#'100 NORTH MAIN RD.'
s = '100 NORTH BROAD ROAD'
import re
re.sub('ROAD$', 'RD.', s)
#'100 NORTH BROAD RD.'
```

Take a look at the first parameter: `ROAD$`. This is a simple regular expression that matches `ROAD` only when it occurs at the end of a string. The `$` means “end of the string.” (There is a corresponding character, the caret `^`, which means “beginning of the string.”) Using the `re.sub()` function, you search the string `s` for the regular expression 'ROAD$' and replace it with 'RD.'. This matches the ROAD at the end of the string `s`, but does *not* match the ROAD that’s part of the word BROAD, because that’s in the middle of `s`.

```python
s = '100 BROAD'
re.sub('ROAD$', 'RD.', s)
#'100 BRD.'
re.sub('\\bROAD$', 'RD.', s)   
#'100 BROAD'
re.sub(r'\bROAD$', 'RD.', s)   
#'100 BROAD'
s = '100 BROAD ROAD APT. 3'
re.sub(r'\bROAD$', 'RD.', s)   
#'100 BROAD ROAD APT. 3'
re.sub(r'\bROAD\b', 'RD.', s)  
#'100 BROAD RD. APT 3'
```

1.	What I really wanted was to match 'ROAD' when it was at the end of the string and it was its own word (and not a part of some larger word). To express this in a regular expression, you use `\b`, which means “a word boundary must occur right here.” In Python, this is complicated by the fact that the `\` character in a string must itself be escaped. This is sometimes referred to as the backslash plague, and it is one reason why regular expressions are easier in Perl than in Python. On the down side, Perl mixes regular expressions with other syntax, so if you have a bug, it may be hard to tell whether it’s a bug in syntax or a bug in your regular expression.
2.	To work around the backslash plague, you can use what is called a *raw string*, by prefixing the string with the letter `r`. This tells Python that nothing in this string should be escaped; `\t` is a tab character, but r'\t' is really the backslash character `\` followed by the letter `t`. I recommend always using raw strings when dealing with regular expressions; otherwise, things get too confusing too quickly (and regular expressions are confusing enough already).

Case Study: Roman Numerals
--------------------------

-	I = 1
-	V = 5
-	X = 10
-	L = 50
-	C = 100
-	D = 500
-	M = 1000

The following are some general rules for constructing Roman numerals:

-	Sometimes characters are additive. I is 1, II is 2, and III is 3. VI is 6 (literally, “5 and 1”), VII is 7, and VIII is 8.
-	The tens characters (I, X, C, and M) can be repeated up to three times. At 4, you need to subtract from the next highest fives character. You can't represent 4 as IIII; instead, it is represented as IV (“1 less than 5”). 40 is written as XL (“10 less than 50”), 41 as XLI, 42 as XLII, 43 as XLIII, and then 44 as XLIV (“10 less than 50, then 1 less than 5”).
-	Sometimes characters are… the opposite of additive. By putting certain characters before others, you subtract from the final value. For example, at 9, you need to subtract from the next highest tens character: 8 is VIII, but 9 is IX (“1 less than 10”), not VIIII (since the I character can not be repeated four times). 90 is XC, 900 is CM.
-	The fives characters can not be repeated. 10 is always represented as X, never as VV. 100 is always C, never LL.
-	Roman numerals are read left to right, so the order of characters matters very much. DC is 600; CD is a completely different number (400, “100 less than 500”). CI is 101; IC is not even a valid Roman numeral (because you can't subtract 1 directly from 100; you would need to write it as XCIX, “10 less than 100, then 1 less than 10”).

**Problem**: What would it take to validate that an arbitrary string is a valid Roman numeral?

### Checking For Thousands

Since Roman numerals are always written highest to lowest, let’s start with the highest: the thousands place. For numbers 1000 and higher, the thousands are represented by a series of M characters.

```python
import re
parttern ='^M?M?M?$'
pattern = '^M?M?M?$'
re.search(pattern, 'M')
#<_sre.SRE_Match object; span=(0, 1), match='M'>
re.search(pattern, 'MM')
#<_sre.SRE_Match object; span=(0, 2), match='MM'>
re.search(pattern, 'MMM')
#<_sre.SRE_Match object; span=(0, 3), match='MMM'>
re.search(pattern, 'MMMM')
re.search(pattern, '')
#<_sre.SRE_Match object; span=(0, 0), match=''>
```

This pattern has three parts:

-	`^` matches what follows only at the beginning of the string. If this were not specified, the pattern would match no matter where the `M` characters were, which is not what you want. You want to make sure that the `M` characters, if they’re there, are at the beginning of the string.
-	`M?` optionally matches a single `M` character. Since this is repeated three times, you’re matching anywhere from zero to three `M` characters in a row. And
	-	`?` makes a pattern optional.
-	`$` matches the end of the string. When combined with the `^` character at the beginning, this means that the pattern must match the entire string, with no other characters before or after the M characters.

The essence of the `re` module is the `search()` function, that takes a regular expression (`pattern`) and a string (`M`) to try to match against the regular expression. If a match is found, `search()` returns an object which has various methods to describe the match; if no match is found, `search()` returns `None`, the Python null value. All you care about at the moment is whether the pattern matches, which you can tell by just looking at the return value of `search()`. `M` matches this regular expression, because the first optional `M` matches and the second and third optional `M` characters are ignored. Interestingly, an empty string also matches this regular expression, since all the M characters are optional.

### Checking For Hundreds:

The hundreds place is more difficult than the thousands, because there are several mutually exclusive ways it could be expressed, depending on its value.

-	100 = C
-	200 = CC
-	300 = CCC
-	400 = CD
-	500 = D
-	600 = DC
-	700 = DCC
-	800 = DCCC
-	900 = CM

So there are four possible patterns:

-	CM
-	CD
-	Zero to three C characters (zero if the hundreds place is 0)
-	D, followed by zero to three C characters

The last two patterns can be combined:

-	an optional D, followed by zero to three C characters

```python
import re
pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
re.search(pattern, 'MCM')
#<_sre.SRE_Match object; span=(0, 3), match='MCM'>
re.search(pattern, 'MD')
#<_sre.SRE_Match object; span=(0, 2), match='MD'>
re.search(pattern, 'MMMCCC')
#<_sre.SRE_Match object; span=(0, 6), match='MMMCCC'>
re.search(pattern, 'MCMC')
re.search(pattern, '')
#<_sre.SRE_Match object; span=(0, 0), match=''>
```

Using The {n,m} Syntax
----------------------

```python
pattern = '^M{0,3}$'
re.search(pattern, '')
#<_sre.SRE_Match object; span=(0, 0), match=''>
re.search(pattern, 'M')
#<_sre.SRE_Match object; span=(0, 1), match='M'>
re.search(pattern, 'MM')
#<_sre.SRE_Match object; span=(0, 2), match='MM'>
re.search(pattern, 'MMM')
#<_sre.SRE_Match object; span=(0, 3), match='MMM'>
re.search(pattern, 'MMMM')
```

This pattern says: “Match the start of the string, then anywhere from zero to three M characters, then the end of the string.” The 0 and 3 can be any numbers; if you want to match at least one but no more than three M characters, you could say `M{1,3}`.

### Checking For Tens And Ones

```python
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
re.search(pattern, 'MDLV')
#<_sre.SRE_Match object; span=(0, 4), match='MDLV'>
re.search(pattern, 'MMDCLXVI')
#<_sre.SRE_Match object; span=(0, 8), match='MMDCLXVI'>
re.search(pattern, 'MMMDCCCLXXXVIII')
#<_sre.SRE_Match object; span=(0, 15), match='MMMDCCCLXXXVIII'>
re.search(pattern, 'I')
#<_sre.SRE_Match object; span=(0, 1), match='I'>
```

Verbose Regular Expressions
---------------------------

So far you’ve just been dealing with what I’ll call “compact” regular expressions. As you’ve seen, they are difficult to read, and even if you figure out what one does, that’s no guarantee that you’ll be able to understand it six months later. What you really need is inline documentation.

Python allows you to do this with something called verbose regular expressions. A verbose regular expression is different from a compact regular expression in two ways:

-	Whitespace is ignored. Spaces, tabs, and carriage returns are not matched as spaces, tabs, and carriage returns. They’re not matched at all. (If you want to match a space in a verbose regular expression, you’ll need to escape it by putting a backslash in front of it.)
-	Comments are ignored. A comment in a verbose regular expression is just like a comment in Python code: it starts with a `#` character and goes until the end of the line. In this case it’s a comment within a multi-line string instead of within your source code, but it works the same way.

```python
compact_pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
verbose_pattern = '''
^						#beginning of string
M{0,3}					#thousands - 0 to 3 Ms
(CM|CD|D?C{0,3})		#hundreds - 900 (CM), 400(CD), 0-300 (0 to 3 Cs),
						#or 500-800 (D, followed by 0 to 3 Cs)
(XC|XL|L?X{0,3})		#ten - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs)
						#or 50-80 (L, followed by 0 to 3 Xs)
(IX|IV|V?I{0,3})		#ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is)
						#or 5-8 (V, followed by 0 to 3 Is)
$						#end of string
'''

re.search(pattern, 'MDLV', re.VERBOSE)
#<_sre.SRE_Match object; span=(0, 4), match='MDLV'>
re.search(pattern, 'M', re.VERBOSE)
#<_sre.SRE_Match object; span=(0, 1), match='M'>
re.search(pattern, 'MCMLXXXIX', re.VERBOSE)
#<_sre.SRE_Match object; span=(0, 9), match='MCMLXXXIX'>
re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE)
#<_sre.SRE_Match object; span=(0, 15), match='MMMDCCCLXXXVIII'>
```

The most important thing to remember when using verbose regular expressions is that you need to pass an extra argument when working with them: `re.VERBOSE` is a constant defined in the re module that signals that the pattern should be treated as a verbose regular expression.

Case Study: Parsing Phone Numbers
---------------------------------

When a regular expression does match, you can pick out specific pieces of it. You can find out what matched where.

**Problem**: parsing an American phone number. The client wanted to be able to enter the number free-form (in a single field), but then wanted to store the area code, trunk, number, and optionally an extension separately in the company’s database.

Here are the phone numbers you needed to be able to accept:

-	800-555-1212
-	800 555 1212
-	800.555.1212
-	(800) 555-1212
-	1-800-555-1212
-	800-555-1212-1234
-	800-555-1212x1234
-	800-555-1212 ext. 1234
-	work 1-(800) 555.1212 #1234

First step:

```python
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
phonePattern.search('800-555-1212').groups()
#('800', '555', '1212')
phonePattern.search('800-555-1212-1234').groups()
#Traceback (most recent call last):
#  File "<pyshell#166>", line 1, in <module>
#    phonePattern.search('800-555-1212-1234').groups()
#AttributeError: 'NoneType' object has no attribute 'groups'
```

The sequence

```python
prog = re.compile(pattern)
result = prog.match(string)
```

is equivalent to

```python
result = re.match(pattern, string)
```

but using `re.compile()` and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.

1.	`\d` means "any numeric digit" (0 through 9)
2.	`{3}` means "match exactly three numeric digits"
3.	Putting it all in parentheses means "match exactly three numeric digits, and *then remember them as a group that I can ask for later*".
4.	To get access to the groups that the regular expression parser remembered along the way, use the `groups()` method on the object that the `search()` method returns. It will return a tuple of however many groups were defined in the regular expression. In this case, you defined three groups, one with three digits, one with three digits, and one with four digits.
5.	If the `search()` method returns no matches, it returns `None`, not a regular expression match object. Calling `None.groups()` raises a perfectly obvious exception: `None` doesn’t have a `groups()` method. This is why you should *never "chain" the `search()` and `groups()` methods in production code.*

```python
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')  
phonePattern.search('800-555-1212-1234').groups()              
#('800', '555', '1212', '1234')
phonePattern.search('800 555 1212 1234')                       
phonePattern.search('800-555-1212')
```

```python
phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
phonePattern.search('800 555 1212 1234').groups()
#('800', '555', '1212', '1234')
phonePattern.search('800-555-1212-1234').groups()
#('800', '555', '1212', '1234')
phonePattern.search('80055512121234')
phonePattern.search('800-55-1212')
```

1.	`\D` matches any character except a numeric digit, and `+` means “1 or more”. So `\D+` matches one or more characters that are not digits. This is what you’re using instead of a literal hyphen, to try to match different separators.
2.	Unfortunately, this is still not the final answer, because it assumes that there is a separator at all. What if the phone number is entered without any spaces or hyphens at all?

```python
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
phonePattern.search('80055512121234').groups()
#('800', '555', '1212', '1234')
phonePattern.search('800.555.1212 x1234').groups()
#('800', '555', '1212', '1234')
phonePattern.search('800-555-1212').groups()
#('800', '555', '1212', '')
phonePattern.search('(800)5551212 x1234')
```

`*` means "zero or more". So now you should be able to parse phone numbers even when there is no separator character at all.

```python
phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
phonePattern.search('(800)5551212 ext. 1234').groups()
#('800', '555', '1212', '1234')
phonePattern.search('800-555-1212').groups()
#('800', '555', '1212', '')
phonePattern.search('work 1-(800) 555.1212 #1234')
```

Rather than trying to match it all just so you can skip over it, let’s take a different approach: don’t explicitly match the beginning of the string at all. This approach is shown in the next example.

```python
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
phonePattern.search('work 1-(800) 555.1212 #1234').groups()
#('800', '555', '1212', '1234')
phonePattern.search('800-555-1212').groups()
#('800', '555', '1212', '')
phonePattern.search('80055512121234').groups()
#('800', '555', '1212', '1234')
```

Note the lack of ^ in this regular expression. You are not matching the beginning of the string anymore. There’s nothing that says you need to match the entire input with your regular expression. The regular expression engine will do the hard work of figuring out where the input string starts to match, and go from there.

Verbose regular expression version:

```python
phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
phonePattern.search('work 1-(800) 555.1212 #1234').groups()
#('800', '555', '1212', '1234')
phonePattern.search('800-555-1212')
#('800', '555', '1212', '')
```

Summary
-------

-	`^` matches the beginning of a string.
-	`$` matches the end of a string.
-	`\b` matches a word boundary.
-	`\d` matches any numeric digit.
-	`\D` matches any non-numeric character.
-	`x?` matches an optional `x` character (in other words, it matches an x zero or one times).
-	`x*` matches `x` zero or more times.
-	`x+` matches `x` one or more times.
-	`x{n,m}` matches an x character at least `n` times, but not more than `m` times.
-	`(a|b|c)` matches exactly one of `a`, `b` or `c`.
-	`(x)` in general is a remembered group. You can get the value of what matched by using the `groups()` method of the object returned by `re.search`.
-	`a`, `X`, `9`, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: . `^ $ * + ? { [ ] \ | ( )` (details below)
-	`.` (a period) -- matches any single character except newline `\n`
-	`\w` -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. `\W` (upper case W) matches any non-word character.
-	`\b` -- boundary between word and non-word
-	`\s` -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ `\n\r\t\f`]. `\S` (upper case S) matches any non-whitespace character.
-	\t, \n, \r -- tab, newline, return
-	`\` -- inhibit the "specialness" of a character. So, for example, use . to match a period or `\\` to match a slash. If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, `\@`, to make sure it is treated just as a character.
