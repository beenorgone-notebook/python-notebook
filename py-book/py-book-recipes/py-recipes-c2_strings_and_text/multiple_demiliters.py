# You need to split a string into fields, but the delimiters
# (and spacing around them) aren’t consistent throughout the string.
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
fields = re.split(r'[;,\s]\s*', line)
print(fields)
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


# To capture delimiters, use group parentheses (...)
fields = re.split(r'([;,\s])\s*', line)
print(fields)
#['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']


values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
#[' ', ';', ',', ',', ',', '']


# Reform the line using the same delimiters
print(''.join(v + d for v, d in zip(values, delimiters)))
#'asdf fjdk;afed,fjek,asdf,foo'

# If you don’t want the separator characters in the result,
# but still need to use parentheses to group parts of the regular
# expression pattern, use a noncapture group, specified as (?:...)
fields = re.split(r'(?:[;,\s])\s*', line)
print(fields)
