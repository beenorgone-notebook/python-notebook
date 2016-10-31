'''
Given n two-dimensional points in space, determine whether they lie on some vertical or horizontal line. If yes, print YES; otherwise, print NO.
'''

#!/bin/python3

import sys

points = []

n = int(input().strip())
for a0 in range(n):
    x, y = input().strip().split(' ')
    x, y = (int(x), int(y))
    points.append((x, y))

def line_or_not(points):
    vertical, horizontal = True, True
    for point in points:
        if point[0] != points[0][0]:
            vertical = False
        if point[1] != points[0][1]:
            horizontal = False
    if vertical or horizontal:
        return 'YES'
    else:
        return 'NO'

print(line_or_not(points))
