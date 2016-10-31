import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{label}: {time}'.format(label=label, time=end - start))


with timethis('counting'):
    n = 1000000
    while n > 0:
        n -= 1
