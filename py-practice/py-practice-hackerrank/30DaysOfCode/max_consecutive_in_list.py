# CHALLENGE: https://www.hackerrank.com/challenges/30-binary-numbers

# REFRENCES: http://stackoverflow.com/questions/36441522/find-maximum-length-of-consecutive-repeated-numbers-in-a-list-python

'''
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.
'''

import itertools

def max_consecutive(a_list, search_key):
    search_key_groups = [(x[0], len(list(x[1]))) for x in itertools.groupby(a_list) if int(x[0]) == search_key]
    print(int(max(search_key_groups, key=lambda x:x[1])[1]))

n = int(input().strip())

max_consecutive(list(bin(n)[2:]), 1)
