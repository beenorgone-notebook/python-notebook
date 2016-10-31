Python Quick References: Files & Directories
============================================

**Contents:**

1.	Working With Files And Directories
	1.	Working With Filenames and Directory Names
	2.	Listing Directories
	3.	Getting File Metadata
	4.	Constructing Absolute Pathnames
2.	Reading From Text Files
	1.	Reading Data From A Text File
	2.	Closing Files
	3.	Closing Files Automatically
	4.	Reading Data One Line At A Time
3.	Writing to Text Files
4.	Binary Files
5.	Stream Objects From Non-File Sources
	1.	Handling Compressed Files
6.	Standard Input, Output, and Error
	1.	Redirecting Standard Output

Working With Filenames and Directory
------------------------------------

```python
import os
print(os.getcwd()) # get current working directory
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

### Listing Directories

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

```python
metadata = os.stat('humansize.py')
metadata
#os.stat_result(st_mode=33204, st_ino=3805906, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=2525, st_atime=1463140481, st_mtime=1463140481, st_ctime=1463140481)
metadata.st_mtime
#1463140481.0080671
time.localtime(metadata.st_mtime)
#time.struct_time(tm_year=2016, tm_mon=5, tm_mday=13, tm_hour=18, tm_min=54, tm_sec=41, tm_wday=4, tm_yday=134, tm_isdst=0)
```

### Constructing Absolute Pathnames

```python
print(os.path.realpath('humansize'))
#/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples/humansize
print(os.path.realpath('humansize.py'))
#/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_3--dive-in/examples/humansize.py
```

Reading From Text Files
-----------------------

**Specify the encoding every time you open a file.**

```python
a_file = open('examples/chinese.txt', encoding='utf-8')
a_file.name
#'examples/chinese.txt'
a_file.encoding
#'utf-8'
a_file.mode
#'r'
```

| Character | Meaning                                                         |
|-----------|-----------------------------------------------------------------|
| 'r'       | open for reading (default)                                      |
| 'w'       | open for writing, truncating the file first                     |
| 'x'       | open for exclusive creation, failing if the file already exists |
| 'a'       | open for writing, appending to the end of the file if it exists |
| 'b'       | binary mode                                                     |
| 't'       | text mode (default)                                             |
| '+'       | open a disk file for updating (reading and writing)             |

### Reading Data From A Text File

```python
a_file = open('examples/chinese.txt', encoding='utf-8')
a_file.read()
#'Dive Into Python 是为有经验的程序员编写的一本 Python 书。\n'
a_file.read()
#''

a_file.seek(0) #The `seek()` method moves to a specific byte position in a file
#0
a_file.read(16)
#'Dive Into Python'
a_file.read(1)
#' '
a_file.read(1)
#'是'
a_file.tell() # The `tell()` method tell you which byte you're on
#20
a_file.seek(17)
#17
a_file.read(1)
#'是'
a_file.tell()
#20
```

### Closing Files

```python
a_file.close()
a_file.closed
True
```

### Closing Files Automatically

```python
with open('examples/chinese.txt', encoding='utf-8') as a_file:
a_file.seek(17)
a_character = a_file.read(1)
print(a_character)
```

### Reading Data One Line At A Time

*Python handles line endings automatically by default.*

```python
line_number = 1
with open('examples/favorite-people.txt', encoding='utf-8') as a_file:
for a_line in a_file:
print('{:>4} {}'.format(line_number, a_line.rstrip()))
line_number += 1
```

Writing to Text Files
---------------------

There are two file modes for writing:

-	“Write” mode will overwrite the file. Pass `mode='w'` to the `open()` function. "Write" mode will destroy all previos data in file.
-	“Append” mode will add data to the end of the file. Pass `mode='a'` to the `open()` function.

**Specify the encoding every time you open a file.**

```python
with open('test.log', mode='w', encoding='utf-8') as a_file:
  a_file.write('test succeeded')
with open('test.log', encoding='utf-8') as a_file:
  print(a_file.read())
#test succeeded
with open('test.log', mode='a', encoding='utf-8') as a_file:
  a_file.write('and again')
with open('test.log', encoding='utf-8') as a_file:
  print(a_file.read())
#test succeededand again
```

Binary Files
------------

```python
an_image = open('beauregard.jpg', mode='rb')
an_image.mode
'rb'
an_image.name
'beauregard.jpg'
an_image.coding
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
an_image.coding
AttributeError: '_io.BufferedReader' object has no attribute 'coding'

an_image.tell()
#0
data = an_image.read(3)
data
#b'\xff\xd8\xff'
type(data)
#<class 'bytes'>
an_image.tell()
#3
an_image.seek(0)
#0
data = an_image.read()
len(data)
#3150
```

Stream Objects From Non-File Sources
------------------------------------

`io.StringIO` lets you treat a string as a text file. There’s also a `io.BytesIO` class, which lets you treat a byte array as a binary file.

```python
a_string = 'PapayaWhip is the new black.'
import io
a_file = io.StringIO(a_string)
a_file.read()
#'PapayaWhip is the new black.'
a_file.read()
#''
a_file.seek(0)
#0
a_file.read(10)
#'PapayaWhip'
a_file.tell()
#10
a_file.seek(18)
#18
a_file.read()
#'new black.'
```

### Handling Compressed Files

```python
import gzip
with gzip.open('out.log.gz', mode='wb') as z_file:
  z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))

exit()
```

Standard Input, Output, and Error
---------------------------------

When you call the `print()` function, the thing you’re printing is sent to the `stdout` pipe. When your program crashes and prints out a traceback, it goes to the `stderr` pipe. By default, both of these pipes are just connected to the terminal window where you are working; when your program prints something, you see the output in your terminal window, and when a program crashes, you see the traceback in your terminal window too. In the graphical Python Shell, the `stdout` and `stderr` pipes default to your “Interactive Window”.

```python
for i in range(3):
  print('PapayaWhip')
#PapayaWhip
#PapayaWhip
#PapayaWhip

import sys
for i in range(3):
  l = sys.stdout.write('is the')
#is theis theis the
for i in range(3):
  l = sys.stderr.write('new black')
#new blacknew blacknew black

#`sys.stdout` and `sys.stderr` are stream objects, but they are write-only.
sys.stdout.read()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IOError: not readable
```

### Redirecting Standard Output

You can assign `sys.stdout` and `sys.stderr` a new value — any other stream object — to redirect their output.

```python
import sys

class RedirectStdoutTo:
    '''Redirect `stdout` to a stream object (ex: a file). Restore `stdout` to defauld ("Interactive Window) when exit.
    '''
  def __init__(self, out_new):
    self.out_new = out_new

  def __enter__(self):
    self.out_old = sys.stdout
    sys.stdout = self.out_new

  def __exit__(self, *args):
    sys.stdout = self.out_old

print('A')
with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
  print('B')
print('C')
```
