[Dive into Python 3: Comprehensions](http://www.diveintopython3.net/comprehensions.html)
========================================================================================

Working With Files And Directories
----------------------------------

```python
import os
print(os.getcwd())
#/home/beenorgone
os.chdir('/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples')
print(os.getcwd())
#/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples
```

### Working With Filenames and Directory Names

```python
import os
print(os.path.join('/Users/pilgrim/diveintopython3/examples/', 'humansize.py'))
print(os.path.expanduser('~'))
#/home/beenorgone
print(os.path.expanduser('~'), 'Documents', 'gDrive')
#/home/beenorgone Documents gDrive
print(os.path.join('/home/beenorgone/', 'test.py'))
#/home/beenorgone/test.py #There're no test.py in my current home folder.
print(os.path.join('/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples', 'humansize.py'))
#/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples/humansize.py
pathname = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/ppython_3--dive-in/examples/humansize.py'
os.path.split(pathname)
#('/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples', 'humansize.py')
(dirname, filename) = os.path.split(pathname)
dirname
#'/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples'
filename
#'humansize.py'
(shortname, extension) = os.path.splitext(filename)
shortname
#'humansize'
extension
#'.py'
```

1.	The `split` function splits a full pathname and returns a tuple containing the path and filename.
2.	`os.path` also contains the `os.path.splitext()` function, which splits a filename and returns a tuple containing the filename and the file extension. You use the same technique to assign each of them to separate variables.

### Listing Directories

The `glob` module is another tool in the Python standard library. It’s an easy way to get the contents of a directory programmatically.

1.	The `glob` module takes a wildcard and returns the path of all files and directories matching the wildcard.
2.	The `os.chdir()` function can take relative pathnames.
3.	You can include multiple wildcards in your glob pattern.

```python
os.chdir('/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in')
print(os.getcwd())
#/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in
glob.glob('examples/*.py')
#['examples/humansize.py']
os.chdir('examples/')
print(os.getcwd())
#/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples
glob.glob('*man*.py')
#['humansize.py']
```

### Getting File Metadata

Every modern file system stores metadata about each file: creation date, last-modified date, file size, and so on. Python provides a single `api` to access this metadata. You don’t need to open the file; all you need is the filename.

The `time` module is part of the Python standard library. It contains functions to convert between different time representations, format time values into strings, and fiddle with timezones.

```python
metadata = os.stat('humansize.py')
metadata
#os.stat_result(st_mode=33204, st_ino=3805906, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=2525, st_atime=1463140481, st_mtime=1463140481, st_ctime=1463140481)
metadata.st_mtime
#1463140481.0080671
time.localtime(metadata.st_mtime)
#time.struct_time(tm_year=2016, tm_mon=5, tm_mday=13, tm_hour=18, tm_min=54, tm_sec=41, tm_wday=4, tm_yday=134, tm_isdst=0)
```

1.	`st_mtime` is the modification time, but it’s in a format that isn’t terribly useful. (Technically, it’s the number of seconds since the Epoch, which is defined as the first second of January 1st, 1970. Seriously.)
2.	The `time.localtime()` function converts a time value from seconds-since-the-Epoch (from the `st_mtime` property returned from the `os.stat()` function) into a more useful structure of year, month, day, hour, minute, second, and so on.
3.	The `os.stat()` function also returns the size of a file, in the `st_size` property.

### Constructing Absolute Pathnames

```python
print(os.path.realpath('humansize'))
#/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples/humansize
print(os.path.realpath('humansize.py'))
#/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples/humansize.py
```

List Comprehensions
-------------------

A list comprehension provides a compact way of mapping a list into another list by applying a function to each of the elements of the list.

```python
a_list = [1, 9, 8, 4]
[i * 2 for i in a_list]
#[2, 18, 16, 8]
a_list
#[1, 9, 8, 4]
```

1.	A list comprehension creates a new list; it does not change the original list.
2.	You can use any Python expression in a list comprehension, including the functions in the `os` module for manipulating files and directories.

You can use any Python expression in a list comprehension, including the functions in the `os` module for manipulating files and directories.

```python
os.chdir('/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in')
import os, glob
glob.glob('*')
#['python_3--dive-into_1st-program.md', 'python_3--dive-in_native-datatypes.md', 'examples', 'python_3--dive-into_comprehensions.md']
[os.path.realpath(f) for f in glob.glob('*.md')]
#['/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/python_3--dive-into_1st-program.md', '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/python_3--dive-in_native-datatypes.md', '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/python_3--dive-into_comprehensions.md']
[os.stat(f) for f in glob.glob('*.md')]
#[os.stat_result(st_mode=33204, st_ino=4471906, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=11261, st_atime=1463218242, st_mtime=1463143384, st_ctime=1463143391), os.stat_result(st_mode=33204, st_ino=6431693, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=19580, st_atime=1463218069, st_mtime=1463218069, st_ctime=1463218069), os.stat_result(st_mode=33204, st_ino=6431694, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=5097, st_atime=1463238749, st_mtime=1463238749, st_ctime=1463238749)]
```

List comprehensions can also filter items, producing a result that can be smaller than the original list.

```python
[f for f in glob.glob('*.md') if os.stat(f).st_size > 9500]
#['python_3--dive-into_1st-program.md', 'python_3--dive-in_native-datatypes.md']
[(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.md')]
#[(11261, '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/python_3--dive-into_1st-program.md'), (19580, '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/python_3--dive-in_native-datatypes.md'), (6798, '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/python_3--dive-into_comprehensions.md')]
```

Dictionary Comprehensions
-------------------------

A dictionary comprehension is like a list comprehension, but it constructs a dictionary instead of a list.

```python
metadata_dict = {f:os.stat(f) for f in glob.glob('*.md')}
type(metadata_dict)
#<class 'dict'>
metadata_dict.keys()
#dict_keys(['python_3--dive-into_1st-program.md', 'python_3--dive-into_comprehensions.md', 'python_3--dive-in_native-datatypes.md'])
dict_keys = metadata_dict.keys()
dict_keys
#dict_keys(['python_3--dive-into_1st-program.md', 'python_3--dive-into_comprehensions.md', 'python_3--dive-in_native-datatypes.md'])
#dict_keys[0]
#Traceback (most recent call last):
#  File "<pyshell#127>", line 1, in <module>
#    dict_keys[0]
#TypeError: 'dict_keys' object does not support indexing
type(dict_keys)
#<class 'dict_keys'>
#list(dict_keys)
#['python_3--dive-into_1st-program.md', 'python_3--dive-into_comprehensions.md', 'python_3--dive-in_native-datatypes.md']
metadata_dict['python_3--dive-into_1st-program.md']
#os.stat_result(st_mode=33204, st_ino=4471906, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=11261, st_atime=1463218242, st_mtime=1463143384, st_ctime=1463143391)
metadata_dict['python_3--dive-into_1st-program.md'].st_size
#11261
```

### Other Fun Stuff To Do With Dictionary Comprehensions

Swapping the keys and values of a dictionary.

```python
a_dict = {'a': 1, 'b': 2, 'c': 3}
a_dict.items()
#dict_items([('b', 2), ('a', 1), ('c', 3)])
type(a_dict.items())
#<class 'dict_items'>
{value:key for key, value in a_dict.items()}
#{1: 'a', 2: 'b', 3: 'c'}
```

Of course, this only works if the values of the dictionary are immutable, like strings or tuples. If you try this with a dictionary that contains lists, it will fail most spectacularly.

```python
a_dict = {'a':[1,2,3], 'b':4, 'c':5}
{value:key for key, value in a_dict.items()}
#Traceback (most recent call last):
#  File "<pyshell#141>", line 1, in <module>
#    {value:key for key, value in a_dict.items()}
#  File "<pyshell#141>", line 1, in <dictcomp>
#    {value:key for key, value in a_dict.items()}
#TypeError: unhashable type: 'list'
```

Set Comprehensions
------------------

Not to be left out, sets have their own comprehension syntax as well. It is remarkably similar to the syntax for dictionary comprehensions. The only difference is that sets just have values instead of key:value pairs.

Set comprehensions do not need to take a set as input; they can take any sequence.

```python
{2**x for x in range(10)}
#{32, 1, 2, 4, 8, 64, 128, 256, 16, 512}
```

Further Reading
---------------

-	The Python Standard Library by Example, Chapter 6: The File System by Doug Hellmann
-	[`os` module](http://docs.python.org/3/library/os.html)
-	[`os` — Portable access to operating system specific features](http://www.doughellmann.com/PyMOTW/os/)
-	[`os.path` module](http://docs.python.org/3/library/os.path.html)
-	[`os.path` — Platform-independent manipulation of file names](http://www.doughellmann.com/PyMOTW/ospath/)
-	[`glob` module](http://docs.python.org/3/library/glob.html)
-	[`glob` — Filename pattern matching](http://www.doughellmann.com/PyMOTW/glob)
-	[`time` module](http://docs.python.org/3/library/time.html)
-	[`time` — Functions for manipulating clock time](http://www.doughellmann.com/PyMOTW/time/)
-	[List comprehensions](http://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
-	[Nested list comprehensions](http://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
-	[Looping techniques](http://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
