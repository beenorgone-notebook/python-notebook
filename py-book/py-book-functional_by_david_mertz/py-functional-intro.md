# Functional Programming in Python by David Mertz: Preface

<!-- toc orderedList:0 -->

 - [Functional Programming in Python by David Mertz: Preface](#functional-programming-in-python-by-david-mertz-preface)

<!-- tocstop -->

 ## What Is Functional Programming?

- Functions are 1st class (objects)
- Recursion implementation
- Focus on list processing. Lists are often used with recursion on sublists as a substitute for loops.
- "Pure" functions vs. side effects.
- Worries about _what_ is to be computed rather than _how_ it is to be computed.
- Utilizes "higher order" functions.

## Beyond the Standard Library

- collections of higher-order functions
- tools for working lazily with iterators (`itertools`)
- examples:

  - [`pyrsistent`](http://pyrsistent.readthedocs.io/en/latest/intro.html): immutable data structures
  - [`toolz`](https://toolz.readthedocs.org/en/latest/): a set of utility functions for iterators, functions, and dictionaries (extend the standard libraries: `itertools`, `functools` and borrow from standard libraries of contemporary functional languages)
  - [`hypothesis`](http://hypothesis.readthedocs.io/en/latest/): a library for creating unit tests for finding edge cases in your code you wouldn't have thought to look for. It gererate random data matching your specification and checking that your guarantee still holds in that case (property-based testing)
  - [`more_itertools`](https://pythonhosted.org/more-itertools/api.html): useful compositions of iterators.
