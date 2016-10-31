# coding: utf-8
import os
import random
from multiprocessing import Pipe, Process


def producer_task(conn):
    value = random.randint(1, 10)
    conn.send(value)
    print('Value [%d] sent by PID [%d]' % (value, os.getpid()))
    conn.close()

# Never forget to always call the `close()` method of a `Pipe` connection
# which sends data through the `send` method. This is important to
# finalize resources associated with the channel of communication when
# this is no longer being used.


def consumer_task(conn):
    print('Value [%d] received by PID [%d]' % (conn.recv(), os.getpid()))

if __name__ == '__main__':
    producer_conn, consumer_conn = Pipe()
    consumer = Process(target=consumer_task, args=(consumer_conn,))
    producer = Process(target=producer_task, args=(producer_conn,))

    producer.start()
    consumer.start()
    # Make the main process waits for the execution of the producer and
    # consumer processes by calling `join()` method
    consumer.join()
    producer.join()
