# https://www.hackerrank.com/challenges/collections-counter

from collections import Counter

X = int(input().strip())
SHOE_SIZES = Counter(map(int, input().strip().split(' ')))
N = int(input().strip())
REVENUE = 0

for _ in range(N):
    size, x = map(int, input().strip().split(' '))
    if size in SHOE_SIZES and SHOE_SIZES[size] > 0:
        REVENUE += x
        SHOE_SIZES[size] -= 1

print(REVENUE)
