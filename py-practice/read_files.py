'''
You are writing a file browser which displays files line by line.
The list of files is specified on the commands line (in sys.argv).
After displaying one line, the program waits for user input. The user
can:
• press Enter to display the next line
• press n + Enter to forget the rest of the current file and start with the next file
• or anything else + Enter to display the next line

The first part is already written:
it is a function which displays the lines and queries the user for input.

Your job is to write the second part:
the generator read_lines with the following interface,
during construction it is passed a list of files to read.
If yields line after line from the first file,
then from the second file, and so on.
When the last file is exhausted, it stops.

The user of the generator can also throw an exception into
the generator (SkipThisFile) which signals the generator to skip
the rest of the current file, and just yield a dummy value to be skipped.
'''


class SkipThisFile(Exception):
    "Tells the generator to jump to the next file in list."
    pass


def read_lines(*files):
    '''this is the generator to be written
    >>> list(read_lines('exercises.rst'))[:2]
    ['=============================', 'Advanced Python -- exercises']
    '''
    for file in files:
        for line in open(file):
            try:
                yield line.rstrip('\n')
            except SkipThisFile:
                print('dummy file')
                yield
                break


def display_files(*files):
    source = read_lines(*files)
    for line in source:
        print(line, end='\a')
        inp = input()
        if inp == 'n':
            print('NEXT')
            source.throw(SkipThisFile)  # return value is ignored

import os

path = '/home/beenorgone/Desktop'
files = [os.path.join(path, fn) for fn in next(os.walk(path))[2]]


print(files)
display_files(*files)
