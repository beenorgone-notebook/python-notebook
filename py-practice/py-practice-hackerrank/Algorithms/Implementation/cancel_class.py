# https://www.hackerrank.com/challenges/angry-professor

def calc_ontime_students(num_students, cancel_threshold, arrive_times):
    for i in arrive_times:
        if i > 0:
            ontime_students = arrive_times.index(i)
            break
    return ontime_students

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    a = sorted(a)
    if calc_ontime_students(n, k, a) >= k:
        print('NO')
    else:
        print('YES')
