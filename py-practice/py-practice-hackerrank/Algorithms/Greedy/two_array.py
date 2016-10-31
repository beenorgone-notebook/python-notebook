'''
You are given two integer arrays, A and B, each containing N integers. The size of the array is less than or equal to 1000. You are free to permute the order of the elements in the arrays.

QUESTION: Is there an permutation A', B' possible of A and B, such that, A'i+B'i ≥ K for all i, where A'i denotes the ith element in the array A' and B'i denotes ith element in the array B'.
'''

import re

t = int(input())

def get_numbers(a_string):
    return re.findall(r'\d+' ,a_string)

while t:
    n_k = get_numbers(input())
    n = int(n_k[0])
    k = int(n_k[1])
    a = sorted([int(n) for n in get_numbers(input())])
    b = sorted([int(n) for n in get_numbers(input())])
    
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
    
    
        
