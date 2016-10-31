'''
https://www.hackerrank.com/challenges/bigger-is-greater

https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

1. Find largest index i such that array[i − 1] < array[i].
2. Find largest index j such that j ≥ i and array[j] > array[i − 1].
3. Swap array[j] and array[i − 1].
4. Reverse the suffix starting at array[i].
'''

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
        cases = get_input(input_files[i])
        output = get_output(output_files[i])
        print('-------- \nTestcase {} \nResult:'.format(os.path.split(input_files[i])[1]))
        for case in cases:
            result = func(case)
            print(result, end='\n')
        print('Expected Output: \n{}'.format(output))

def get_input(input_case):
    with open(input_case) as f:
        t = f.readline().strip()
        t = int(t)
        cases = []
        for i in range(t):
            arr = f.readline().strip()
            cases += [arr]
    return cases

def get_output(output_case):
    with open(output_case) as f:
        return f.read().strip()

@timeout(10.0)  # if execution takes longer than 10 seconds, raise a TimeoutError
def next_bigger_perm(a_string):
    arr = list(a_string)
    #Find longest non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1 : i-1 : -1]
    return ''.join(arr)

'''
t = int(input().strip())
for i in range(t):
    arr = list(input().strip())
    next_perm = next_bigger_perm(arr)
    if next_perm:
        print(next_perm)
    else:
        print('no answer')
'''

if __name__ == "__main__":
    input_path = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-hackerrank/Algorithms/Sorting/testcases/bigger-is-greater-testcases/input'
    output_path = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-hackerrank/Algorithms/Sorting/testcases/bigger-is-greater-testcases/output'
    input_pattern = '*.txt'
    output_pattern = '*.txt'
    test(next_bigger_perm, input_path, output_path, input_pattern, output_pattern)
