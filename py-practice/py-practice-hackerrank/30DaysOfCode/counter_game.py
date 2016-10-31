def is_power2(num):
    num = int(num)
    return num > 0 and (num & (num - 1)) == 0

def getClosestSmaller(n, k=2):
    num = 1
    while num < n:
        num = num * k
    num = num / k
    return num

def CounterGameSolution(n):
    turn = 0
    while n > 1:
        turn += 1
        if is_power2(n):
            n = n / 2
        else:
            n -= getClosestSmaller(n)
    if turn & 1 == 0:
        print("Richard")
    else:
        print("Louise")


'''
t = int(input().strip())
for i in range(0,t):
    CounterGameSolution(int(input().strip()))
'''
