How to use APIs with Python
===========================

Resources
---------

-	[Codecademy API course](https://www.codecademy.com/en/courses/python-intermediate-en-6zbLp)
-	[Getting started with Twitter, Oauth2 and Python](http://stackoverflow.com/questions/6399978/getting-started-with-twitter-oauth2-python)

The Requests
------------

### Anatomy of a Request

An HTTP request is made up of three parts:

1.	The **request line**, which tells the server what kind of request is being sent (GET, POST, etc.) and what resource it's looking for;
2.	The **header**, which sends the server additional information (such as which client is making the request)
3.	The **body**, which can be empty (as in a GET request) or contain data (if you're POSTing or PUTing information, that information is contained here).

The Response
------------

### Anatomy of a Response

The HTTP response structure mirrors that of the HTTP request. It contains:

1.	A response line (line 2), which includes the three-digit HTTP status code;

2.	A header line or lines (line 3), which include further information about the server and its response;

3.	The body (line 5 and line 6), which contains the text message of the response (for example, "404" would have "file not found" in its body).

In Real World
-------------

Get a json url with `urlopen` and `json`

```python
>>> link
'http://www.nhtsa.gov/webapi/api/SafetyRatings?format=json'
>>> r1 = urlopen(link)
>>> str_r1 = r1.read().decode('utf-8')
>>> str_r1
'{"Count":28,"Message":"Results returned successfully","Results":[{"ModelYear":2017,"VehicleId":0},{"ModelYear":2016,"VehicleId":0},{"ModelYear":2015,"VehicleId":0},{"ModelYear":2014,"VehicleId":0},{"ModelYear":2013,"VehicleId":0},{"ModelYear":2012,"VehicleId":0},{"ModelYear":2011,"VehicleId":0},{"ModelYear":2010,"VehicleId":0},{"ModelYear":2009,"VehicleId":0},{"ModelYear":2008,"VehicleId":0},{"ModelYear":2007,"VehicleId":0},{"ModelYear":2006,"VehicleId":0},{"ModelYear":2005,"VehicleId":0},{"ModelYear":2004,"VehicleId":0},{"ModelYear":2003,"VehicleId":0},{"ModelYear":2002,"VehicleId":0},{"ModelYear":2001,"VehicleId":0},{"ModelYear":2000,"VehicleId":0},{"ModelYear":1999,"VehicleId":0},{"ModelYear":1998,"VehicleId":0},{"ModelYear":1997,"VehicleId":0},{"ModelYear":1996,"VehicleId":0},{"ModelYear":1995,"VehicleId":0},{"ModelYear":1994,"VehicleId":0},{"ModelYear":1993,"VehicleId":0},{"ModelYear":1992,"VehicleId":0},{"ModelYear":1991,"VehicleId":0},{"ModelYear":1990,"VehicleId":0}]}'
>>> json.load(str_r1)
'''
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    json.load(str_r1)
  File "/usr/lib/python3.5/json/__init__.py", line 265, in load
    return loads(fp.read(),
AttributeError: 'str' object has no attribute 'read'
'''
>>> str_r1
'{"Count":28,"Message":"Results returned successfully","Results":[{"ModelYear":2017,"VehicleId":0},{"ModelYear":2016,"VehicleId":0},{"ModelYear":2015,"VehicleId":0},{"ModelYear":2014,"VehicleId":0},{"ModelYear":2013,"VehicleId":0},{"ModelYear":2012,"VehicleId":0},{"ModelYear":2011,"VehicleId":0},{"ModelYear":2010,"VehicleId":0},{"ModelYear":2009,"VehicleId":0},{"ModelYear":2008,"VehicleId":0},{"ModelYear":2007,"VehicleId":0},{"ModelYear":2006,"VehicleId":0},{"ModelYear":2005,"VehicleId":0},{"ModelYear":2004,"VehicleId":0},{"ModelYear":2003,"VehicleId":0},{"ModelYear":2002,"VehicleId":0},{"ModelYear":2001,"VehicleId":0},{"ModelYear":2000,"VehicleId":0},{"ModelYear":1999,"VehicleId":0},{"ModelYear":1998,"VehicleId":0},{"ModelYear":1997,"VehicleId":0},{"ModelYear":1996,"VehicleId":0},{"ModelYear":1995,"VehicleId":0},{"ModelYear":1994,"VehicleId":0},{"ModelYear":1993,"VehicleId":0},{"ModelYear":1992,"VehicleId":0},{"ModelYear":1991,"VehicleId":0},{"ModelYear":1990,"VehicleId":0}]}'
>>> json.loads(str_r1)
'''
{'Count': 28, 'Results': [{'VehicleId': 0, 'ModelYear': 2017}, {'VehicleId': 0, 'ModelYear': 2016}, {'VehicleId': 0, 'ModelYear': 2015}, {'VehicleId': 0, 'ModelYear': 2014}, {'VehicleId': 0, 'ModelYear': 2013}, {'VehicleId': 0, 'ModelYear': 2012}, {'VehicleId': 0, 'ModelYear': 2011}, {'VehicleId': 0, 'ModelYear': 2010}, {'VehicleId': 0, 'ModelYear': 2009}, {'VehicleId': 0, 'ModelYear': 2008}, {'VehicleId': 0, 'ModelYear': 2007}, {'VehicleId': 0, 'ModelYear': 2006}, {'VehicleId': 0, 'ModelYear': 2005}, {'VehicleId': 0, 'ModelYear': 2004}, {'VehicleId': 0, 'ModelYear': 2003}, {'VehicleId': 0, 'ModelYear': 2002}, {'VehicleId': 0, 'ModelYear': 2001}, {'VehicleId': 0, 'ModelYear': 2000}, {'VehicleId': 0, 'ModelYear': 1999}, {'VehicleId': 0, 'ModelYear': 1998}, {'VehicleId': 0, 'ModelYear': 1997}, {'VehicleId': 0, 'ModelYear': 1996}, {'VehicleId': 0, 'ModelYear': 1995}, {'VehicleId': 0, 'ModelYear': 1994}, {'VehicleId': 0, 'ModelYear': 1993}, {'VehicleId': 0, 'ModelYear': 1992}, {'VehicleId': 0, 'ModelYear': 1991}, {'VehicleId': 0, 'ModelYear': 1990}], 'Message': 'Results returned successfully'}
'''
```
