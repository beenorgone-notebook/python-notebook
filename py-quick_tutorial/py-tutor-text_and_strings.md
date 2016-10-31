# Solving Text and Strings Problems in Python

<!-- toc orderedList:0 -->

 - [Solving Text and Strings Problems in Python](#solving-text-and-strings-problems-in-python)

  - [Resources](#resources)
  - [Matching](#matching)
  - [Search and Replace](#search-and-replace)

<!-- tocstop -->

 ## Resources

Python Cookbook - Chap 2: Strings and Text by David Beazley

`py-tutor-regex` note

## Matching

### Ends or Starts With

To match text using wildcard patterns (`*`, `?`), use: `fnmatch.fnmatch()` and `fnmatch.fnmatchcase()`

```python
import re
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
# True
print(fnmatch('foo.txt', '?oo.txt'))
# True
print(fnmatch('Dat45.csv', 'Dat.[0-9]*'))
# False
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
#['Dat1.csv', 'Dat2.csv']
```

### Specific Patterns

For a simple literal: `str.find()`, `str.endswith()`, `str.startswith()`

For more complicated matching, use regex (the `re` module)

- first compiling a pattern using `re.compile()` and then
- using methods such as `re.match()`, `re.findall()`, or `re.finditer()`.

```python
# Simple matching: `\d+` means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
# yes

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
# yes


text = 'Today is 11/27/2012\. PyCon starts 3/13/2013.'
datepat.findall(text)
#['11/27/2012', '3/13/2013']

# When defining regular expressions, it is common to introduce
# capture groups by enclosing parts of the pattern in parentheses.
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)  # <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>
print(m.group(0))  # 11/27/2012
print(m.group(1))  # 11
print(m.group(2))  # 27
print(m.group(3))  # 2012
print(m.groups())  # ('11', '27', '2012')

# Find all matches (notice splitting into tuples)
print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]
```

### Shortest Match

To get the shortest match, add the `?` modifier after the `*` operator in the pattern.

```python
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
# ['no.']
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# ['no." Phone says "yes.']

str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
# ['no.', 'yes.']
```

### Multiple Lines

Use `|\n` or `re.DOTALL` flag

```python
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a

multiline comment */
    '''

print(comment.findall(text2))  # []

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
# (?:.|\n) specifies a noncapture group
# (i.e., it defines a group for the purposes of matching, but
# that group is not captured separately or numbered).
print(comment.findall(text2))
# [' this is a\n\nmultiline comment ']

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
# [' this is a\n\nmultiline comment ']
```

## Search and Replace

### Text Patterns

For simple literal patterns, use the `str.replace()` method.

For more complicated patterns, use the `re.sub()` function/method or `re.subn()` if you want to know how many substitutions were made.

```python
import re
from calendar import month_abbr

text = 'Today is 11/27/2012\. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# 'Today is 2012-11-27\. PyCon starts 2013-3-13.'

text = 'Today is 11/27/2012\. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# 'Today is 2012-11-27\. PyCon starts 2013-3-13.'
# Backslashed digits such as \3 refer to capture group numbers in the pattern.

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
# 'Today is 2012-11-27\. PyCon starts 2013-3-13.'
```

#### Callback function

For more complicated substitutions, it's possible to specify a substitution callback function instead.

```python
import re
from calendar import month_abbr

text = 'Today is 11/27/2012\. PyCon starts 3/13/2013.'

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))
# Today is 27 Nov 2012\. PyCon starts 13 Mar 2013.
```

### Case-Insensitive

Use `re.IGNORECASE` flag if you want to search for and replace text in a case-insensitive manner.

If you need replacing text match the case of matched text, use a function which will build replacing rules based on matched text's case.

```python
import re

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
# UPPER SNAKE, lower snake, Mixed Snake
```

## Working with Encoding

### Normalizing Unicode Text

#### Why Normalizing?

In Unicode, certain characters can be represented by more than one valid sequence of code points:

```python
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalape\u0303o'
print(s1, s2)
```

To make sure that all of the strings have the same underlying representation.
