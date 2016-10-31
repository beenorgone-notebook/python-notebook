[Dive into Python 3: Files](http://www.diveintopython3.net/files.html)
======================================================================

Reading From Text Files
-----------------------

Python has a built-in `open()` function, which takes a filename as an argument.

### Character Encoding Rears Its Ugly Head

Bytes are bytes; characters are an abstraction. A string is a sequence of Unicode characters. But a file on disk is not a sequence of Unicode characters; a file on disk is a sequence of bytes. So if you read a “text file” from disk, how does Python convert that sequence of bytes into a sequence of characters? It decodes the bytes according to a specific character encoding algorithm and returns a sequence of Unicode characters (otherwise known as a string).

```python
# This example was created on Windows. Other platforms may
# behave differently, for reasons outlined below.
file = open('examples/chinese.txt')
a_string = file.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python31\lib\encodings\cp1252.py", line 23, in decode
return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 28: character maps to <undefined>
```

You didn’t specify a character encoding, so Python is forced to use the default encoding. What’s the default encoding? If you look closely at the traceback, you can see that it’s dying in `cp1252.py`, meaning that Python is using `CP-1252` as the default encoding here. (`CP-1252` is a common encoding on computers running Microsoft Windows.) The `CP-1252` character set doesn’t support the characters that are in this file, so the read fails with an ugly `UnicodeDecodeError`.

> If you need to get the default character encoding, import the locale module and call `locale.getpreferredencoding()`. Your results may be different (even on Windows) depending on which version of your operating system you have installed and how your regional/language settings are configured. This is why it’s so important to **specify the encoding every time you open a file.**

### Stream Objects

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
```

1\. Once you open a file (with the correct encoding), reading from it is just a matter of calling the stream object’s read() method. The result is a string.

2\. Reading the file again does not raise an exception. Python does not consider reading past end-of-file to be an error; it simply returns an empty string.

What if you want to re-read a file?

```python
# continued from the previous example
a_file.read()
#''
a_file.seek(0)
#0
a_file.read(16)   
#'Dive Into Python'
a_file.read(1)
#' '
a_file.read(1)
#'是'
a_file.tell()
#20
```

1.	The `seek()` method moves to a specific byte position in a file.
2.	The `read()` method can take an optional parameter, the number of characters to read.
3.	If you like, you can even read one character at a time.
4.	The `tell()` method tell you which byte you're on.

```python
# continued from the previous example
a_file.seek(17)
#17
a_file.read(1)
#'是'
a_file.tell()
#20
```

The `seek()` and `tell()` methods always count bytes, but since you opened this file as text, the `read()` method counts characters. Chinese characters require multiple bytes to encode in `utf-8`. The English characters in the file only require one byte each, so you might be misled into thinking that the `seek()` and `read()` methods are counting the same thing. But that’s only true for some characters.

```python
a_file.seek(18)
#18
a_file.read(1)
#Traceback (most recent call last):
#  File "<pyshell#17>", line 1, in <module>
a_file.read(1)
#  File "/usr/lib/python3.5/codecs.py", line 321, in decode
#(result, consumed) = self._buffer_decode(data, self.errors, final)
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0x98 in position 0: invalid start byte
```

Why does this fail? Because there isn’t a character at the `18th` byte. The nearest character starts at the `17th` byte (and goes for three bytes). Trying to read a character from the middle will fail with a `UnicodeDecodeError`.

### Closing Files

> Open files consume system resources, and depending on the file mode, other programs may not be able to access them. It’s important to close files as soon as you’re finished with them.

```python
a_file.close()
a_file.read()
#Traceback (most recent call last):
#  File "<pyshell#19>", line 1, in <module>
a_file.read()
#ValueError: I/O operation on closed file.
a_file.seek(0)
#Traceback (most recent call last):
#  File "<pyshell#20>", line 1, in <module>
a_file.seek(0)
#ValueError: I/O operation on closed file.
a_file.tell()
#Traceback (most recent call last):
#  File "<pyshell#21>", line 1, in <module>
a_file.tell()
#ValueError: I/O operation on closed file.
a_file.closed
True
```

1\. When calling `close()` method, the stream object `a_file` still exists. Calling its `close()` method doesn’t destroy the object itself. But it’s not terribly useful.

2\. You can't seek in and read from or use `tell()` with a closed file.

3\. Closed stream objects do have one useful attribute: the closed attribute will confirm that the file is closed.

### Closing Files Automatically

what happens if your code has a bug and crashes before you call `close()`? That file could theoretically stay open for much longer than necessary. While you’re debugging on your local computer, that’s not a big deal. On a production server, maybe it is.

```python
with open('examples/chinese.txt', encoding='utf-8') as a_file:
a_file.seek(17)
a_character = a_file.read(1)
print(a_character)
```

The `with` statement starts a code block, like an `if` statement or a `for` loop. Inside this code block, you can use the variable `a_file` as the stream object returned from the call to `open()`. All the regular stream object methods are available — `seek()`, `read()`, whatever you need. When the with block ends, Python calls `a_file.close()` automatically.

No matter how or when you exit the `with` block, Python will close that file… even if you “exit” it via an unhandled exception.

> In technical terms, the with statement creates a runtime context. In these examples, the stream object acts as a context manager. Python creates the stream object `a_file` and tells it that it is entering a runtime context. When the `with` code block is completed, Python tells the stream object that it is exiting the runtime context, and the stream object calls its own `close()` method. See [Appendix B, “Classes That Can Be Used in a with Block”](http://www.diveintopython3.net/special-method-names.html#context-managers) for details.

There’s nothing file-specific about the `with` statement; it’s just a generic framework for creating runtime contexts and telling objects that they’re entering and exiting a runtime context. If the object in question is a stream object, then it does useful file-like things (like closing the file automatically). But that behavior is defined in the stream object, not in the `with` statement.

### Reading Data One Line At A Time

*Text files can use several different characters to mark the end of a line.* Every operating system has its own convention. Some use a carriage return character, others use a line feed character, and some use both characters at the end of every line.

*Python handles line endings automatically by default.*

```python
line_number = 1
with open('examples/favorite-people.txt', encoding='utf-8') as a_file:
for a_line in a_file:
print('{:>4} {}'.format(line_number, a_line.rstrip()))
line_number += 1
```

To read a file one line at a time, use a `for` loop. Besides having explicit methods like `read()`, the stream object is also an iterator which spits out a single line every time you ask for a value.

Using the `format()` string method, you can print out the line number and the line itself. The format specifier `{:>4}` means “print this argument right-justified within 4 spaces.” The `a_line` variable contains the complete line, carriage returns and all. The `rstrip()` string method removes the trailing whitespace, including the carriage return characters.

Writing to Text Files
---------------------

There are two file modes for writing:

-	“Write” mode will overwrite the file. Pass `mode='w'` to the `open()` function.
-	“Append” mode will add data to the end of the file. Pass `mode='a'` to the `open()` function.

Either mode will create the file automatically if it doesn’t already exist.

You should always close a file as soon as you’re done writing to it, to release the file handle and ensure that the data is actually written to disk.

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

1\. The `mode='w'` parameter means open the file for writing. Yes, that’s all as dangerous as it sounds. I hope you didn’t care about the previous contents of that file (if any), because that data is gone now.

2\. You can add data to the newly opened file with the `write()` method of the stream object returned by the `open()` function. After the `with` block ends, Python automatically closes the file.

3\. **Appending will never harm the existing contents of the file.**

4\. Both the original line you wrote and the second line you appended are now in the file `test.log`. Also note that neither carriage returns nor line feeds are included. Since you didn’t write them explicitly to the file either time, the file doesn’t include them. You can write a carriage return with the `'\r'` character, and/or a line feed with the `'\n'` character. Since you didn’t do either, everything you wrote to the file ended up on one line.

### Character Encoding Again

In order to write to the file, Python needs to know how to convert your string into a sequence of bytes. The only way to be sure it’s performing the correct conversion is to specify the encoding parameter when you open the file for writing.

Binary Files
------------

Not all files contain text. Some of them contain pictures.

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
```

1\. Opening a file in binary mode is simple but subtle. The only difference from opening it in text mode is that the mode parameter contains a `b` character.

2\. The stream object you get from opening a file in binary mode has many of the same attributes, including `mode`, which reflects the mode parameter you passed into the `open()` function. And `name` attribute too.

3\. Here’s one difference, though: a binary stream object has no `encoding` attribute. That makes sense, right? You’re reading (or writing) bytes, not strings, so there’s no conversion for Python to do. What you get out of a binary file is exactly what you put into it, no conversion necessary.

```python
# continued from the previous example
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

You’re reading bytes, not strings. Since you opened the file in binary mode, the `read()` method *takes the number of bytes to read*, not the number of characters.

That means that there’s never an unexpected mismatch between the number you passed into the `read()` method and the position index you get out of the `tell()` method. The `read()` method reads bytes, and the `seek()` and `tell()` methods track the number of bytes read. For binary files, they’ll always agree.

Stream Objects From Non-File Sources
------------------------------------

Imagine you’re writing a library, and one of your library functions is going to read some data from a file. The function could simply take a filename as a string, go open the file for reading, read it, and close it before exiting. But you shouldn’t do that. Instead, your api should take *an arbitrary stream object.*

In the simplest case, a stream object is anything with a `read()` method which takes an optional size parameter and returns a string. When called with no size parameter, the `read()` method should read everything there is to read from the input source and return all the data as a single value. When called with a size parameter, it reads that much from the input source and returns that much data. When called again, it picks up where it left off and returns the next chunk of data.

The input source that’s being “read” could be anything: a web page, a string in memory, even the output of another program. As long as your functions take a stream object and simply call the object’s `read()` method, you can handle any input source that acts like a file, without specific code to handle each kind of input.

```python
a_string = 'PapayaWhip is the new black.'
import io
a_file = io.StringIO(a_string)
a_file.read()
'PapayaWhip is the new black.'
a_file.read()
''
a_file.seek(0)
0
a_file.read(10)
'PapayaWhip'
a_file.tell()
10
a_file.seek(18)
18
a_file.read()
'new black.'
```

1\. The `io` module defines the `StringIO` class that you can use to treat a string in memory as a file.

2\. To create a stream object out of a string, create an instance of the `io.StringIO()` class and pass it the string you want to use as your “file” data. Now you have a stream object, and you can do all sorts of stream-like things with it.

> `io.StringIO` lets you treat a string as a text file. There’s also a `io.BytesIO` class, which lets you treat a byte array as a binary file.

### Handling Compressed Files

The Python standard library contains modules that support reading and writing compressed files: `gzip`, `bzip2`, `zipfile`, `tarfile`

The `gzip` module lets you create a stream object for reading or writing a gzip-compressed file. The stream object it gives you supports the `read()` method (if you opened it for reading) or the `write()` method (if you opened it for writing). That means you can use the methods you’ve already learned for regular files to *directly read or write a gzip-compressed file*, without creating a temporary file to store the decompressed data.

It supports the with statement too, so you can let Python automatically close your gzip-compressed file when you’re done with it.

```python
import gzip
with gzip.open('out.log.gz', mode='wb') as z_file:
  z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))

