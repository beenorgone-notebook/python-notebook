[Python Quick References: Pickle & JSON](http://www.diveintopython3.net/serializing.html)
=========================================================================================

I. `pickle`

1.	Saving Data to a Pickle File
2.	Loading Data from a Pickle File
3.	Pickling Without a File
4.	Debugging Pickle Files

II. `json`

1.	Saving Data to a `json` File
2.	Mapping of Python Datatypes to `json`
3.	Serializing Datatypes Unsupported by `json`
4.	Loading Data from a `json` File

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

Loading Data from a Pickle File
-------------------------------

```python
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

entry
#{'published': True, 'tags': ('diveintopython', 'docbook', 'html'), 'internal_id': b'\xde\xd5\xb4\xf8', 'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1), 'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition', 'title': 'Dive into history, 2009 edition', 'comments_link': None}
```

Pickling Without a File
-----------------------

```python
b = pickle.dumps(entry)
type(b)
#<class 'bytes'>
entry3 = pickle.loads(b)
entry3 == entry
#True
```

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

import time
# add this to customserializer.py
def to_json(python_object):
    '''
    a function that will take an unsupported Python object and convert it to supported JSON datatype.
    '''
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(python_object)}
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')

import customserializer
with open('entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f, default=customserializer.to_json)

# To hook your custom conversion function into the `json.dump()` function, pass your function into the `json.dump()` function in the `default` parameter.

with open('entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f) # It works
```

Loading Data from a `json` File
-------------------------------

```python
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

# add this to customserializer.py
def from_json(json_object):
    '''
    a function that will take a custom-converted `json` object and convert it back to the original Python datatype.
    '''
    if '__class__' in json_object:
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])
    return json_object

import customserializer
with open('entry.json', 'r', encoding='utf-8') as f:
    entry = json.load(f, object_hook=customserializer.from_json)

# NOTE: To hook the `from_json()` function into the deserialization process, pass it as the `object_hook` parameter to the `json.load()` function.

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
