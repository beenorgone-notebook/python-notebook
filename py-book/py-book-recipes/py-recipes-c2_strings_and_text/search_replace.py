# PROBLEM: Search for and replace a text pattern in a string
# SOLUTION:
# For simple literal patterns, use the str.replace() method.
# For more complicated patterns,
# use the re.sub() function/method

import re
from calendar import month_abbr

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'
# Backslashed digits such as \3 refer to capture group numbers in the pattern.

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'


# For more complicated substitutions,
# it’s possible to specify a substitution callback function instead.
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))
# Today is 27 Nov 2012. PyCon starts 13 Mar 2013.

# If you want to know how many substitutions were made
# in addition to getting the replacement text, use re.subn() instead
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
# Today is 2012-11-27. PyCon starts 2013-3-13.
print(n)
# 2

# PROBLEM: search for and possibly replace text in
# a case-insensitive manner.
# SOLUTION: use `re.IGNORECASE` flag
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
#['PYTHON', 'python', 'Python']
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
#'UPPER snake, lower snake, Mixed snake'


# PROBLEM: Matching the case of replacing text with matched text's case
# SOLUTION: use a function which will built replacing rules
# based on matched text's case
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
