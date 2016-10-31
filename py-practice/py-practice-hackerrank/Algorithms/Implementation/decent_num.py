# https://www.hackerrank.com/challenges/sherlock-and-the-beast
'''
a + b = N
a % 5 = 0
b % 3 = 0
return '5' * a + '3' * b
'''

def max_decent_number(N):
    if not (1 <= N <= 100000):
        raise ValueError('N should be between 1 and 100000')
    for i in range(0, N, 5):
        if not (N - i) % 3:
            max_decent_num = int('5' * (N-i) + '3' * i)
            return max_decent_num
    if N % 5:
        return -1
    else:
        return int('3' * N)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max_decent_number(n))
