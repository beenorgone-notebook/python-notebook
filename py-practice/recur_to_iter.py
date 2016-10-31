'''Get rid of recursion in the following function (using iteration)
In a nutshell:

1. Study the function.
2. Convert all recursive calls into tail calls. (If you can’t, stop. Try another method.)
3. Introduce a one-shot loop around the function body.
4. Convert tail calls into continue statements.
5. Tidy up.

Read more:
http://blog.moertel.com/posts/2013-05-11-recursive-to-iterative.html
'''


def find_val_or_next_smallest(bst, x):
    '''Get the greatest value <= x in a binary search tree (bst).
    Returns None if no such value can be found.
    https://github.com/tmoertel/recursion-to-iteration
    '''
    if bst is None:
        return None
    elif bst.val == x:
        return x
    elif bst.val > x:
        return find_val_or_next_smallest(bst.left, x)
    else:
        right_best = find_val_or_next_smallest(bst.right, x)
        if right_best is None:
            return bst.val
        return right_best
