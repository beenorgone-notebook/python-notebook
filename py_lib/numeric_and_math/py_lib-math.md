[Python: `math` - Mathetical functions](https://docs.python.org/3/library/math.html)
====================================================================================

```python
import math
math.ceil(12.35435)
#13
math.copysign(145, 12.01)
#145.0
math.copysign(1224, -1)
#-1224.0
math.factorial(12)
#479001600
math.floor(13.8434)
#13
math.fmod(17,3)
#2.0
math.fmod(12424,7)
#6.0
math.fmod(-17/3)
#2.0
-17 % 3
#1
```

1.	`fmod(x, y)` be exactly (mathematically; to infinite precision) equal to `x - n*y` for some integer `n` such that the result has the same sign as `x` and magnitude less than `abs(y)`.
2.	function `fmod()` is generally preferred when working with floats, while Python’s `x % y` is preferred when working with integers.
