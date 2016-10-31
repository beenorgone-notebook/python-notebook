# https://www.hackerrank.com/challenges/compress-the-string

from itertools import groupby

A_STR = input().strip()

for key, quantity in groupby(A_STR):
    print((len(list(quantity)), int(key)), end=' ')
