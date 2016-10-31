Python Quick References: Dictionaries
=====================================

**Contents:**

1.	Creating A Dictionary
2.	Modifying A Dictionary
3.	Dictionaries In A Boolean Context

Creating A Dictionary
---------------------

A dictionary is an unordered set of key-value pairs. When you add a key to a dictionary, you must also add a value for that key. (You can always change the value later.) Python dictionaries are optimized for retrieving the value when you know the key, but not the other way around.

```python
a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
a_dict
#{'database': 'mysql', 'server': 'db.diveintopython3.org'}
a_dict['server']
#'db.diveintopython3.org'
a_dict['database']
#'mysql'
a_dict['db.diveintopython3.org']
#Traceback (most recent call last):
#  File "<pyshell#42>", line 1, in <module>
#    a_dict['db.diveintopython3.org']
#KeyError: 'db.diveintopython3.org'

#Use Dictionary Comprehensions
metadata_dict = {f:os.stat(f) for f in glob.glob('*.md')}
```

Modifying A Dictionary
----------------------

```python
a_dict
#{'server': 'db.diveintopython3.org', 'database': 'mysql'}
a_dict['database'] = 'blog'
a_dict
#{'server': 'db.diveintopython3.org', 'database': 'blog'}
a_dict['user'] = 'mark'  
a_dict
#{'server': 'db.diveintopython3.org', 'user': 'mark', 'database': 'blog'}
a_dict['user'] = 'dora'
a_dict
#{'server': 'db.diveintopython3.org', 'user': 'dora', 'database': 'blog'}
```

Dictionaries In A Boolean Context
---------------------------------

1.	In a boolean context, an empty dictionary is false.
2.	Any dictionary with at least one key-value pair is true.
