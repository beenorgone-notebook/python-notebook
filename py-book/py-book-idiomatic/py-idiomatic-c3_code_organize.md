# Writing Idiomatic Python - Chap 3: Organizing your Code

<!-- toc orderedList:0 -->

- [Writing Idiomatic Python - Chap 3: Organizing your Code](#writing-idiomatic-python-chap-3-organizing-your-code)
	- [Modules and Packages](#modules-and-packages)
		- [Use modules for encapsulation where other languages would use Objects](#use-modules-for-encapsulation-where-other-languages-would-use-objects)
	- [Formatting](#formatting)
		- [Use all capital letters when declaring global constant values](#use-all-capital-letters-when-declaring-global-constant-values)
		- [Avoid placing multiple statements on a single line](#avoid-placing-multiple-statements-on-a-single-line)
		- [Format your code according to PEP8](#format-your-code-according-to-pep8)
	- [Executable Scripts](#executable-scripts)
		- [Use `sys.exit` in your script to return proper error codes](#use-sysexit-in-your-script-to-return-proper-error-codes)
		- [Use the if `__name__ == '__main__'` pattern to allow a file to be both imported and run directly](#use-the-if-__name__-__main__-pattern-to-allow-a-file-to-be-both-imported-and-run-directly)
	- [Imports](#imports)
		- [Prefer **absolute imports** to **relative imports**](#prefer-absolute-imports-to-relative-imports)
		- [Do not use `from foo import *` to import the contents of a module.](#do-not-use-from-foo-import-to-import-the-contents-of-a-module)
		- [Arrange your `import` statements in a standard order](#arrange-your-import-statements-in-a-standard-order)

<!-- tocstop -->

 ## Modules and Packages

### Use modules for encapsulation where other languages would use Objects

Most data that would otherwise stored in a class can be represented using the simple `list` , `dict` , and `set` types. Python has a wide variety of built-in functions and standard library modules optimized (both in design and implementation) to interact with them. One can make a compelling case that classes should be used only when necessary and almost never at API boundaries.

## Formatting

### Use all capital letters when declaring global constant values

### Avoid placing multiple statements on a single line

### Format your code according to PEP8

## Executable Scripts

### Use `sys.exit` in your script to return proper error codes

Create a `main` function that contains the code to be run as a script. Use `sys.exit` in `main` to return error codes if something goes wrong or zero if everything runs to completion.

```python
# Harmful
if __name__ == '__main__':
    import sys
    # What happens if no argument is passed on the command line?
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        result = do_stuff(argument)
        # Again, what if this is False? How would other programs knows?
        if result:
            do_stuff_with_result(result)

# Idiomatic
def main():
    import sys
    if len(sys.argv) < 2:
        # Calling sys.exit with a string automatically
        # prints the string to stderr and exits with
        # a value of '1' (error)
        sys.exit('You forget to pass an argument')
    argument = sys.argv[1]
    result = do_stuff(argument)
    if not result:
        sys.exit(1)
        # We can also exit with just the return code
    do_stuff_with_result(result)
    # Optional, since the return value without this return
    # statment would default to None, which sys.exit treats
    # as 'exit with 0'
    return 0
# The three lines below are the canonical script entry
# point lines. You'll see them often in other Python scripts
if __name__ == '__main__':
    sys.exit(main())
```

### Use the if `__name__ == '__main__'` pattern to allow a file to be both imported and run directly

Unlike the `main()` function available in some languages, Python has no built-in notion of a main entry point. Rather, the interpreter immediately begins executing statements upon loading a Python source file. If you want a file to function both as an importable Python module and a stand-alone script, use the if `__name__ == '__main__'` idiom.

## Imports

### Prefer **absolute imports** to **relative imports**

```python
# Relative import clutter a module's namespace
from package import module

# Absolute import
import package.module
import package.other_module as other
```

### Do not use `from foo import *` to import the contents of a module.

### Arrange your `import` statements in a standard order

Order recommended by Python Programming FAQ:

1. standard library modules
2. third-party library modules installed in site-packages
3. modules local to the current project
