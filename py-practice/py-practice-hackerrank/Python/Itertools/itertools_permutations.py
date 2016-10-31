# https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations as perms

A_STRING, PERM_SIZE = input().strip().split(' ')

for i in perms(sorted(A_STRING), int(PERM_SIZE)):
    print(''.join(i))
