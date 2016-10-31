# https://www.hackerrank.com/contests/june-world-codesprint/challenges/minimum-distances

import itertools

def difference(a_pair):
    x, y = a_pair
    return abs(x-y)

def list_duplicates(source, item):
    return [index_x for index_x, x in enumerate(source) if x == item]

def min_dist(A):
    min_dist_list = []
    seen = set(A)
    for num in seen:
        indices_of_num = sorted(list_duplicates(A, num) ,reverse=True)
        if len(indices_of_num) <= 1:
            continue
        elif len(indices_of_num) == 2:
            i, j = indices_of_num
            min_dist_list.append(abs(i-j))
        else:
            dist_list = map(difference, list(itertools.combinations(indices_of_num, 2)))
            min_dist_list.append(min(dist_list))
    if min_dist_list:
        return min(min_dist_list)
    else:
        return -1
