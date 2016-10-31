'''
Given a 2D array of digits, try to find the occurrence of a given 2D pattern of digits. For example, consider the following 2D matrix:

1234567890
0987654321
1111111111
1111111111
2222222222

we need to look for the following 2D pattern:

876543
111111
111111

If we scan through the original array, we observe that the 2D pattern begins at the second row and the third column of the larger grid (the 8 in the second row and third column of the larger grid is the top-left corner of the pattern we are searching for).

So, a 2D pattern of P digits is said to be present in a larger grid G, if the latter contains a contiguous, rectangular 2D grid of digits matching with the pattern P, similar to the example shown above.
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
        print('------------- \ntestcase {} \nResult'.format(os.path.split(input_files[i])[1]))
        cases = get_input(input_files[i])
        output = get_output(output_files[i])
        result = []
        for case in cases:
            print(func(case[0], case[1]))
        print('Expected output \n{}'.format(output))
        #print('testcase {:<20} result: {:<20} expected output: {:<20}'.format(os.path.split(input_files[i])[1], result, output))

def get_input(input_case):
    def get_matrix():
        matrix = []
        R, C = f.readline().strip().split(' ')
        R, C = [int(R), int(C)]
        while R:
            temp = f.readline().strip()
            matrix.append(temp)
            R -= 1
        return matrix

    with open(input_case) as f:
        T = f.readline().strip()
        T = int(T)
        cases = []
        for i in range(T):
            larger = get_matrix()
            smaller = get_matrix()
            cases.append([larger, smaller])
    return cases

def get_output(output_case):
    with open(output_case) as f:
        return f.read().strip()

@timeout(10.0)  # if execution takes longer than 10 seconds, raise a TimeoutError
def grid_search(matrix, pattern):
    pat0 = pattern[0]
    for i in range(len(matrix)):
        if pat0 in matrix[i]:
            sub_pos = get_subset_pos(matrix[i], pat0)
            for pos in sub_pos:
                first, last = pos
                found = True
                for j in range(1, len(pattern)):
                    if matrix[(i+j)][first:last] != pattern[j]:
                        found = False
                        break
                if found:
                    return 'YES'
                else:
                    continue
        else:
            continue
    return 'NO'

def get_subset_pos(a_list, pattern):
    if pattern not in a_list:
        raise ValueError('Your input is not subset of the remain.')
    ln = len(pattern)
    sub_pos = []
    for i in range(len(a_list)):
        if (a_list[i] == pattern[0]) and a_list[i:(i+ln)]:
            sub_pos.append([i, i+ln])
    return sub_pos

if __name__ == "__main__":
    input_path = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-hackerrank/Algorithms/Implementation/testcases/the-grid-search-testcases/input/'
    output_path = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-hackerrank/Algorithms/Implementation/testcases/the-grid-search-testcases/output/'
    input_pattern = '*.txt'
    output_pattern = '*.txt'

    test(grid_search, input_path, output_path, input_pattern, output_pattern)
