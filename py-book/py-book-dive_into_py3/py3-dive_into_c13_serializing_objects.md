Dive into Python 3: Serializing Objects
=======================================

**Contents:**

1.	Diving In
2.	Saving Data to a Pickle File
3.	Loading Data from a Pickle File
4.	Pickling Without a File
5.	Bytes and Strings Rear Their Ugly Heads Again
6.	Debugging Pickle Files
7.	Serializing Python Objects to be Read by Other Languages
8.	Saving Data to a `json` File
9.	Mapping of Python Datatypes to `json`
10.	Serializing Datatypes Unsupported by `json`
11.	Loading Data from a `json` File
12.	Further Reading

Diving In
---------

To store data for next use/play use `pickle` module. What can the `pickle` module store?

-	All the native datatypes that Python supports: booleans, integers, floating point numbers, complex numbers, strings, bytes objects, byte arrays, and `None`.
-	Lists, tuples, dictionaries, and sets containing any combination of native datatypes.
-	Lists, tuples, dictionaries, and sets containing any combination of lists, tuples, dictionaries, and sets containing any combination of native datatypes (and so on, to [the maximum nesting level that Python supports](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit)).
-	Functions, classes, and instances of classes (with caveats).

Saving Data to a Pickle File
----------------------------

```python
# in shell #1
entry = {}
entry['title'] = 'Dive into history, 2009 edition'
entry['article_link'] = #'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True
import time
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')
entry['published_date']
#time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1)

import pickle
with open('entry.pickle', 'wb') as f:
    pickle.dump(entry, f)
```

1\. Use the `open()` function to open a file. Set the file mode to `'wb'` to open the file for writing in binary mode. Wrap it in a `with` statement to ensure the file is closed automatically when you’re done with it.

2\. The `dump()` function in the `pickle` module takes a serializable Python data structure, serializes it into a binary, Python-specific format using the latest version of the pickle protocol, and saves it to an open file.

3\. The pickle protocol is Python-specific; there is no guarantee of cross-language compatibility. You probably couldn’t take the `entry.pickle` file you just created and do anything useful with it in Perl, PHP, Java, or any other language.

4\. Not every Python data structure can be serialized by the pickle module. The pickle protocol has changed several times as new data types have been added to the Python language, but there are still limitations.

5\. Unless you specify otherwise, the functions in the pickle module will use the latest version of the pickle protocol. This ensures that you have maximum flexibility in the types of data you can serialize, but it also means that the resulting file will not be readable by older versions of Python that do not support the latest version of the pickle protocol.

6\. The latest version of the pickle protocol is a binary format. Be sure to open your pickle files in binary mode, or the data will get corrupted during writing.

Loading Data from a Pickle File
-------------------------------

```python
# in shell 2
entry
#NameError: name 'entry' is not defined
import pickle
with open('entry.pickle', 'rb') as f:
	entry = pickle.load(f)

entry
#{'published': True, 'tags': ('diveintopython', 'docbook', 'html'), 'internal_id': b'\xde\xd5\xb4\xf8', 'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1), 'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition', 'title': 'Dive into history, 2009 edition', 'comments_link': None}

```

The `pickle.load()` function takes a stream object, reads the serialized data from the stream, creates a new Python object, recreates the serialized data in the new Python object, and returns the new Python object.

```python
# in shell #1
with open('entry.pickle', 'rb') as f:
    entry2 = pickle.load(f)

entry2 == entry
#True
entry2 is entry
#False
entry2['tags']
#('diveintopython', 'docbook', 'html')
entry2['internal_id']
#b'\xde\xd5\xb4\xf8'
```

Pickling Without a File
-----------------------

You can also serialize to a `bytes` object in memory.

```python
b = pickle.dumps(entry)
type(b)
#<class 'bytes'>
entry3 = pickle.loads(b)
entry3 == entry
#True
```

1\. The `pickle.dumps()` function (note the `s` at the end of the function name) performs the same serialization as the `pickle.dump()` function. Instead of taking a stream object and writing the serialized data to a file on disk, it simply returns the serialized data.

2\. The `pickle.loads()` function (again, note the `s` at the end of the function name) performs the same deserialization as the `pickle.load()` function. Instead of taking a stream object and reading the serialized data from a file, it takes a bytes object containing serialized data, such as the one returned by the `pickle.dumps()` function.

Debugging Pickle Files
----------------------

To determine which protocol version was used to store a pickle file use these code:

```python
import pickletools

def protocol_version(file_object):
    maxproto = -1
    for opcode, arg, pos in pickletools.genops(file_object):
        maxproto = max(maxproto, opcode.proto)
    return maxproto

import pickleversion
with open('entry.pickle', 'rb') as f:
    v = pickleversion.protocol_version(f)

v
#3
```

