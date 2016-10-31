import re

t = int(input())

def get_numbers(input_data):
    return map(int, re.findall(r'\d+', input_data))


while t:
    n_k = get_numbers(input())
    n = int(n_k[0])
    k = int(n_k[1])
    a = sorted(get_numbers(input()))
    b = sorted(get_numbers(input()))

    if a[0] + b[0] >= k:
        print('YES')
    elif a[-1] + b[-1] <= k:
        print('NO')
    else:
        for i in a:
            for j in b:
                if i+j < k:
                    continue
                else:
                    b.remove(j)
                    break
            if len(b) == n:
                print('NO')
                break
            else:
                n = n - 1
        if not n:
            print('YES')