exit()
```

1\. You should always open gzipped files in binary mode. (Note the `b` character in the `mode` argument.)

Standard Input, Output, and Error
---------------------------------

Standard output and standard error (commonly abbreviated stdout and stderr) are pipes that are built into every unix-like system, including Mac OS X and Linux. When you call the `print()` function, the thing you’re printing is sent to the `stdout` pipe. When your program crashes and prints out a traceback, it goes to the `stderr` pipe. By default, both of these pipes are just connected to the terminal window where you are working; when your program prints something, you see the output in your terminal window, and when a program crashes, you see the traceback in your terminal window too. In the graphical Python Shell, the `stdout` and `stderr` pipes default to your “Interactive Window”.

```python
for i in range(3):
  print('PapayaWhip')
PapayaWhip
PapayaWhip
PapayaWhip
import sys
for i in range(3):
  l = sys.stdout.write('is the')     
is theis theis the
for i in range(3):
  l = sys.stderr.write('new black')  
new blacknew blacknew black
```

1\. `stdout` is defined in the `sys` module, and it is a stream object. Calling its `write()` function will print out whatever string you give it, then return the length of the output. In fact, this is what the print function really does; it adds a carriage return to the end of the string you’re printing, and calls `sys.stdout.write`.

2\. In the simplest case, `sys.stdout` and `sys.stderr` send their output to the same place: the Python `ide` (if you’re in one), or the terminal (if you’re running Python from the command line). Like standard output, standard error does not add carriage returns for you. If you want carriage returns, you’ll need to write carriage return characters.

`sys.stdout` and `sys.stderr` are stream objects, but they are write-only. Attempting to call their `read()` method will always raise an `IOError`.

```python
import sys
sys.stdout.read()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IOError: not readable
```

### Redirecting Standard Output

`sys.stdout` and `sys.stderr` are stream objects, albeit ones that only support writing. But they’re not constants; they’re variables. That means you can assign them a new value — any other stream object — to redirect their output.

```python
import sys

