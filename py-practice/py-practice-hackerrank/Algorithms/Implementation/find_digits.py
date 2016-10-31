# https://www.hackerrank.com/challenges/find-digits

def find_evenly_div_digits(N):
    count = 0
    string_N = str(N)
    for i in string_N:
        if not i:
            continue
        if not N % int(i):
            count += 1
    return count
