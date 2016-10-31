# https://www.hackerrank.com/challenges/list-comprehensions


def get_num():
    return int(input().strip())

x = get_num()
y = get_num()
z = get_num()
n = get_num()

output = [[a, b, c] for a in range(
    0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1)
    if a + b + c != n]
print(output)