class RedirectStdoutTo:
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

Let’s take the last part first.

```python
print('A')
with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
    print('B')
print('C')
```

That’s a complicated with statement. Let's rewrite it as something more recognizable.

```python
with open('out.log', mode='w', encoding='utf-8') as a_file:
  with RedirectStdoutTo(a_file):
    print('B')
```

As the rewrite shows, you actually have two `with` statements, one nested within the scope of the other. The “outer” `with` statement should be familiar by now: it opens a utf-8-encoded text file named `out.log` for writing and assigns the stream object to a variable named a_file. But that’s not the only thing odd here.

```python
  with RedirectStdoutTo(a_file):
```

Where’s the `as` clause? The `with` statement doesn’t actually require one. Just like you can call a function and ignore its return value, you can have a `with` statement that doesn’t assign the `with` context to a variable. In this case, you’re only interested in the side effects of the `RedirectStdoutTo` context.

What are those side effects? Take a look inside the `RedirectStdoutTo` class. This class is a custom context manager. Any class can be a context manager by defining two special methods: `__enter__()` and `__exit__()`.

```python
class RedirectStdoutTo:
  def __init__(self, out_new):
    self.out_new = out_new

  def __enter__(self):
    self.out_old = sys.stdout
    sys.stdout = self.out_new

  def __exit__(self, *args):
    sys.stdout = self.out_old
```

