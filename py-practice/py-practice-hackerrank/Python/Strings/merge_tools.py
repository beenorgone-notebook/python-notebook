'''
https://hackerrank.com/challenges/merge-the-tools
Given a string S of length N. Divide this string into N/K equal parts
thus each part contain exactly K elements.

Let us consider the string thus obtained in part i as Ti.
For each string Ti thus obtained you have to make a modified string
such that each character that occurs in Ti occurs exactly once in the
modified string.
'''

import textwrap
from collections import OrderedDict

S = input().strip()
N = len(S)
K = int(input())
S_parted = textwrap.wrap(S, K)

'''
def str_duplicates_remove(a_string):
    return ''.join(sorted(set(a_string), key=a_string.index))

S_modified = map(str_duplicates_remove, S_parted)
'''

S_modified = map(lambda s: ''.join(sorted(set(s), key=s.index)),
                 S_parted)
for i in S_modified:
    print(i)


# We can use OrderedDict instead:
S_modified = map(lambda s: ''.join(OrderedDict.fromkeys(s)),
                 S_parted)

# Declarative version
s = input().strip()
k = int(input())
i = 0
while i < len(s):
    a = s[i:i + k]
    output = ''
    for x in a:
        if x not in output:
            output += x
    print(output)
    i += k
