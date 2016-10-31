# https://www.hackerrank.com/challenges/itertools-combinations

from itertools import combinations

A_STRING, COMBI_SIZE = input().strip().split(' ')

for i in range(1, int(COMBI_SIZE) + 1):
    for j in combinations(sorted(A_STRING), i):
        print(''.join(j))

# https://www.hackerrank.com/challenges/maximize-it

K, M = map(int, input().strip().split(' '))
LISTS_OF_INTS = [list(map(int, input().split(' ')))[1:] for _ in range(K)]
S = []

for p in product(*LISTS_OF_INTS):
    S.append(sum(map(lambda i: i**2, p)) % M)
