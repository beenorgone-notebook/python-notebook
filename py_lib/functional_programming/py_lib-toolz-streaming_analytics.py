# -*- encoding: utf-8 -*-

from cytoolz import first, join, reduceby, second, unique
from cytoolz.curried import (compose, filter, get, groupby, map, pipe, pluck,
                             valmap)

accounts = [(1, 'Alice', 100, 'F'),  # id, name, balance, gender
            (2, 'Bob', 200, 'M'),
            (3, 'Charlie', 150, 'M'),
            (4, 'Dennis', 50, 'M'),
            (5, 'Edith', 300, 'F')]


# I. SELECTING WITH `MAP()` AND `FILTER()`
# SELECT name, balance FROM accounts WHERE balance > 150

# Functional version with pipeline and curry
acc1 = pipe(accounts, filter(lambda account: account[2] > 150),
            map(get([1, 2])),
            list)
print(acc1)

# List comprehensions version (more Pythonic):
acc2 = [(name, balance) for (id, name, balance, gender) in accounts
        if balance > 150]
print(acc2)


# II. SPLIT-APPLY-COMBINE WITH `GROUPBY` AND `REDUCEBY`:
# 1. Split the dataset into groups by some property
# 2. Reduce each of the groups with some synopsis function

# In Memory Split-Apply-Combine
# SELECT gender, SUM(balance) FROM accounts GROUP BY gender;
print(groupby(get(3), accounts))
# {'M': [(2, 'Bob', 200, 'M'), (3, 'Charlie', 150, 'M'), (4, 'Dennis', 50, 'M')], 'F': [(1, 'Alice', 100, 'F'), (5, 'Edith', 300, 'F')]}
print(pipe(accounts, groupby(get(3)),
           valmap(compose(sum, pluck(2)))))
# {'M': 400, 'F': 400} (pluck item )


# Streaming Split-Apply-Combine
# the groupby operation is not streaming and so this approach is limited
# to datasets that can fit comfortably into memory.
# to achieves streaming split-apply-combine use `reduceby()`

# The `reduceby` operation takes a key function,
# like `get(3)` or `lambda x: x[3]`, and a binary operator like
# `add` or `lesser = lambda acc, x: acc if acc < x else x`.
# It successively applies the key function to each item in succession,
# accumulating running totals for each key by combining each new value
# with the previous using the binary operator.
# It can’t accept full reduction operations like `sum` or `min` as
# these require access to the entire group at once. Here's an example:
def iseven(n):
    return n % 2 == 0


def add(x, y):
    return x + y

print(reduceby(iseven, add, [1, 2, 3, 4]))  # {False: 4, True: 6}
# The even numbers are added together (2 + 4 = 6) into group True, and
# the odd numbers are added together (1 + 3 = 4) into group False.

# Here is the solution for our accounts example that
# adds up the balances for each group:
binop = lambda total, acc: total + acc[2]
print(reduceby(get(3), binop, accounts), 0)  # {'M': 400, 'F': 400}


# SEMI-STREAMING `JOIN`
# We register multiple datasets together with `join`.
# Consider a second dataset storing addresses by ID
addresses = [(1, '123 Main Street'),  # id, address
             (2, '5 Adams Way'),
             (5, '34 Rue St Michel')]

# SELECT accounts.name, addresses.address FROM accounts, addresses
# WHERE accounts.id = addresses.id;

result = join(first, accounts,
              first, addresses)

for ((id, name, bal, gender), (id, address)) in result:
    print((id, name, bal, gender), (id, address))
    print((name, address))

# toolz.itertoolz.join(leftkey, leftseq, rightkey, rightseq, left_default='__no__default__', right_default='__no__default__')
# This is a semi-streaming operation. The LEFT sequence is fully evaluated
# and placed into memory. The RIGHT sequence is evaluated lazily and so
# can be arbitrarily large.


# `JOIN` ON ARBITRARY FUNCTIONS / DATA
def isodd(x):
    return x % 2 == 1

print(list(join(iseven, [1, 2, 3, 4],
                isodd, [7, 8, 9])))
# [(2, 7), (4, 7), (1, 8), (3, 8), (2, 9), (4, 9)]

# `join` one-to-many or many-to-many relationships:
friends = [('Alice', 'Edith'),
           ('Alice', 'Zhao'),
           ('Edith', 'Alice'),
           ('Zhao', 'Alice'),
           ('Zhao', 'Edith')]

cities = [('Alice', 'NYC'),
          ('Dan', 'Syndey'),
          ('Alice', 'Chicago'),
          ('Edith', 'Paris'),
          ('Edith', 'Berlin'),
          ('Zhao', 'Shanghai')]

# In what cities do people have friends?
result = join(second, friends,
              first, cities)
for ((name, friend), (friend, city)) in sorted(unique(result)):
    print((name, city))
# ('Alice', 'Berlin')
# ('Alice', 'Paris')
# ('Alice', 'Shanghai')
# ('Edith', 'Chicago')
# ('Edith', 'NYC')
# ('Zhao', 'Chicago')
# ('Zhao', 'NYC')
# ('Zhao', 'Berlin')
# ('Zhao', 'Paris')
