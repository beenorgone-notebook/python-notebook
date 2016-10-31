import os
import shutil
import tempfile
from contextlib import ExitStack, contextmanager


# Example 1: Temporarily changes the current working directory
@contextmanager
def chdir(dir):
    cwd = os.getcwd()
    try:
        os.chdir(dir)
        yield
    finally:
        os.chdir(cwd)

with chdir('/tmp'):
    print('before `with` statement end, cwd is {}'.format(os.getcwd()))

print('after `with` statement end, cwd is {}'.format(os.getcwd()))


# Example 2: Deletes temporary directories when the `with` statement
# exits using `ExitStack.callback()`
with ExitStack() as stack:
    tempdir = tempfile.mkdtemp()
    stack.callback(shutil.rmtree, tempdir)
    # Remind `stack` to remove tempdir folder when exits.
    # when the `with` statement completes, it calls all of its
    # callbacks, which includes removing the temporary directory.

# If we need to del three temporary directories,
# and log all successfully deleted directories.
with ExitStack() as stack:
    tempdirs = []
    for i in range(3):
        tempdir = tempfile.mkdtemp()
        stack.callback(shutil.rmtree, tempdir)
        tempdirs.append(tempdir)
    # Do sth with the tempdirs


# Example 3: you are opening a bunch of files:
# if all of the files open successfully,
# you want to do something with them,
# but if any of them fail to open, you want to make sure that
# the ones that did get open are guaranteed to get closed.
# Using `ExitStack.enter_context()`
files = []
with ExitStack() as stack:
    for filename in filenames:
        # Open the file and automatically add its context manager
        # to the `stack.enter_context()`
        # returns the passed in context manager, i.e. the file object.
        fp = stack.enter_context(open(filename))
        files.append(fp)
    # Capture the close method, but do not call it yet.
    close_all_files = stack.pop_all().close

# shorter version:
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    # Hold onto the close method, but don't call it yet.
    close_files = stack.pop_all().close
    # If opening any file fails, all previously opened files will be
    # closed automatically. If all files are opened successfully,
    # they will remain open even after the with statement ends.
    # close_files() can then be invoked explicitly to close them all.

'''Discussion
if one of the `open()` calls fail before the loop completes?
The `with` statement will exit as normal and
the `ExitStack` will exit all the context managers it knows about.
In other words, all the files that were successfully opened will get closed.
Thus, in an error condition, you will be left with no open files
and no leaked file descriptors, etc.

if the loop completes and all files got opened successfully?

First, `pop_all()` creates a new `ExitStack`,
and populates it from the original `ExitStack`,
removing all the context managers from the original `ExitStack`.
So, after `stack.pop_all()` completes, the original `ExitStack`,
i.e. the one used in the `with` statement, is now empty.
When the `with` statement exits, the original `ExitStack` contains
no context managers so none of the files are closed.

Second, `ExitStack` s have a `close()` method which unwinds all
the registered context managers and callbacks and invokes their exit functionality.
after you're finally done with all the files and
you want to clean everything up, call `close_all_files()`
'''
