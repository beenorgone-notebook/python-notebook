# You have a list of dictionaries and you would like to sort the
# entries according to one or more of the dictionary values.

# SOLUTION: Use operator.itemgetter or lambda

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# operator.itemgetter version, with help from functools.partial

from functools import partial
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)

sort_by_fname_func = partial(sorted, key=itemgetter('fname'))
print(sort_by_fname_func(rows))

sort_by_fname_lname_func = partial(sorted, key=itemgetter('fname', 'lname'))
print(sort_by_fname_lname_func(rows))

# lambda version:

rows_by_fname = sorted(rows, key=lambda x: x['fname'])

# You can also use `key` to sort objects of the same class,
# if they don’t natively support comparison operations

# SOLUTION: operator.attrgetter
