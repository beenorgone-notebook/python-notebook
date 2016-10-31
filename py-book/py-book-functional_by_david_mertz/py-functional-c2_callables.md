# Functional Programming in Python - Chap II: Callables


<!-- toc orderedList:0 -->

- [Functional Programming in Python - Chap II: Callables](#functional-programming-in-python-chap-ii-callables)
	- [Closures vs. Callable Instances](#closures-vs-callable-instances)
	- [Multiple Dispatch](#multiple-dispatch)

<!-- tocstop -->

Several different ways to create functions in Python:

- `def`
- `lambda`
- `__call()__` method
- Closures returned by function factories
- Static methods of instances
- Generators

## Closures vs. Callable Instances

```python
# A class that creates callable adder instances
class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, m):
        return self.n + m

add5_i = Adder(5)  # "instance" or "imperative"

# A closure:
def make_adder(n):
    def adder(m):
        return m + n
    return adder

add5_f = make_adder(5)  # "functional"

add5_i(10) # 15
add5_f(10) # 15 (only argument affects result)
add5_i.n = 10  # state is readily changeable
add5_i(10)  # 20 (result is dependent on prior flow)
```

## Multiple Dispatch

- An approach to programming multiple paths of execution
- Idea: declare multiple signatures for a single function and call the actual computation that matches the types or properties of the calling arguments.
- Help avoid or reduce the use of explicitly conditional branching
- [`multipledispatch` module](http://multiple-dispatch.readthedocs.org/en/latest/)

Example: [implement the game of rock/paper/scissors](../../py-recipes/mutilpe_dispatch-rock_paper_scissors.py)
