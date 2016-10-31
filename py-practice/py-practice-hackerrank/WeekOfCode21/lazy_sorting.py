# https://www.wikiwand.com/en/Arithmetico-geometric_sequence


def factorial(n):
    if n == 0:
        return 1
    if n:
        return n * factorial(n-1)

N = int(input().strip())
P = input().strip().split(' ')
P = [int(x) for x in P]

p = 1/factorial(N)
q = 1 - p