Serializing Python Objects to be Read by Other Languages
--------------------------------------------------------

If cross-language compatibility is one of your requirements, you need to look at other serialization formats. One such format is `json`. “`json`” stands for “JavaScript Object Notation,” but don’t let the name fool you — `json` is explicitly designed to be usable across multiple programming languages.

1\. the json data format is text-based, not binary.

2\. as with any text-based format, there is the issue of whitespace. `json` allows arbitrary amounts of whitespace (spaces, tabs, carriage returns, and line feeds) between values.

3\. `json` must be stored in a Unicode encoding (`UTF-32`, `UTF-16`, or the default, `utf-8`\)

Saving Data to a `json` File
----------------------------

```python
basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'Dive into history, 2009 edition'
basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
basic_entry['published'] = True
basic_entry['comments_link'] = None
import json
with open('basic.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f)

with open('basic-pretty.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f, indent=2)
```

If you pass an indent parameter to the `json.dump()` function, it will make the resulting `json` file more readable, at the expense of larger file size. The `indent` parameter is an integer. `0` means “put each value on its own line.” A number greater than 0 means “put each value on its own line, and use this number of spaces to indent nested data structures.”

```
$ cat basic.json
{"id": 256, "title": "Dive into history, 2009 edition", "published": true, "tags": ["diveintopython", "docbook", "html"], "comments_link": null}
$ cat basic-pretty.json
{
  "id": 256,
  "title": "Dive into history, 2009 edition",
  "published": true,
  "tags": [
    "diveintopython",
    "docbook",
    "html"
  ],
  "comments_link": null
}
```

Mapping of Python Datatypes to `json`
-------------------------------------

Since `json` is not Python-specific, there are some mismatches in its coverage of Python datatypes.

| Notes                               | JSON       | Python 3 |
|-------------------------------------|------------|----------|
| object                              | dictionary |          |
| array                               | list       |          |
| string                              | string     |          |
| integer                             | integer    |          |
| real number                         | float      |          |
|                                     | true       | `True`   |
|                                     | false      | `False`  |
|                                     | null       | `None`   |
| All json values are case-sensitive. |            |          |

`json` has an array type, which the `json` module maps to a Python list, but it does not have a separate type for “frozen arrays” (tuples). And while `json` supports strings quite nicely, it has no support for `bytes` objects or byte arrays.

Serializing Datatypes Unsupported by `json`
-------------------------------------------

The `json` module provides extensibility hooks for encoding and decoding unknown datatypes (not defined in `json`).

```python
entry
'''
{'comments_link': None,
 'internal_id': b'\xDE\xD5\xB4\xF8',
 'title': 'Dive into history, 2009 edition',
 'tags': ('diveintopython', 'docbook', 'html'),
 'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
 'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1),
 'published': True}
'''
import json
with open('entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f)

#TypeError: b'\xDE\xD5\xB4\xF8' is not JSON serializable
```

The `json.dump()` function tried to serialize the bytes object `b'\xDE\xD5\xB4\xF8'`, but it failed, because `json` has no support for bytes objects. However, if storing bytes is important to you, you can define your own “mini-serialization format.”

```python
def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')
```

1\. To define your own “mini-serialization format” for a datatype that `json` doesn’t support natively, just define a function that takes a Python object as a parameter. This Python object will be the actual object that the `json.dump()` function is unable to serialize by itself — in this case, the `bytes` object `b'\xDE\xD5\xB4\xF8'`.

2\. Your custom serialization function should check the type of the Python object that the `json.dump()` function passed to it. This is not strictly necessary if your function only serializes one datatype, but it makes it crystal clear what case your function is covering, and it makes it easier to extend if you need to add serializations for more datatypes later.

3\. In this case, I’ve chosen to convert a `bytes` object into a dictionary. The `__class__` key will hold the original datatype (as a string, 'bytes'), and the `__value__` key will hold the actual value. Of course this can’t be a `bytes` object; the entire point is to convert it into something that can be serialized in `json`! A bytes object is just a sequence of integers; each integer is somewhere in the range 0–255. We can use the list() function to convert the bytes object into a list of integers. So `b'\xDE\xD5\xB4\xF8'` becomes `[222, 213, 180, 248]`.

4\. In particular, this custom serialization function *returns a Python dictionary*, not a string. You’re not doing the entire serializing-to-json yourself; you’re only doing the converting-to-a-supported-datatype part. The `json.dump()` function will do the rest.

```python
# in shell #1
import customserializer
with open('entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f, default=customserializer.to_json)
#TypeError: time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1) is not JSON serializable
```

