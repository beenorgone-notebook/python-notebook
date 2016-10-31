# https://www.hackerrank.com/challenges/defaultdict-tutorial

'''The defaultdict tool is a container in the collections class of
Python. It's similar to the usual dictionary (dict) container, but
it has one difference: The value fields' data type is specified
upon initialization. For example:

    from collections import defaultdict
    d = defaultdict(list)
    d['python'].append("awesome")
    d['something-else'].append("not relevant")
    d['python'].append("language")
    for i in d.items():
        print i

This prints:

    ('python', ['awesome', 'language'])
    ('something-else', ['not relevant'])'''

from collections import defaultdict

n, m = map(int, input().strip().split(' '))
d = defaultdict(list)
for _ in range(n):
    d['A'].append(input())
for _ in range(m):
    i = input().strip()
    indices = tuple(j + 1 for j in range(n) if d['A'][j] == i)
    if indices:
        print(' '.join(map(str, indices)))
    else:
        print(-1)
