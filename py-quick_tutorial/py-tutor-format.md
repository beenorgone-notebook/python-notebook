# [Python Formatting](https://pyformat.info)

<!-- toc orderedList:0 -->

- [Python Formatting](#python-formattinghttpspyformatinfo)
	- [Basic formatting](#basic-formattinghttpspyformatinfosimple)
	- [Value conversion](#value-conversionhttpspyformatinfoconversion_flags)
	- [Padding and aligning strings](#padding-and-aligning-stringshttpspyformatinfostring_pad_align)
	- [Truncating long strings](#truncating-long-stringshttpspyformatinfostring_truncating)
	- [Combining truncating and padding](#combining-truncating-and-paddinghttpspyformatinfostring_trunc_pad)
	- [Numbers](#numbershttpspyformatinfonumber)
	- [Padding numbers](#padding-numbershttpspyformatinfonumber_padding)
	- [Signed numbers](#signed-numbershttpspyformatinfonumber_sign)
	- [Named placeholders](#named-placeholdershttpspyformatinfonamed_placeholders)
	- [Datetime](#datetimehttpspyformatinfodatetime)

<!-- tocstop -->

 ## [Basic formatting](https://pyformat.info/#simple)

```python
print ('{} {}'.format('one', 'two'))
print ('{} {}'.format(1, 2))
# one two
# 1 2
print ('{1} {0}'.format('one', 'two'))
# two one
```

**Read more:** [Python string format](https://mkaz.tech/python-string-format.html) via mkaz

## [Value conversion](https://pyformat.info/#conversion_flags)

`!s` and `!r`, `!a`

```python
print ('{!s} {!r}'.format('Tuấn', 'Hà'))
# Tuấn 'Hà'
print ('{!s} {!a}'.format('Tuấn', 'Hà'))
# Tuấn 'H\xe0'
```

## [Padding and aligning strings](https://pyformat.info/#string_pad_align)

```python
print ('{:>10}'.format('test'))
#       test
print ('{:^10}'.format('test'))
#    test   
print ('{:<{}s}'.format('test', 8))
test    
print ('{:_<10}'.format('test'))
# test______
```

## [Truncating long strings](https://pyformat.info/#string_truncating)

```python
print ('{:.5}'.format('xylophone'))
# xylop
print ('{:.{}}'.format('xylophone', 7))
# xylopho
```

## [Combining truncating and padding](https://pyformat.info/#string_trunc_pad)

```python
print ('{:10.5}'.format('xylophone'))
# xylop
```

## [Numbers](https://pyformat.info/#number)

Integers: `:d` and Floats: `:f`

## [Padding numbers](https://pyformat.info/#number_padding)

```python
print ('{:4d}'.format(42))
#   42
print ('{:06.2f}'.format(3.141592653589793))
# 003.14
print ('{:04d}'.format(42))
# 0042
```

## [Signed numbers](https://pyformat.info/#number_sign)

```python
print ('{:+d}'.format(42))
# +42
print ('{: d}'.format((- 23)))
# -23
print ('{: d}'.format(42))
#  42
print ('{:=5d}'.format((- 23)))
# -  23
print ('{: 5d}'.format((- 23)))
#   -23
```

## [Named placeholders](https://pyformat.info/#named_placeholders)

```python
data = {'first': 'Hodor', 'last': 'Hodor!'}
print ('{first} {last}'.format(**data))
# or
print ('{first} {last}'.format(first='Hodor', last='Hodor!'))
```

[Getitem and Getattr](https://pyformat.info/#getitem_and_getattr)

```python
person = {'first': 'Jean-Luc', 'last': 'Picard'}
print ('{p[first]} {p[last]}'.format(p=person))
# Jean-Luc Picard
data = [4, 8, 15, 16, 23, 42]
print ('{d[4]} {d[5]}'.format(d=data))
# 23 43

class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]

print ('{p.type}'.format(p=Plant()))
# tree
print ('{p.type}: {p.kinds[0][name]}'.format(p=Plant()))
# tree: oak
```

## [Datetime](https://pyformat.info/#datetime)

**Setup**:

```python
from datetime import datetime
```

```python
print ('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))
# 2001-02-03 04:05
```
