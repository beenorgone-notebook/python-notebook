# https://www.hackerrank.com/challenges/utopian-tree

def tree_height(tree, N, start):
    if not N:
        return tree
    if start == 'spring':
        for i in range(N // 2):
            tree = tree * 2 + 1
        if N % 2:
            return tree * 2
        else:
            return tree
    elif start == 'summer':
        for i in range(N // 2):
            tree = (tree + 1) * 2
        if N % 2:
            return tree + 1
        else:
            return tree
    else:
        raise ValueError('start season must be spring or summer')

T = int(input().strip())

for i in range(T):
    print(tree_height(1, int(input().strip()), start='spring'))
