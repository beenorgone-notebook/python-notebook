# Parallel Programming with Python by Jan Palach - Chap 5: Using Multiprocessing and ProcessPoolExecutor

<!-- toc orderedList:0 -->

 - [Parallel Programming with Python by Jan Palach - Chap 5: Using Multiprocessing and ProcessPoolExecutor](#parallel-programming-with-python-by-jan-palach-chap-5-using-multiprocessing-and-processpoolexecutor)

  - [Understanding the concept of a process](#understanding-the-concept-of-a-process)

    - [Understanding the process model](#understanding-the-process-model)
    - [Defining the states of a process](#defining-the-states-of-a-process)

  - [Implementing `multiprocessing` communication](#implementing-multiprocessinghttpdocspythonorg3librarymultiprocessinghtml-communication)

    - [Using `multiprocessing.Pipe`](#using-multiprocessingpipe)

  - [Understanding `multiprocessing.Queue`](#understanding-multiprocessingqueue)
  - [Using `multiprocessing` to compute Fibonacci series terms with multiple inputs](#using-multiprocessing-to-compute-fibonacci-series-terms-with-multiple-inputs)

<!-- tocstop -->

 ## Understanding the concept of a process

- Processes: containers for programs in execution and their resources.
- Have data area, child processes, estates, communication with other processes.

### Understanding the process model

- Operating System has [**Process Control Block (PCB)**](https://www.wikiwand.com/en/Process_control_block), which stores information referring to processes
- **Process ID**: the unique integer value (unsigned) identifies a process within the operational system.
- **Program counter**: contains the address of the next program instruction to be executed.
- **I/O information**: a list of open files and devices associated with the process.
- **Memory allocation**: stores information about the memory space used by and reserved for the process and the tables of paging.
- **CPU scheduling**: stores information about the priority of the process and points to the staggering queues.
- **Priority**: defines the priority that the process will have in the acquisition of the CPU.
- **Current state**: waiting or running, whether the process is ready.
- **CPU registry**: stores stack pointers and other information.

### Defining the states of a process

- **Running**: The process is making use of the CPU
- **Ready**: The process that was waiting in the processes queue is now ready to use the CPU
- **Waiting**: The process is waiting for some I/O operation related to the task it was executing

## Implementing [`multiprocessing`](http://docs.python.org/3/library/multiprocessing.html) communication

Allow two ways of communication among processes, both based on the message passing paradigm.

### Using `multiprocessing.Pipe`

_Pipe_: mechanism that establishes communication between two _endpoints_ (2 processes in communication).

Example:

> we will implement a Python program that creates two processes, A and B. Process A sends a random integer value in intervals from 1 to 10 to process B, and process B will display it on the screen.

code: [multiprocessing_pipe.py](assets/codes/chap_5_code/multiprocessing_pipe.py)

## Understanding `multiprocessing.Queue`

Interface are quite similar to `queue.Queue`.

## Using `multiprocessing` to compute Fibonacci series terms with multiple inputs

code: [multiprocessing_fibonacci.py](assets/codes/chap_5_code/multiprocessing_fibonacci.py)
