# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement as comb_w_replace

A_STR, SIZE = input().strip().split(' ')

for i in comb_w_replace(sorted(A_STR), int(SIZE)):
    print(''.join(i))
