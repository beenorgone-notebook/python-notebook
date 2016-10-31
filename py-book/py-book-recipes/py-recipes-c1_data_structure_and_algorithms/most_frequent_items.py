# You have a sequence of items, and you’d like to determine
# the most frequently occurring items in the sequence.
# SOLUTION: collections.Counter and its most_common() method

import collections

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = collections.Counter(words)
print(word_counts)
'''
Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, "don't": 1, 'under': 1, 'not': 1, "you're": 1})
'''

top_three = word_counts.most_common(3)
print(top_three)
'''
[('eyes', 8), ('the', 5), ('look', 4)]
'''
