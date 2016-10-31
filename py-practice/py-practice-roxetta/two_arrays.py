'''
You are given two integer arrays, A and B, each containing N integers. The size of the array is less than or equal to 1000. You are free to permute the order of the elements in the arrays.

QUESTION: Is there an permutation A', B' possible of A and B, such that, A'i+B'i ≥ K for all i, where A'i denotes the ith element in the array A' and B'i denotes ith element in the array B'.

Input Format
The first line contains an integer, T, the number of test-cases. T test cases follow. Each test case has the following format:
The first line contains two integers, N and K. The second line contains N space separated integers, denoting array A. The third line describes array B in a same format.

Output Format
For each test case, if such an arrangement exists, output "YES", otherwise "NO" (without quotes).

Constraints
1 <= T <= 10
1 <= N <= 1000
1 <= K <= 109
0 <= Ai, Bi ≤ 109

SAMPLE INPUT
2
3 10
2 1 3
7 8 9
4 5
1 2 2 1
3 3 3 4

SAMPLE OUTPUT:
YES
NO

The first input has 3 elements in Array A and Array B, we see that the one of the arrangements, 3 2 1 and 7 8 9 has each pair of elements (3+7, 2 + 8 and 9 + 1) summing upto 10 and hence the answer is "YES".
The second input has array B with three 3s. So, we need at least three numbers in A that are greater than 1. As this is not the case, the answer is "NO".
'''
import itertools
import re
import redirect_stdin
import redirect_stdout
import os
import sys

print(os.getcwd())

def two_arrays(file_path):
    with redirect_stdin.RedirectStdinTo(open(file_path, encoding='utf-8', mode='r')):

    pass

two_arrays('/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-roxetta_code/two_arrays_input1.txt')
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
