[Structuring Your Project](http://docs.python-guide.org/en/latest/writing/structure/)
=====================================================================================

Structure of the Repository
---------------------------

### Sample Repository

https://github.com/kennethreitz/samplemod

```
README.rst
LICENSE
Makefile
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/Makefile
docs/conf.py
docs/index.rst
docs/make.bat
tests/__init__.py
tests/context.py
tests/test_basic.py
tests/test_advanced.py
```

### The Actual Module

Your module package is the core focus of the repository. It should not be tucked away. If your module consists of only a single file, you can place it directly in the root of your repository:

`./sample/` or `./sample.py`

Your library does not belong in an ambiguous src or python subdirectory.

### License

This is arguably the most important part of your repository, aside from the source code itself. The full license text and copyright claims should exist in this file.

If you aren't sure which license you should use for your project, check out [choosealicense.com](http://choosealicense.com).

Of course, you are also free to publish code without a license, but this would prevent many people from potentially using your code.

### Setup.py

If your module package is at the root of your repository, this should obviously be at the root as well: `./setup.py`

### Requirements File

A [pip requirements file](https://pip.pypa.io/en/stable/user_guide/#requirements-files) should be placed at the root of the repository. It should specify the dependencies required to contribute to the project: testing, building, and generating documentation.

If your project has no development dependencies, or you prefer development environment setup via `setup.py`, this file may be unnecessary.