1\. The `customserializer` module is where you just defined the `to_json()` function in the previous example.

2\. To hook your custom conversion function into the `json.dump()` function, pass your function into the `json.dump()` function in the `default` parameter.

```python
import time

def to_json(python_object):
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(python_object)}
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')
```

1\. Adding to our existing `customserializer.to_json()` function, we need to check whether the Python object (that the `json.dump()` function is having trouble with) is a `time.struct_time`.

2\. The `time.asctime()` function will convert that nasty-looking `time.struct_time` into the string `'Fri Mar 27 22:20:42 2009'`

With these two custom conversions, the entire entry data structure should serialize to `json` without any further problems.

Loading Data from a `json` File
-------------------------------

Like the `pickle` module, the `json` module has a `load()` function which takes a stream object, reads `json`-encoded data from it, and creates a new Python object that mirrors the `json` data structure.

```Python
# in shell #2
del entry
import json
with open('entry.json', 'r', encoding='utf-8') as f:
    entry = json.load(f)

entry
'''
{'comments_link': None,
 'internal_id': {'__class__': 'bytes', '__value__': [222, 213, 180, 248]},
 'title': 'Dive into history, 2009 edition',
 'tags': ['diveintopython', 'docbook', 'html'],
 'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
 'published_date': {'__class__': 'time.asctime', '__value__': 'Fri Mar 27 22:20:42 2009'},
 'published': True}
'''
```

1\. The `json.load()` function successfully read the `entry.json` file you created in Python Shell `#1` and created a new Python object that contained the data.

2\. The two values `'internal_id'` and `'published_date'` were recreated as dictionaries — specifically, the dictionaries with `json`-compatible values that you created in the `to_json()` conversion function.

3\. `json.load()` doesn’t know anything about any conversion function you may have passed to `json.dump()`. What you need is the opposite of the `to_json()` function — a function that will take a custom-converted `json` object and convert it back to the original Python datatype.

```Python
# add this to customserializer.py
def from_json(json_object):
    if '__class__' in json_object:
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])
    return json_object

# in shell #2
import customserializer
with open('entry.json', 'r', encoding='utf-8') as f:
    entry = json.load(f, object_hook=customserializer.from_json)

entry
'''
{'comments_link': None,
 'internal_id': b'\xDE\xD5\xB4\xF8',
 'title': 'Dive into history, 2009 edition',
 'tags': ['diveintopython', 'docbook', 'html'],
 'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
 'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1),
 'published': True}
'''
```

To hook the `from_json()` function into the deserialization process, pass it as the `object_hook` parameter to the `json.load()` function.

```python
# in shell #1
import customserializer
with open('entry.json', 'r', encoding='utf-8') as f:
    entry2 = json.load(f, object_hook=customserializer.from_json)

entry2 == entry
#False
entry['tags']
#('diveintopython', 'docbook', 'html')
entry2['tags']
#['diveintopython', 'docbook', 'html']
```

1\. Even after hooking the `to_json()` function into the serialization, and hooking the `from_json()` function into the deserialization, we still haven’t recreated a perfect replica of the original data structure. Why not?

2\. In the original entry data structure, the value of the 'tags' key was a tuple of three strings.

3\. But in the round-tripped `entry2` data structure, the value of the 'tags' key is a *list* of three strings. `json` doesn’t distinguish between tuples and lists; it only has a single list-like datatype, the array, and the `json` module silently converts both tuples and lists into `json` arrays during serialization. For most uses, you can ignore the difference between tuples and lists, but it’s something to keep in mind as you work with the `json` module.

Further Reading
---------------

On pickling with the `pickle` module:

-	[`pickle` module](http://docs.python.org/3.1/library/pickle.html)
-	[`pickle` and `cPickle` — Python object serialization](http://www.doughellmann.com/PyMOTW/pickle)
-	[Using `pickle`](http://wiki.python.org/moin/UsingPickle)
-	[Python persistence management](http://www.ibm.com/developerworks/library/l-pypers.html)

On `JSON` and the `json` module:

-	[`json` — JavaScript Object Notation Serializer](http://www.doughellmann.com/PyMOTW/json)
-	[JSON encoding and ecoding with custom objects in Python](http://blog.quaternio.net/2009/07/16/json-encoding-and-decoding-with-custom-objects-in-python)

On pickle extensibility:

-	[Pickling class instances](http://docs.python.org/3.1/library/pickle.html#pickling-class-instances)
-	[Persistence of external objects](http://docs.python.org/3.1/library/pickle.html#persistence-of-external-objects)
-	[Handling stateful objects](http://docs.python.org/3.1/library/pickle.html#handling-stateful-objects)
