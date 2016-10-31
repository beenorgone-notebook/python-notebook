def print_staircase(n)
    for i in range(1, n+1):
        print('{:>{}}'.format('#'*i, n))

print_staircase(int(input().strip()))
