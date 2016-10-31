# You have data inside of a sequence, and need to extract values or
# reduce the sequence using some criteria.

# SOLUTION: list comprehension/generator expressions or
# filter(), itertools.compress()

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_pos_int(val):
    try:
        x = int(val)
        if x > 0:
            return True
        else:
            return False
    except ValueError:
        return False

pos_ints = tuple(filter(is_pos_int, values))
print(pos_ints)

# PROBLEM: You want to make a dictionary that is a subset of another dictionary.
# SOLUTION: dict comprehension
