# Parallel Programming With Python by Jan Palach - Chap 4: Using the `threading` and `concurrent.futures` Modules

<!-- toc orderedList:0 -->

 - [Parallel Programming With Python by Jan Palach - Chap 4: Using the `threading` and `concurrent.futures` Modules](#parallel-programming-with-python-by-jan-palach-chap-4-using-the-threading-and-concurrentfutures-modules)

  - [Defining threads](#defining-threads)

    - [Advantages and disadvantages of using threads](#advantages-and-disadvantages-of-using-threads)
    - [Understanding different kinds of threads](#understanding-different-kinds-of-threads)
    - [Defining the states of a thread](#defining-the-states-of-a-thread)
    - [Choosing between `threading` and `_thread`](#choosing-between-threading-and-_thread)

  - [Using threading to obtain the Fibonacci series term with multiple inputs](#using-threading-to-obtain-the-fibonacci-series-termpy-parallel-c3_parallelizable_problemmd-with-multiple-inputs)
  - [Crawling the Web using the `concurrent.futures` module](#crawling-the-webpy-parallel-c3_parallelizable_problemmd-using-the-concurrentfutures-module)

    - [Problem and Solution](#problem-and-solution)

<!-- tocstop -->

 ## Defining threads

- Threads are different execution lines in a process.
- Threads belong to the same process and share the same memory space.
- the developer's task is to control and access these areas of memory.

### Advantages and disadvantages of using threads

Advantages:

- Fast communication between threads in the same process, data location and shared information.
- Thread creation is less costly than process creation (not necessary to copy all the context information).
- Best use of data locality by optimizing memory access through the processor cache memory.

Disadvantages:

- Difficult-to-solve errors by inexperienced developers.
- Data sharing limits the flexibility of the solution:

  - Painful migrating
  - Limits the scalability of algorithms

> Within the Python programming language, the use of CPU-bound threads may harm performance of the application due to GIL.

### Understanding different kinds of threads

**Kernel threads**: created and managed by the operating system.

- Advantages:

  - One kernel thread is referenced to one process. So if a kernel thread blocks, others can still run.
  - The kernel threads can run on different CPUs.

- Disadvantages:

  - The creation and synchronization routines are too expensive
  - The implementation is platform dependent

**User threads**: controlled by the package developer.

- Advantages:

  - The user thread has low cost for creation and synchronization
  - The user thread is platform independent

- Disadvantages:

  - All the user threads inside a process are related to only one kernel thread. So, if one user thread blocks, all the other user threads can't run.
  - The user threads can't run on different CPUs.

### Defining the states of a thread

- Five possible states
- **Creation**: the main process that creates a thread, after its creation, it is sent to a line of threads ready for execution.
- **Execution**: the thread makes use of the CPU
- **Ready**: the thread is in a line of threads ready for execution and bound to be executed.
- **Blocked**: the thread is blocked to wait for sth happen, doesn't make use of the CPU.
- **Concluded**: end the life span of the thread.

### Choosing between `threading` and `_thread`

The `threading` module offers a friendly interface for the `_thread` module, making its use more convenient.

## Using threading to obtain [the Fibonacci series term](py-parallel-c3_parallelizable_problem.md) with multiple inputs

> The mission is to parallelize the execution of the terms of the Fibonacci series when multiple input values are given. For tactical purposes, we will fix the input values in the four elements and the four threads to process each element, simulating a perfect symmetry among workers and tasks to be executed. The algorithm will work as follows:

> 1. First, a list will store the four values to be calculated and the values will be sent into a structure that allows synchronized access of threads.
> 2. After the values are sent to the synchronized structure, the threads that calculate the Fibonacci series need to be advised that the values are ready to be processed. For this, we will use a thread synchronization mechanism called `Condition`. (The `Condition` mechanism is one of the Python objects that offer data access synchronization mechanisms shared among threads; you can learn more at <http://docs.python.org/3/library/threading.html#threading.Condition>.)
> 3. After each thread finishes their Fibonacci series calculation, the results will be saved in a dictionary.

code: [parallel_fibonacci.py](assets/codes/chap_4_code/parallel_fibonacci.py)

```
threads start -> condition -> check queue empty or not
    if Yes -> wait
    if No -> get data from queue -> do task -> report to queue (update state)
queue update task start -> check input data exist or not
    if No -> wait
    if Yes -> get data -> update queue with data -> notify condition that queue is not empty
```

## [Crawling the Web](py-parallel-c3_parallelizable_problem.md) using the `concurrent.futures` module

> In the previous example, in which we analyzed `parallel_fibonacci.py`, quite primitive forms of threads were used. Also, at a specific moment, we had to create and initialize more than one thread manually. In larger programs, it is very difficult to manage this kind of situation. In such case, there are mechanisms that allow a thread pool.

- Thread pool: a structure that keeps several threads, which are previously created, to be used in a certain process.
- Aims to reuse threads, thus avoiding unnecessary costly creation of threads

### Problem and Solution

> A Web crawler consists of a computer program that browses the Web to search for information on pages. The scenario to be analyzed is a problem in which a sequential Web crawler is fed by a variable number of Uniform Resource Locators (URLs), and it has to search all the links within each URL provided. Imagining that the number of input URLs may be relatively large, we could plan a solution looking for parallelism in the following way:

> 1. Group all the input URLs in a data structure.
> 2. Associate data URLs with tasks that will execute the crawling by obtaining information from each URL.
> 3. Dispatch the tasks for execution in parallel workers.
> 4. The result from the previous stage must be passed to the next stage, which will improve raw collected data, thereby saving them and relating them to the original URLs.

code: [parallel_web_crawler.py](assets/codes/chap_4_code/parallel_web_crawler.py)
