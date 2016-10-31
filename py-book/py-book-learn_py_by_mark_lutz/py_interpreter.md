Python Interpreter
==================

CPython
-------

The standard The original, and standard, implementation of Python is usually called CPython when you want to contrast it with the other options (and just plain "Python" otherwise). This name comes from the fact that it is coded in portable ANSI C language code. This is the Python that you fetch from http://www.python.org, get with the ActivePython and Enthought distributions, and have automatically on most Linux and Mac OS X ma- chines. If you've found a preinstalled version of Python on your machine, it's probably CPython, unless your company or organization is using Python in more specialized ways.

Unless you want to script Java or .NET applications with Python or find the benefits of Stackless or PyPy compelling, you probably want to use the standard CPython sys- tem. Because it is the reference implementation of the language, it tends to run the fastest, be the most complete, and be more up-to-date and robust than the alternative systems. Figure 2-2 reflects CPython's runtime architecture.

![](/assets/cpython_execution_model.png)

Jython
------

Python for Java The Jython system (originally known as JPython) is an alternative implementation of the Python language, targeted for integration with the Java programming language. Jython consists of Java classes that compile Python source code to Java byte code and then route the resulting byte code to the Java Virtual Machine (JVM). Programmers still code Python statements in `.py` text files as usual; the Jython system essentially just replaces the rightmost two bubbles in Figure 2-2 with Java-based equivalents.

Jython's goal is to allow Python code to script Java applications, much as CPython allows Python to script C and C++ components. Its integration with Java is remarkably seamless. Because Python code is translated to Java byte code, it looks and feels like a true Java program at runtime. Jython scripts can serve as web applets and servlets, build Java-based GUIs, and so on. Moreover, Jython includes integration support that allows Python code to import and use Java classes as though they were coded in Python, and Java code to run Python code as an embedded language. Because Jython is slower and less robust than CPython, though, it is usually seen as a tool of interest primarily to Java developers looking for a scripting language to serve as a frontend to Java code. See Jython's website http://jython.org for more details.

IronPython: Python for .NET
---------------------------

A third implementation of Python, and newer than both CPython and Jython, IronPy- thon is designed to allow Python programs to integrate with applications coded to work with Microsoft's .NET Framework for Windows, as well as the Mono open source equivalent for Linux. .NET and its C# programming language runtime system are de- signed to be a language-neutral object communication layer, in the spirit of Microsoft's earlier COM model. IronPython allows Python programs to act as both client and server components, gain accessibility both to and from other .NET languages, and leverage .NET technologies such as the Silverlight framework from their Python code.

By implementation, IronPython is very much like Jython (and, in fact, was developed by the same creator)--it replaces the last two bubbles in Figure 2-2 with equivalents for execution in the .NET environment. Also like Jython, IronPython has a special focus -- it is primarily of interest to developers integrating Python with .NET components. Formerly developed by Microsoft and now an open source project, IronPython might also be able to take advantage of some important optimization tools for better perfor- mance. For more details, consult http://ironpython.net and other resources to be had with a web search.

Stackless: Python for concurrency
---------------------------------

Still other schemes for running Python programs have more focused goals. For example, the Stackless Python system is an enhanced version and reimplementation of the standard CPython language oriented toward concurrency. Because it does not save state on the C language call stack, Stackless Python can make Python easier to port to small stack architectures, provides efficient multiprocessing options, and fosters novel programming structures such as coroutines.

Among other things, the microthreads that Stackless adds to Python are an efficient and lightweight alternative to Python's standard multitasking tools such as threads and processes, and promise better program structure, more readable code, and increased programmer productivity. CCP Games, the creator of EVE Online, is a well-known Stackless Python user, and a compelling Python user success story in general. Try http: //stackless.com for more information.

PyPy: Python for speed
----------------------

The PyPy system is another standard CPython reimplementation, focused on perfor- mance. It provides a fast Python implementation with a JIT (just-in-time) compiler, provides tools for a "sandbox" model that can run untrusted code in a secure environment, and by default includes support for the prior section's Stackless Python systems and its microthreads to support massive concurrency.

PyPy is the successor to the original Psyco JIT, described ahead, and subsumes it with a complete Python implementation built for speed. A JIT is really just an extension to the PVM--the rightmost bubble in Figure 2-2--that translates portions of your byte code all the way to binary machine code for faster execution. It does this as your program is running, not in a prerun compile step, and is able to created type-specific machine code for the dynamic Python language by keeping track of the data types of the objects your program processes. By replacing portions of your byte code this way, your program runs faster and faster as it is executing. In addition, some Python programs may also take up less memory under PyPy.

It runs most CPython code, though C extension modules must generally be recompiled, and PyPy has some minor but subtle language differences, including garbage collection semantics that obviate some com- mon coding patterns. For instance, its non-reference-count scheme means that temporary files may not close and flush output buffers immediately, and may require manual close calls in some cases.

In return, your code may run much quicker. PyPy currently claims a 5.7X speedup over CPython across a range of benchmark programs (per http://speed.pypy.org/). In some cases, its ability to take advantage of dynamic optimization opportunities can make Python code as quick as C code, and occasionally faster. This is especially true for heavily algorithmic or numeric programs, which might otherwise be recoded in C. For instance, in one simple benchmark we'll see in Chapter 21, PyPy today clocks in at 10X faster than CPython 2.7, and 100X faster than CPython 3.X. Though other benchmarks will vary, such speedups may be a compelling advantage in many domains, perhaps even more so than leading-edge language features. Just as important, memory space is also optimized in PyPy--in the case of one posted benchmark, requiring 247 MB and completing in 10.3 seconds, compared to CPython's 684 MB and 89 seconds. PyPy's tool chain is also general enough to support additional languages, including Pyrolog, a Prolog interpreter written in Python using the PyPy translator. Search for PyPy's website for more. PyPy currently lives at http://pypy.org, though the usual web search may also prove fruitful over time. For an overview of its current performance, also see http://www.pypy.org/performance.html.

> Naturally the only benchmark that truly matters is your own code, and there are cases where CPython wins the race; PyPy's file iterators, for instance, may clock in slower today. Still, given PyPy's focus on performance over language mutation, and especially its support for the numeric domain, many today see PyPy as an important path for Python. If you write CPU-intensive code, PyPy deserves your attention.