1\. The `__init__()` method is called immediately after an instance is created. It takes one parameter, the stream object that you want to use as standard output for the life of the context. This method just saves the stream object in an instance variable so other methods can use it later.

2\. The `__enter__()` method is a special class method; Python calls it when entering a context (i.e. at the beginning of the `with` statement). This method saves the current value of `sys.stdout` in `self.out_old`, then redirects standard output by assigning `self.out_new` to `sys.stdout`.

3\. The `__exit__()` method is another special class method; Python calls it when exiting the context (i.e. at the end of the `with` statement). This method restores standard output to its original value by assigning the saved `self.out_old` value to `sys.stdout`.

Putting it all together:

```python
print('A')
with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
  print('B')
print('C')
```

1\. This `with` statement takes *a comma-separated list of contexts*. The comma-separated list acts like a series of nested with blocks.

-	The first context listed is the “outer” block;
-	The last one listed is the “inner” block.
-	The first context opens a file;
-	The second context redirects `sys.stdout` to the stream object that was created in the first context.

2\. Because this `print()` function is executed with the context created by the `with` statement, it will not print to the screen; it will write to the file `out.log`.

3\. The `with` code block is over. Python has told each context manager to do whatever it is they do upon exiting a context. The context managers form a last-in-first-out stack. Upon exiting, the second context changed `sys.stdout` back to its original value, then the first context closed the file named `out.log`. Since standard output has been restored to its original value, calling the `print()` function will once again print to the screen.

Redirecting standard error works exactly the same way, using `sys.stderr` instead of `sys.stdout`.

Further Reading
---------------

-	[Reading and writing files](http://docs.python.org/py3k/tutorial/inputoutput.html#reading-and-writing-files) in the Python.org tutorial
-	[`io` module](http://docs.python.org/3.1/library/io.html)
-	[Stream objects](http://docs.python.org/3.1/library/stdtypes.html#file-objects)
-	[Context manager types](http://docs.python.org/3.1/library/stdtypes.html#context-manager-types)
-	[`sys.stdout` and `sys.stderr`](http://docs.python.org/3.1/library/sys.html#sys.stdout)
-	[`fuse` on Wikipedia](http://en.wikipedia.org/wiki/Filesystem_in_Userspace)
