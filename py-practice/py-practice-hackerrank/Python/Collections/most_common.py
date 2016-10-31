# https://www.hackerrank.com/challenges/most-commons
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass

a_string = input().strip()
character_counts = OrderedCounter(sorted(a_string))
# An OrderedDict is a dict that remembers the order that keys were first inserted.
# So we need to sort a_string before apply OrderedCounter

for pair in character_counts.most_common(3):
    print(*pair)

# TODO: Read
# https://docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes
