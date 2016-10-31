import bz2
import fnmatch
import functools
import gzip
import os
import re
import sys


# Inside a function, the yield statement can also be used as an
# expression that appears on the right side of an assignment operator.


def receiver():
    print("Ready to receive")
    while True:
        n = (yield)
        print("Got {}".format(n))


# Example use:
r1 = receiver()

next(r1)  # Ready to receive
next(r1)  # Got None

r1.send(1)  # Got 1
r1.send(2)  # Got 2
r1.send('Hello')  # Got Hello


# The requirement of first calling next() on a coroutine is easily
# overlooked and a common source of errors.Therefore, it is
# recommended that coroutines be wrapped with a decorator that
# automatically takes care of this step.


def autostart_coroutine(func):
    @functools.wraps(func)
    def start(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.__next__()  # or `next(gen)`
        return gen
    return start


@autostart_coroutine
def receiver():
    print("Ready to receive")
    while True:
        n = (yield)
        print("Got {}".format(n))


# Example use:
r2 = receiver()
r2.send("Hello World")  # Note: initial `next(r)` needed

# A coroutine will typically run indefinitely unless it is explicitly
# shut down or it exits on its own.To close the stream of input
# values, use the `close()` method

r1.close()
r2.close()
# r1.send(1) will raise StopIteration


@autostart_coroutine
def receiver():
    print("Ready to receive")
    try:
        while True:
            n = (yield)
            print("Got {}".format(n))
    except GeneratorExit:
        print("Receiver done")

# Exceptions can be raised inside a coroutine using the
# `throw(exctype [, value [,tb]])` method where exctype is an
# exception type, value is the exception value, and tb is a traceback
# object. For example: r.throw(RuntimeError, "You're hosed!")

# A coroutine may simultaneously receive and emit return values using
# `yield` if values are supplied in the `yield` expression.


def line_splitter(delimiter=None):
    print("Ready to split")
    result = None
    while True:
        line = (yield result)
        result = line.split(delimiter)

s = line_splitter(',')
print(next(s))  # None
print(s.send('A, B, C'))  # ['A', 'B', 'C']
print(s.send('100, 200, 300'))  # ['100', '200', '300']


# Using Generators and Coroutines

# Generator functions are useful if you want to set up a processing
# pipeline, similar in nature to using a pipe in the UNIX shell.

# Coroutines can be used to write programs based on data-flow
# processing. Programs organized in this way look like inverted
# pipelines. Instead of pulling values through a sequence of
# generator functions using a for loop, you send values into a
# collection of linked coroutines.


@autostart_coroutine
def find_files(target):
    while True:
        topdir, pattern = (yield)
        for path, dirname, filelist in os.walk(topdir):
            for name in filelist:
                if fnmatch.fnmatch(name, pattern):
                    target.send(os.path.join(path, name))


@autostart_coroutine
def opener(target):
    while True:
        name = (yield)
        if name.endswith('.gz'):
            f = gzip.open(name)
        elif name.endswith('.bz2'):
            f = bz2.BZ2File(name)
        else:
            f = open(name)
        target.send(f)


@autostart_coroutine
def cat(target):
    while True:
        f = (yield)
        for line in f:
            target.send(line)


@autostart_coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


@autostart_coroutine
def printer():
    while True:
        line = (yield)
        sys.stdout.write(line)


# Here is how you would link these coroutines to create a dataflow
# processing pipeline:
finder = find_files(opener(cat(grep('py', printer()))))

finder.send(
    ('/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/py-advanced', '*.md'))


'''
A critical aspect of this example is that the coroutine pipeline
remains active indefinitely or until close() is explicitly called
on it. Because of this, a program can continue to feed data into a
coroutine for as long as necessary—for example, the two repeated
calls to send() shown in the example.

Coroutines can be used to implement a form of concurrency.
For example, a centralized task manager or event loop can schedule
and send data into a large collection of hundreds or even thousands
of coroutines that carry out various processing tasks. The fact
that input data is “sent” to a coroutine also means that coroutines
can often be easily mixed with programs that use message queues and
message passing to communicate between program components.
'''


# Generator version:
def find_files(topdir, pattern):
    for path, dirname, filelist in os.walk(topdir):
        for name in filelist:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path.name)


def opener(filenames):
    for name in filenames:
        if name.endswith(".gz"):
            f = gzip.open(name)
        elif name.endswith(".bz2"):
            f = bz2.BZ2File(name)
        else:
            f = open(name)
        yield f


def cat(filelist):
    for f in filelist:
        for line in f:
            yield line


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


'''
Apply several regex to the text in a set of HTML files.
The purpose is to output each file’s URLs and level 1 and level 2 headings.
We’ll start by looking at the regular expressions, then
the creation of the coroutine “matchers”, and then
we will look at the coroutines and how they are used.
'''


@autostart_coroutine
def regex_matcher(receiver, regex):
    '''A coroutine that takes a receiver function
    (itself a coroutine) and a regex to match.
    Whenever the matcher matches it sends the match to the receiver.'''
    while True:
        text = (yield)
        for match in regex.finditer(text):
            receiver.send(match)


@autostart_coroutine
def reporter():
    '''A coroutine which be used to output results.
    When suspended, it will wait until a match is sent to it, then
    it prints the match's details, and then it waits again,
    in an endless loop--stopping only if `close()` is called on it.'''
    ignore = frozenset({"style.css", "favicon.png", "index.html"})
    while True:
        match = (yield)
        if match is not None:
            groups = match.groupdict()
            if 'url' in groups and groups['url'] not in ignore:
                print('URL: {}'.format(groups['url']))
            elif 'h1' in groups:
                print('H1: {}'.format(groups['h1']))
            elif 'h2' in groups:
                print('H2: {}'.format(groups['h2']))


URL_RE = re.compile(r'''href=(?P<quote>['"])(?P<url>[^\1]+?)'''
                    r'''(?P=quote)''', re.IGNORECASE)
flags = re.MULTILINE | re.IGNORECASE | re.DOTALL
H1_RE = re.compile(r"<h1>(?P<h1>.+?)</h1>", flags)
H2_RE = re.compile(r"<h2>(?P<h2>.+?)</h2>", flags)

receiver = reporter()
matchers = (regex_matcher(receiver, URL_RE),
            regex_matcher(receiver, H1_RE),
            regex_matcher(receiver, H2_RE))

try:
    for file in sys.argv[1:]:
        print(file)
        html = open(file, encoding="utf-8").read()
        for matcher in matchers:
            matcher.send(html)
finally:
    for matcher in matchers:
        matcher.close()
    receiver.close()

'''The program reads the filenames listed on the command line,
and for each one prints the filename and then reads the file’s
entire text into the html variable using the UTF-8 encoding. Then
the program iterates over all the matchers (three in this case),
and sends the text to each of them. Each matcher then proceeds
independently, sending each match it makes to the reporter
coroutine. At the end we call close() on each matcher and
on the reporter--this terminates them, since otherwise they would
continue (suspended) waiting for text (or matches in the case of
the reporter) since they contain infinite loops.'''
