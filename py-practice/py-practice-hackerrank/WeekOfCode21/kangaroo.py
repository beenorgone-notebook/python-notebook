# https://www.hackerrank.com/contests/w21/challenges/kangaroo

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

a = (x2-x1)/(v1-v2)
if a => 0 and a == int(a):
    print('YES')
else:
    print('NO')
