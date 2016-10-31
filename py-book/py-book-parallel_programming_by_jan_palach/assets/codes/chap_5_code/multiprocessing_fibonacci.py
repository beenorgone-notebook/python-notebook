# coding: utf-8

import logging
import os
import random
import sys
import time
from multiprocessing import (Manager, Pool, Process, Queue, cpu_count,
                             current_process)

# `cpu_count`: obtaining the quantity of CPUs in a machine
# `current_process`: obtaining information on the current process,
#   for example, its name
# `Manager`: object that allows sharing Python objects among different
#   processes by means of proxies

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


def producer_task(q, fibo_dict):
    for i in range(15):
        value = random.randint(1, 20)
        fibo_dict[value] = None
        logger.info("Producer [%s] putting value [%d] into queue.. "
                    % (current_process().name, value))
        q.put(value)


def consumer_task(q, fibo_dict):
    while not q.empty():
        value = q.get(True, 0.05)
        fibo_dict[value] = fib(value)
        logger.info("consumer [%s] getting value [%d] from queue..."
                    % (current_process().name, value))


def fib(n):
    "Return fibonacci number nth"
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    data_queue = Queue()
    number_of_cpus = cpu_count()
    manager = Manager()
    fibo_dict = manager.dict()

    producer = Process(target=producer_task, args=(data_queue, fibo_dict))
    producer.start()
    producer.join()

    consumer_list = []
    for i in range(number_of_cpus):
        consumer = Process(target=consumer_task, args=(data_queue, fibo_dict))
        consumer.start()
        consumer_list.append(consumer)

    [consumer.join() for consumer in consumer_list]

    logger.info(fibo_dict)
