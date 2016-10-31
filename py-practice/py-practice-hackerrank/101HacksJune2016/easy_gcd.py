#!/bin/python3

# Timeout Function

import multiprocessing.pool
import functools

def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator

# Test Functions

import os
import glob

def test(func, input_path, output_path, input_pattern, output_pattern):
    input_files = sorted(glob.glob(os.path.join(input_path, input_pattern)))
    output_files = sorted(glob.glob(os.path.join(output_path, output_pattern)))
    for i in range(len(input_files)):
        n, k, A = get_input(input_files[i])
        output = get_output(output_files[i])
        result = func(A, k)
        print('------------- \nTestcase {:<20} \nResult: {:<20} \nExpected output: {:<20}'.format(os.path.split(input_files[i])[1], result, output))

def get_input(input_case):
    with open(input_case) as f:
        n,k = f.readline().strip().split(' ')
        n,k = [int(n),int(k)]
        A = [int(A_temp) for A_temp in f.readline().strip().split(' ')]
    return n, k, A

def get_output(output_case):
    with open(output_case) as f:
        return int(f.readline().strip())

# Solve Challenge

def prime_factors(n):
    primfac = []
    d = 2
    while d ** 2 <= n:
        while n % d == 0:
            if d not in primfac:
                primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def common_prime_factors(a_list):
    if len(a_list) == 1:
        return prime_factors(a_list[0])
    min_num = min(a_list)
    common_prime_factors = prime_factors(min_num)
    for x in a_list:
        if x != min_num:
            common_prime_factors = [i for i in common_prime_factors if x % i == 0]
        if x == min_num:
            continue
    return common_prime_factors

@timeout(10.0)  # if execution takes longer than 10 seconds, raise a TimeoutError
def find_l(a_list, k):
    prime_factors = common_prime_factors(a_list)
    X = [(k % x) for x in prime_factors]
    l = k - min(X)
    return l
'''
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
A = [int(A_temp) for A_temp in input().strip().split(' ')]

print(find_l(A, k))
'''

if __name__ == "__main__":
    input_path = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-hackerrank/101HacksJune2016/testcases/easy-gcd-testcases/input'
    output_path = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-hackerrank/101HacksJune2016/testcases/easy-gcd-testcases/output'
    input_pattern = '*.txt'
    output_pattern = '*.txt'
    test(find_l, input_path, output_path, input_pattern, output_pattern)
