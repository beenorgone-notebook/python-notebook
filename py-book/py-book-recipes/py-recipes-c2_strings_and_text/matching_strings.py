# PROBLEM: ENDS OR STARTS WITH
# You need to check the start or end of a string for specific text
# patterns, such as filename extensions, URL schemes, and so on.
# SOLUTION: str.startswith() and str.endswith()

# PROBLEM: MATCHING STRINGS USING SHELL WILDCARD PATTERNS
# You want to match text using the same wildcard patterns as
# are commonly used when working in Unix shells
# (e.g., *.py , Dat[0-9]*.csv , etc.).
# SOLUTION: fnmatch.fnmatch() and fnmatch.fnmatchcase()

import functools
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

'''Discussion
`fnmatch` sits somewhere between the functionality of simple
string methods and the full power of regular expressions.
If you’re just trying to provide a simple mechanism for
allowing wildcards in data processing operations,
it’s often a reasonable solution.

If you’re actually trying to write code that matches filenames,
use the `glob` module instead.
'''

# PROBLEM: MATCHING OR SEARCHING TEXT FOR A SPECIFIC PATTERN
# SOLUTION:
# For a simple literal: str.find(), str.endswith(), str.startswith()
# For more complicated matching, use regex (the `re` module)


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

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

# match() always tries to find the match at the start of a string.
# If you want to search text for all occurrences of a pattern,
# use the findall() method instead.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
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

# If you want to find matches iteratively, use the finditer() method instead.
for m in datepat.finditer(text):
    print(m.groups())
# ('11', '27', '2012')
# ('3', '13', '2013')

'''Discussion
The essential functionality is first compiling a pattern using
re.compile() and then using methods such as match(), findall(), or finditer().

When specifying patterns, it is relatively common to use raw strings
such as r'(\d+)/(\d+)/(\d+)' . Such strings leave the backslash
character uninterpreted, which can be useful in the context of
regular expressions. Otherwise, you need to use double backslashes
such as '(\\d+)/(\\d+)/(\\d+)' .

the match() method only checks the beginning of a string.
It’s possible that it will match things you aren’t expecting.
'''

# PROBLEM: Get Shortest Match
# SOLUTION: Add the `?` modifier after the `*` operator in the pattern.
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

# PROBLEM: Matching Multiple Lines
# SOLUTION: Use `|\n` or `re.DOTALL` flag
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
