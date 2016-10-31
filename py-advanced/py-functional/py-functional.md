# Functional programming in Python

<!-- toc orderedList:0 -->

 - [Functional programming in Python](#functional-programming-in-python)

  - [Resources](#resources)
  - [Functional Programming in Python](#functional-programming-in-python-1)

    - [Eliminating Flow Control](#eliminating-flow-control)
    - [Eliminating Loops](#eliminating-loops)
    - [Eliminating side-effects](#eliminating-side-effects)

<!-- tocstop -->

 ## Resources

[A practical intro to Functional Programming by Sachin Joglekar](https://codesachin.wordpress.com/2016/04/03/a-practical-introduction-to-functional-programming-for-python-coders/)

- [Can all iterative algorithms be modelled recursively and vice-versa? - Quora topic](https://www.quora.com/Can-all-iterative-algorithms-be-modelled-recursively-and-vice-versa)

[A practical introduction to functional programming](https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming) by Mary Rose Cook

Charming Python: Functional programming in Python:

- [Part 1](https://www.ibm.com/developerworks/library/l-prog/)
- [Part 2](https://www.ibm.com/developerworks/library/l-prog2/)
- [Part 3](https://www.ibm.com/developerworks/library/l-prog3/)

## Functional Programming in Python

### Eliminating Flow Control

```python
# Normal statement-based flow control
if cond1:   func1()
elif cond2: func2()
else:         func3()

# Equivalent "short circuit" expression
(cond1 and func1()) or (cond2 and func2()) or (func3())
```

### Eliminating Loops

See `py-functional_style.py`

### Eliminating side-effects
