[Dive into Python 3: Strings](http://www.diveintopython3.net/strings.html)
==========================================================================

Unicode
-------

Unicode is a system designed to represent *every* character from *every* language. Unicode represents each letter, character, or ideograph as a 4-byte number. Each number represents a unique character used in at least one of the world’s languages. (Not all the numbers are used, but more than 65535 of them are, so 2 bytes wouldn’t be sufficient.) Characters that are used in multiple languages generally have the same number, unless there is a good etymological reason not to. Regardless, there is exactly 1 number per character, and exactly 1 character per number. Every number always means just one thing; there are no “modes” to keep track of. `U+0041` is always 'A', even if your language doesn’t have an 'A' in it.

There is a Unicode encoding that uses four bytes per character. It’s called `UTF-32`, because 32 bits = 4 bytes. `UTF-32` is a straightforward encoding; it takes each Unicode character (a 4-byte number) and represents the character with that same number. This has some advantages, the most important being that you can find the `Nth` character of a string in constant time, because the `Nth` character starts at the `4×Nth` byte. It also has several disadvantages, the most obvious being that it takes four freaking bytes to store every freaking character.

Even though there are a lot of Unicode characters, it turns out that most people will never use anything beyond the first 65535. Thus, there is another Unicode encoding, called `UTF-16` (because 16 bits = 2 bytes). `UTF-16` encodes every character from 0–65535 as two bytes, then uses some dirty hacks if you actually need to represent the rarely-used “astral plane” Unicode characters beyond 65535. Most obvious advantage: `UTF-16` is twice as space-efficient as `UTF-32`, because every character requires only two bytes to store instead of four bytes (except for the ones that don’t). And you can still easily find the Nth character of a string in constant time, if you assume that the string doesn’t include any astral plane characters, which is a good assumption right up until the moment that it’s not.

But there are also non-obvious disadvantages to both `UTF-32` and `UTF-16`. Different computer systems store individual bytes in different ways. That means that the character `U+4E2D` could be stored in `UTF-16` as either `4E 2D` or `2D 4E`, depending on whether the system is big-endian or little-endian. (For `UTF-32`, there are even more possible byte orderings.) As long as your documents never leave your computer, you’re safe — different applications on the same computer will all use the same byte order. But the minute you want to transfer documents between systems, perhaps on a world wide web of some sort, you’re going to need a way to indicate which order your bytes are stored. Otherwise, the receiving system has no way of knowing whether the two-byte sequence `4E 2D` means `U+4E2D` or `U+2D4E`.

UTF-8 is a *variable-length* encoding system for Unicode. That is, different characters take up a different number of bytes. For `ascii` characters (A-Z, &c.) `utf-8` uses just one byte per character. In fact, it uses the exact same bytes; the first 128 characters (0–127) in utf-8 are indistinguishable from ascii. “Extended Latin” characters like ñ and ö end up taking two bytes. (The bytes are not simply the Unicode code point like they would be in `UTF-16`; there is some serious bit-twiddling involved.) Chinese characters like 中 end up taking three bytes. The rarely-used “astral plane” characters take four bytes.

Advantages: super-efficient encoding of common `ascii` characters. No worse than `UTF-16` for extended Latin characters. Better than `UTF-32` for Chinese characters. Also (and you’ll have to trust me on this, because I’m not going to show you the math), due to the exact nature of the bit twiddling, there are no byte-ordering issues. A document encoded in `utf-8` uses the exact same stream of bytes on any computer.

Diving In
---------

In Python 3, all strings are sequences of Unicode characters.

```python
s = '深入 Python'
len(s)
#9
s[0]
#'深'
s + ' 3'
#'深入 Python 3'
```

Formatting Strings
------------------

```python
username = 'mark'
password = 'PapayaWhip'                             
"{0}'s password is {1}".format(username, password)  
#"mark's password is PapayaWhip"
```

Compound Field Names
--------------------

```python
import humansize
si_suffixes = humansize.SUFFIXES[1000]      
si_suffixes
#['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
'1000{0[0]} = 1{0[1]}'.format(si_suffixes)  
#'1000KB = 1MB'
```

*Format specifiers can access items and properties of data structures using (almost) Python syntax*. This is called compound field names.

```python
import humansize # from examples folder
import sys
'1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys)
#'1MB = 1000KB'
```

1.	The `sys` module holds information about the currently running Python instance. Since you just imported it, you can pass the `sys` module itself as an argument to the `format()` method. So the replacement field `{0}` refers to the `sys` module.
2.	`sys.modules` is a dictionary of all the modules that have been imported in this Python instance. The keys are the module names as strings; the values are the module objects themselves. So the replacement field `{0.modules}` refers to the dictionary of imported modules.
3.	`sys.modules['humansize']` is the `humansize` module which you just imported. The replacement field `{0.modules[humansize]}` refers to the `humansize` module.

Format Specifiers
-----------------

Format specifiers refines how the replaced variable should be formatted.

> Format specifiers allow you to munge the replacement text in a variety of useful ways, like the `printf()` function in C. You can add zero- or space-padding, align strings, control decimal precision, and even convert numbers to hexadecimal.

```python
format_spec ::=  '[[fill]align][sign][#][0][width][,][.precision][type]'
fill        ::=  <any character>  
align       ::=  "<" | ">" | "=" | "^"  
sign        ::=  "+" | "-" | " "  
width       ::=  integer  
precision   ::=  integer  
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

Other Common String Methods
---------------------------

```python
s = '''Finished files are the re-  
... sult of years of scientif-
... ic study combined with the
... experience of years.'''
s
#'Finished files are the re-  \n... sult of years of scientif-\n... ic study combined with the\n... experience of years.'
s.splitlines()
#['Finished files are the re-  ', '... sult of years of scientif-', '... ic study combined with the', '... experience of years.']
print(s.lower())
#finished files are the re-  
#... sult of years of scientif-
#... ic study combined with the
#... experience of years.
s.lower().count('f')
#6

query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')
a_list
#['user=pilgrim', 'database=master', 'password=PapayaWhip']
a_list_of_lists = [v.split('=',1) for v in a_list if '=' in v] # `1` means "only split once".
a_list_of_lists
#[['user', 'pilgrim'], ['database', 'master'], ['password', 'PapayaWhip']]
a_dict = dict(a_list_of_lists)
a_dict
#{'user': 'pilgrim', 'password': 'PapayaWhip', 'database': 'master'}
```

1.	The `split()` string method has one required argument, a delimiter. The method splits a string into a list of strings based on the delimiter.
2.	Python can turn a list-of-lists into a dictionary simply by passing it to the `dict()` function.

> The previous example looks a lot like parsing query parameters in a `url`, but real-life `url` parsing is actually more complicated than this. If you’re dealing with `url` query parameters, you’re better off using the `urllib.parse.parse_qs()` function, which handles some non-obvious edge cases.

### Slicing A string

```python
a_string = 'My alphabet starts where your alphabet ends.'
a_string[3:11]           
#'alphabet'
a_string[3:-3]           
#'alphabet starts where your alphabet en'
a_string[0:2]            
#'My'
a_string[:18]            
3'My alphabet starts'
a_string[18:]            
#' where your alphabet ends.'
```

Strings vs. Bytes
-----------------

Bytes are bytes; characters are an abstraction. An immutable sequence of Unicode characters is called a *string*. An immutable sequence of numbers-between-0-and-255 is called a *bytes* object.

```python
by = b'abcd\x65'
by
#b'abcde'
type(by)
#<class 'bytes'>
len(by)
#5
by += b'\xfu'
#SyntaxError: (value error) invalid \x escape at position 0
by += b'\xff'
by
#b'abcde\xff'
len(by)
#6
by[0]
#97
by[-1]
#255
by[0] = 102
#Traceback (most recent call last):
# File "<pyshell#43>", line 1, in <module>
#   by[0] = 102
#TypeError: 'bytes' object does not support item assignment
```

1.	To define a bytes object, use the `b''` “byte literal” syntax. Each byte within the byte literal can be an `ascii` character or an encoded hexadecimal number from `\x00` to `\xff` (0–255).
2.	A `bytes` object is immutable; you can not assign individual bytes. If you need to change individual bytes, you can either use string slicing and concatenation operators (which work the same as strings), or you can convert the bytes object into a bytearray object.

```python
by = b'abcd\x65'
barr = bytearray(by)
barr
#bytearray(b'abcde')
len(barr)
#5
barr[0] = 102
barr
#bytearray(b'fbcde')
```

1.	To convert a `bytes` object into a mutable `bytearray` object, use the built-in `bytearray()` function.
2.	All the methods and operations you can do on a bytes object, you can do on a `bytearray` object too.
3.	The one difference is that, with the `bytearray` object, you can assign individual bytes using index notation. The assigned value must be an integer between 0–255.

The one thing you can *never* do is mix bytes and strings.

```python
by =b'd'
s = 'abcde'
barr = bytearray(by)
by + s
#Traceback (most recent call last):
#  File "<pyshell#56>", line 1, in <module>
#    by + s
#TypeError: can't concat bytes to str
s.count(by)
#Traceback (most recent call last):
#  File "<pyshell#76>", line 1, in <module>
#    s.count(by)
#TypeError: Can't convert 'bytes' object to str implicitly
s.count(by.decode('ascii'))
#1
s.count(by.decode('utf-8'))
#1
```

1.	You can’t concatenate bytes and strings. They are two different data types.
2.	You can’t count the occurrences of bytes in a string, because there are no bytes in a string. A string is a sequence of characters. Perhaps you meant “count the occurrences of the string that you would get after decoding this sequence of bytes in a particular character encoding”? Well then, you’ll need to say that explicitly. Python 3 won’t implicitly convert bytes to strings or strings to bytes.

bytes objects have a `decode()` method that takes a character encoding and returns a string, and strings have an `encode()` method that takes a character encoding and returns a bytes object.

```python
a_string = '深入 Python'
len(a_string)
#9
by = a_string.encode('utf-8')
by
#b'\xe6\xb7\xb1\xe5\x85\xa5 Python'
len(by)
#13
by = a_string.encode('gb18030')
by
#b'\xc9\xee\xc8\xeb Python'
len(by)
#11
by = a_string.encode('big5')
by
#b'\xb2`\xa4J Python'
len(by)
#11
roundtrip = by.decode('big5')
roundtrip
#'深入 Python'
a_string == roundtrip
#True
```

Character Encoding Of Python Source Code
----------------------------------------

In Python 2, the default encoding for `.py` files was `ascii`. In Python 3, the default encoding is `utf-8`.

If you would like to use a different encoding within your Python code, you can put an encoding declaration on the first line of each file.

```python
# -*- coding: windows-1252 -*-
```

Further Reading
---------------

On Unicode in Python:

-	[Python Unicode HOWTO](http://docs.python.org/3/howto/unicode.html)
-	[What’s New In Python 3: Text vs. Data Instead Of Unicode vs. 8-bit](http://docs.python.org/3.0/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit)
-	[`pep` 261](http://www.python.org/dev/peps/pep-0261/) explains how Python handles astral characters outside of the Basic Multilingual Plane (i.e. characters whose ordinal value is greater than 65535)

On Unicode in general:

-	[The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](http://www.joelonsoftware.com/articles/Unicode.html)
-	[On the Goodness of Unicode](http://www.tbray.org/ongoing/When/200x/2003/04/06/Unicode)
-	[On Character Strings](http://www.tbray.org/ongoing/When/200x/2003/04/13/Strings)
-	[Characters vs. Bytes](http://www.tbray.org/ongoing/When/200x/2003/04/26/UTF)

On character encoding in other formats:

-	[Character encoding in XML](http://feedparser.org/docs/character-encoding.html)
-	[Character encoding in HTML](http://blog.whatwg.org/the-road-to-html-5-character-encoding)

On strings and string formatting:

-	[`string` — Common string operations](http://docs.python.org/3/library/string.html)
-	[Format String Syntax](http://docs.python.org/3/library/string.html#formatstrings)
-	[Format Specification Mini-Language](http://docs.python.org/3/library/string.html#format-specification-mini-language)
-	[`pep` 3101: Advanced String Formatting](http://www.python.org/dev/peps/pep-3101)
