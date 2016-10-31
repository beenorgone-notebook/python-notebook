# https://www.hackerrank.com/challenges/py-collections-ordereddict

'''collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Example

Code

>>> from collections import OrderedDict
>>>
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>>
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>>
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>>
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
'''

from collections import OrderedDict

N = int(input())
ITEMS = OrderedDict()
for _ in range(N):
    item, space, quantity = input().rpartition(' ')
    ITEMS[item] = ITEMS.get(item, 0) + int(quantity)
for item, quantity in ITEMS.items():
    print(item, quantity)

# https://www.hackerrank.com/challenges/word-order

n = int(input())
WORD_COUNTS = OrderedDict()
for _ in range(n):
    word = input().strip()
    WORD_COUNTS[word] = WORD_COUNTS.get(word, 0) + 1

print(len(WORD_COUNTS))
for count in WORD_COUNTS.values():
    print(count, end=' ')
