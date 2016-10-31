# coding: utf-8

import logging
import threading
from queue import Queue

# Logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# defined the main data structures to be used
fibo_dict = {}
shared_queue = Queue()
input_list = [3, 10, 5, 7]  # simulates user input

# define an object from the threading module called `Condition`.
# This object aims to synchronize the access to resources according to
# a specific condition.
queue_condition = threading.Condition()


def fibonacci_task(condition):
    with condition:
        while shared_queue.empty():
            logger.info("[%s] - waiting for elements in queue..." %
                        threading.current_thread().name)
            condition.wait()
        else:
            value = shared_queue.get()
            fibo_dict[value] = fib(value)
            shared_queue.task_done()
            logger.debug("[%s] fibonacci of key [%d] with result [%d]" %
                         (threading.current_thread().name, value, fibo_dict[value]))


def fib(n):
    "Return fibonacci number nth"
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def queue_task(condition):
    logging.debug('Starting queue_task...')
    with condition:
        for item in input_list:
            shared_queue.put(item)
        logging.debug(
            "Notifying fibonacci_task threads that the queue is ready to consume..")
        condition.notifyAll()  # Notify condition that `shared_queue` is updated

threads = [threading.Thread(
    daemon=True, target=fibonacci_task, args=(queue_condition,)) for i in range(4)]  # Creation of Fibonacci threads

[thread.start() for thread in threads]  # Start Fibonacci threads

# Creation of queue update thread
prod = threading.Thread(name='queue_task_thread', daemon=True,
                        target=queue_task, args=(queue_condition,))

prod.start()  # Start queue update thread

# make the main thread wait for the execution of `threads` ends.
[thread.join() for thread in threads]

logger.info("[%s] - Result: %s" % (threading.current_thread().name, fibo_dict))
