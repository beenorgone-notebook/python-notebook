# Parallel Programming With Python by Jan Palach - Chap 1: Contextualizing, Parallel, Concurrent, and Distributed Programming

<!-- toc orderedList:0 -->

- [Parallel Programming With Python by Jan Palach - Chap 1: Contextualizing, Parallel, Concurrent, and Distributed Programming](#parallel-programming-with-python-by-jan-palach-chap-1-contextualizing-parallel-concurrent-and-distributed-programming)
	- [Resources](#resources)
	- [Why use parallel programming?](#why-use-parallel-programming)
	- [Exploring common forms of parallelization](#exploring-common-forms-of-parallelization)
	- [Communicating in parallel programming](#communicating-in-parallel-programming)
		- [Shared state](#shared-state)
		- [Message passing](#message-passing)
	- [Identifying parallel programming problems](#identifying-parallel-programming-problems)
		- [Deadlock](#deadlock)
		- [Starvation](#starvation)
		- [Race conditions](#race-conditions)
	- [Discovering Python's external parallel programming tools](#discovering-pythons-external-parallel-programming-tools)
		- [`parallel` module](#parallel-modulehttpparallelpythoncom)
		- [`celery` – a distributed task queue](#celery-a-distributed-task-queuehttpceleryprojectorg)

<!-- tocstop -->

 ## Resources

The Little Book of Semaphores by David Beazley

## Why use parallel programming?

Speed.

## Exploring common forms of parallelization

- _Concurrent programming_ is an abstraction from parallel programming.
- _Parallel systems_ run tasks simultaneously.
- _Distributed systems_ run tasks within physically-separated nodes.

Distributed programming is becoming more and more popular for many reasons:

- **Fault-tolerance**: As the system is decentralized, we can distribute the processing to different machines in a network, and thus perform individual maintenance of specific machines without affecting the functioning of the system as a whole.
- **Horizontal scalability**: We can increase the capacity of processing in distributed systems in general. We can link new equipment with no need to abort applications being executed. We can say that it is cheaper and simpler compared to vertical scalability.
- **Cloud computing**: With the reduction in hardware costs, we need the growth of this type of business where we can obtaining huge machine parks acting in a cooperative way and running programs in a transparent way for their users.

## Communicating in parallel programming

Two forms of communication in parallel programming: shared state & message passing.

### Shared state

has many pitfalls:

- an invalid operation made to the shared resource by one of the processes will affect all of the others, thereby producing bad results.
- impossible for the program to be distributed between multiple machines.

### Message passing

- When we aim to avoid data access control and synchronizing problems originating from shared state.
- Once data is copied at each message exchange, it is impossible that problems occur in terms of concurrence of access.
- Higher memory use than in shared memory state.
- Advantages:

  - Absence of data access concurrence
  - Messages can be exchange locally (various processes) or in distributed environments
  - This makes it less likely that scalability issues occur and enables interoperability of different systems
  - In general, it is easy to maintain according to programmers

> Two events are concurrent if we cannot tell by looking at the program which will happen first.

## Identifying parallel programming problems

### Deadlock

- a situation in which 2 or more workers keep _indefinitely_ waiting for the freeing of a resource,
- which is blocked by a worker of the same group for some reason.

> Deadlock is a phenomenon in which processes wait for a condition to free their tasks, but this condition will never occur.

### Starvation

> Starvation is caused by badly adjusted policies of process ranking.

### Race conditions

- Occur when the result of a process depends on a sequence of facts, and this sequence is broken due to the lack of synchronizing mechanisms
- extremely difficult to filter in larger systems.
- parallel programming is _non-determinism_.

> Non-determinism, if combined with lack of synchronization mechanisms, may lead to race condition issues.

## Discovering Python's external parallel programming tools

### [`parallel` module](http://parallelpython.com)

- Automatic detection of the optimal configuration
- The fact that a number of worker processes can be changed during runtime
- Dynamic load balance
- Fault tolerance
- Auto-discovery of computational resources

### [`celery` – a distributed task queue](http://celeryproject.org)
