# https://stackoverflow.com/questions/2154249/identify-groups-of-continuous-numbers-in-a-list

from itertools import chain, groupby
from operator import itemgetter

data = chain(range(0, 16), range(23, 45), range(12, 1, -1))

for key, group in groupby(enumerate(data), lambda x: x[0] - x[1]):
    print(list(map(itemgetter(1), group)))
