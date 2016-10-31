# https://www.hackerrank.com/contests/june-world-codesprint/challenges/equal-stacks

def diminu_sum(nums):
    total = sum(nums)
    for x in nums[-1::-1]:
        total -= x
        yield total

'''
def all_same(items):
    return all(x == items[0] for x in items)

def all_same(items):
  try:
     iterator = iter(items)
     first = next(iterator)
     return all(first == rest for rest in iterator)
  except StopIteration:
     return True
'''

def all_same(items):
    return len(set(items)) == 1

def max_equal_stacks(stacks):
    dimisums = []
    n = stacks
    for st in stacks:
        st_sum_gen = diminu_sum(st)
        dimisums.append(st_sum_gen)
        comparing_heights.append(sum(st))
    equal_height_found = all_same(comparing_heights)
    while not equal_height_found:
        for i in range(n):
            if comparing_heights[i] == max(comparing_heights):
                    comparing_heights[i] = next(dimisums[i])
    return comparing_heights[0]
