# # coding: utf-8

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import numpy as np

# Logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# parallel matrix scalar multiplication
MATRIX_A = [[33, 23, 12], [23, 2, 4], [1, 4, 9]]
SCALAR = 6

# Numpy solution
np_array = np.array(MATRIX_A)
sp = SCALAR * np_array
print(sp)  # runtime is ~0.3s
'''[[198 138  72]
 [138  12  24]
 [  6  24  54]]'''

# Parallel solution
PRODUCT = [[], [], []]
print(PRODUCT)
SHARED_QUEUE = Queue()
QUEUE_CONDITION = threading.Condition()


def scalar_multiple_task(condition):
    with condition:
        while SHARED_QUEUE.empty():
            logger.info(
                "{} - waiting for elements in queue...".format(threading.current_thread().name))
            condition.wait()
        else:
            value, indices = SHARED_QUEUE.get()
            PRODUCT
