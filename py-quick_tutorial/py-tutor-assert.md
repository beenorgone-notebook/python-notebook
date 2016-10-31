# [UsingAssertionsEffectively - Python Wiki](https://wiki.python.org/moin/UsingAssertionsEffectively)

## Notes

Places to consider putting assertions:

- checking parameter types, classes, or values
- checking data structure invariants
- checking "can't happen" situations (duplicates in a list, contradictory state variables.)
- after calling a function, to make sure that its return is reasonable

If something does go wrong, we want to make it completely obvious as soon as possible.

It's easier to catch incorrect data at the point where it goes in than to work out how it got there later when it causes trouble.
