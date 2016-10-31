# https://www.hackerrank.com/contests/w21/challenges/luck-balance

def get_input():
    a, b = input().strip().split(' ')
    return int(a), int(b)

n, k = get_input()
important, not_important = [], []
for i in range(n):
    l, t = get_input()
    if t == 1:
        important.append(l)
    else:
        not_important.append(l)
important = sorted(important, reverse=True)
can_lose, must_win = important[k:], important[:k]


print(sum(must_win) + sum(not_important) - sum(can_lose))
