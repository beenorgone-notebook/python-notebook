# tail-call recursion version:


def factorial_tail(n, acc=1):
    if n < 2:
        return 1 * acc
    else:
        return factorial_tail(n - 1, acc * n)


# Iterate version:

def factorial_iter(n, acc=1):
    while True:
        if n < 2:
            return 1 * acc
        (n, acc) = (n - 1, acc * n)
        continue
        break
