# Object-Oriented Programming in Python

## Resources

[The Hitchhiker's Guide to Python - Object-Oriented Programming](http://docs.python-guide.org/en/latest/writing/structure/#object-oriented-programming)

- [Concurrency](https://techopedia.com/definition/27385/concurrency-databases)
- [Race-condition](https://www.wikiwand.com/en/Race_condition)

## Opinion

Avoid unnecessary object-orientation. Custom classes help us glueing together some state and some functionality. But, the problem comes from the "state" part of the equation.

in real world, using "state" means that you will have to deal with static information. This is prone to _concurrency problems_ or _race-conditions_. Using stateless functions may be a better programming paradigm.

> using functions and procedures with as few _implicit contexts_ and _side-effects_ as possible.

- A function's implicit context is made up of any of the global variables or items in the _persistence layer_ that are accessed from within the function.
- Side-effects are the changes that a function makes to its implicit context. If a function saves or deletes data in a global variable or in the persistence layer, it is said to have a side-effect.
