[`unittest` -- Unit testing framework](https://docs.python.org/3/library/unittest.html)
=======================================================================================

| Method                      | Checks that            | New in |
|-----------------------------|------------------------|--------|
| `assertEqual(a, b)`         | `a == b`               |        |
| `assertNotEqual(a, b)`      | `a != b`               |        |
| `assertTrue(x)`             | `bool(x) is True`      |        |
| `assertFalse(x)`            | `bool(x) is False`     |        |
| `assertIs(a, b)`            | `a is b`               | 3.1    |
| `assertIsNot(a, b)`         | `a is not b`           | 3.1    |
| `assertIsNone(x)`           | `x is None`            | 3.1    |
| `assertIsNotNone(x)`        | `x is not None`        | 3.1    |
| `assertIn(a, b)`            | `a in b`               | 3.1    |
| `assertNotIn(a, b)`         | `a not in b`           | 3.1    |
| `assertIsInstance(a, b)`    | `isinstance(a, b)`     | 3.2    |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` | 3.2    |

| Method                                          | Checks that                                                          | New in |
|-------------------------------------------------|----------------------------------------------------------------------|--------|
| `assertRaises(exc, fun, *args, **kwds)`         | `fun(*args, **kwds)` raises exc                                      |        |
| `assertRaisesRegex(exc, r, fun, *args, **kwds)` | `fun(*args, **kwds)` raises `exc` and the message matches regex `r`  | 3.1    |
| `assertWarns(warn, fun, *args, **kwds)`         | `fun(*args, **kwds)` raises `warn`                                   | 3.2    |
| `assertWarnsRegex(warn, r, fun, *args, **kwds)` | `fun(*args, **kwds)` raises `warn` and the message matches regex `r` | 3.2    |
| `assertLogs(logger, level)`                     | The with block logs on `logger` with minimum `level`                 |        |

-	exc = exception
-	fun = callable function
