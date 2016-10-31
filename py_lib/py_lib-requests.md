[Requests: HTTP for Humans](http://docs.python-requests.org)
============================================================

Contents
--------

[Quickstart](http://docs.python-requests.org/en/master/user/quickstart)

-	Make a Request
-	Passing Parameters In URLs
-	Response Content
-	Binary Response Content
-	JSON Response Content
-	Raw Response Content
-	Custom Headers
-	More complicated POST requests
-	POST a Multipart-Encoded File
-	Response Status Codes
-	Response Headers
-	Cookies
-	Redirection and History
-	Timeouts
-	Errors and Exceptions

[Advanced Usage](http://docs.python-requests.org/en/master/user/advanced/)

-	Session Objects
-	Request and Response Objects
-	Prepared Requests
-	SSL Cert Verification
-	CA Certificates
-	Body Content Workflow
-	Keep-Alive
-	Streaming Uploads
-	Chunk-Encoded Requests
-	POST Multiple Multipart-Encoded Files
-	Event Hooks
-	Custom Authentication
-	Streaming Requests
-	Proxies
-	Compliance
-	HTTP Verbs
-	Link Headers
-	Transport Adapters
-	Blocking Or Non-Blocking?
-	Header Ordering
-	Timeouts

Authentication

-	Basic Authentication
-	Digest Authentication
-	OAuth 1 Authentication
-	Other Authentication
-	New Forms of Authentication

[Recommended Packages and Extensions](http://docs.python-requests.org/en/master/community/recommended)

[Quickstart](http://docs.python-requests.org/en/master/user/quickstart)
-----------------------------------------------------------------------

### Make a Request

```python
import requests
r = requests.get('https://api.github.com/events')
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
```

### Passing Parameters In URLs

```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
#http://httpbin.org/get?key2=value2&key1=value1

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
#http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

### Response Content

```python
import requests
r = requests.get('https://api.github.com/events')
r.text
#u'[{"repository":{"open_issues":0,"url":"https://github.com/...

r.encoding
#'utf-8'
r.encoding = 'ISO-8859-1'
```

### Binary Response Content

You can also access the response body as bytes, for non-text requests:

```python
r.content
#b'[{"repository":{"open_issues":0,"url":"https://github.com/...
```

The `gzip` and `deflate` transfer-encodings are automatically decoded for you.

For example, to create an image from binary data returned by a request:

```python
from PIL import Image
from StringIO import StringIO

i = Image.open(StringIO(r.content))
```

### JSON Response Content

```python
r.json()
#[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
r.status_code
#200
```

In case the JSON decoding fails, `r.json` raises an exception. For example, if the response gets a `204` (No Content), or if the response contains invalid JSON, attempting `r.json` raises `ValueError: No JSON object could be decoded`.

### Raw Response Content

In the rare case that you'd like to get the raw socket response from the server, you can access `r.raw`. If you want to do this, make sure you set `stream=True` in your initial request. Once you do, you can do this:

```python
r = requests.get('https://api.github.com/events', stream=True)
r.raw
#<requests.packages.urllib3.response.HTTPResponse object at 0x101194810>
r.raw.read(10)
#'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
```

In general, however, you should use a pattern like this to save what is being streamed to a file:

```python
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
```

Using `Response.iter_content` will handle a lot of what you would otherwise have to handle when using `Response.raw` directly. When streaming a download, the above is the preferred and recommended way to retrieve the content.

### Custom Headers

```python
url = 'https://api.github.com'
h = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=h)
```

### More complicated POST requests

Typically, you want to send some form-encoded data -- much like an HTML form. To do this, simply pass a dictionary to the data argument. Your dictionary of data will automatically be form-encoded when the request is made:

```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
```

There are many times that you want to send data that is not form-encoded. If you pass in a `string` instead of a `dict`, that data will be posted directly. For example, the GitHub API v3 accepts JSON-Encoded POST/PATCH data:

```python
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))

# Instead of encoding the dict yourself,
# you can also pass it directly using the json parameter
# (added in version 2.4.2) and it will be encoded automatically:
r = requests.post(url, json=payload)
r = requests.post('https://httpbin.org/post', json={'my': 'json'})

import pprint
pprint.pprint(r.json())
{'args': {},
 'data': '{"my": "json"}',
 'files': {},
 'form': {},
 'headers': {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Content-Length': '14',
             'Content-Type': 'application/json',
             'Host': 'httpbin.org',
             'User-Agent': 'python-requests/2.10.0'},
 'json': {'my': 'json'},
 'origin': '14.162.197.127',
 'url': 'https://httpbin.org/post'}
```

### POST a Multipart-Encoded File

```python
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}

# You can set the filename, content_type and headers explicitly:
url = 'http://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files=files)
r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}

# If you want, you can send strings to be received as files:
url = 'http://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
r.text
'''
{
...
  "files": {
    "file": "some,data,to,send\\nanother,row,to,send\\n"
  },
...
'''
```

> WARNING:
>
> It is strongly recommended that you open files in binary mode. This is because Requests may attempt to provide the Content-Length header for you, and if it does this value will be set to the number of bytes in the file. Errors may occur if you open the file in text mode.

### Response Status Codes

```python
r = requests.get('http://httpbin.org/get')
r.status_code
#200
r.status_code == requests.codes.ok
#True

bad_r = requests.get('http://httpbin.org/status/404')
bad_r.status_code
404

bad_r.raise_for_status()
'''
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    bad_r.raise_for_status()
  File "/usr/lib/python3/dist-packages/requests/models.py", line 773, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: NOT FOUND
'''
r.raise_for_status()
#None
```

### Response Headers

```python
r.headers
{
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
}

r.headers['Content-Type']
#'application/json'
r.headers.get('content-type')
#'application/json'
```

### Cookies

```python
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']
#'example_cookie_value'

# To send your own cookies to the server, you can use the cookies parameter:
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text
#'{"cookies": {"cookies_are": "working"}}'
```

### Redirection and History

```python
r = requests.get('http://github.com')
r.url
#'https://github.com/'
# Github redirects all HTTP requests to HTTPS
r.status_code
#200
r.history
#(<Response [301]>,)

# If you're using GET, OPTIONS, POST, PUT, PATCH or DELETE, you can disable redirection handling with the allow_redirects parameter:
r = requests.get('http://github.com', allow_redirects=False)
r.status_code
#301
r.history
#[]

# If you're using HEAD, you can enable redirection as well:
r = requests.head('http://github.com', allow_redirects=True)
r.url
#'https://github.com/'
r.history
#[<Response [301]>]
```

### Timeouts

```python
# You can tell Requests to stop waiting for a response after a given number of seconds with the timeout parameter:
requests.get('http://github.com', timeout=0.001)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
'''
```

> NOTE:
>
> `timeout` is not a time limit on the entire response download; rather, an exception is raised if the server has not issued a response for `timeout` seconds (more precisely, if no bytes have been received on the underlying socket for `timeout` seconds).

### Errors and Exceptions

In the event of a network problem (e.g. DNS failure, refused connection, etc), Requests will raise a `ConnectionError` exception.

`Response.raise_for_status()` will raise an `HTTPError` if the HTTP request returned an unsuccessful status code.

If a request times out, a `Timeout` exception is raised.

If a request exceeds the configured number of maximum redirections, a `TooManyRedirects` exception is raised.

All exceptions that Requests explicitly raises inherit from `requests.exceptions.RequestException`.

[Advanced Usage](http://docs.python-requests.org/en/master/user/advanced/)
--------------------------------------------------------------------------

[Authentication](http://docs.python-requests.org/en/master/user/authentication)
-------------------------------------------------------------------------------

### Basic Authentication

```python
from requests.auth import HTTPBasicAuth
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
#<Response [200]>
# HTTP Basic Auth is so common that Requests provides a handy shorthand for using it:
requests.get('https://api.github.com/user', auth=('user', 'pass'))
#<Response [200]>
```

### `netrc` Authentication

If no authentication method is given with the `auth` argument, Requests will attempt to get the authentication credentials for the URL's hostname from the user's netrc file. The netrc file overrides raw HTTP authentication headers set with `headers=`.

If credentials for the hostname are found, the request is sent with HTTP Basic Auth.

### Digest Authentication

```python
from requests.auth import HTTPDigestAuth
url = 'http://httpbin.org/digest-auth/auth/user/pass'
requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
#<Response [200]>
```

### OAuth 1 Authentication

```python
import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                  'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
#<Response [200]>
```

### Other Authentication

> `requests` is designed to allow other forms of authentication to be easily and quickly plugged in. Members of the open-source community frequently write authentication handlers for more complicated or less commonly-used forms of authentication. Some of the best have been brought together under the [Requests organization](https://github.com/requests), including:

-	[Kerberos](https://github.com/requests/requests-kerberos)
-	[NTLM](https://github.com/requests/requests-ntlm)

If you want to use any of these forms of authentication, go straight to their GitHub page and follow the instructions.

### New Forms of Authentication

Requests makes it easy to add your own forms of authentication. To do so, subclass `AuthBase` and implement the `__call__()` method:

```python
import requests
class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        # Implement my authentication
        return r

url = 'http://httpbin.org/get'
requests.get(url, auth=MyAuth())
#<Response [200]>
```

When an authentication handler is attached to a request, it is called during request setup. The `__call__` method must therefore do whatever is required to make the authentication work. Some forms of authentication will additionally add hooks to provide further functionality.

Further examples can be found under the [Requests organization](https://github.com/requests) and in the `auth.py` file.

[Recommended Packages and Extensions](http://docs.python-requests.org/en/master/community/recommended)
------------------------------------------------------------------------------------------------------

### Certifi CA Bundle

[Certifi](http://certifi.io/en/latest) is a carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It has been extracted from the Requests project.

This MPL Licensed CA Bundle is extracted from the Mozilla Included CA Certificate List.

To reference the installed certificate authority (CA) bundle, you can use the built-in function:

```python
import certifi
import requests

certifi.where()
#'/usr/local/lib/python3.5/dist-packages/certifi/cacert.pem'

requests.get('https://bongdaplus.com', verify=certifi.where())
```

### CacheControl

[CacheControl](https://cachecontrol.readthedocs.io/en/latest) is an extension that adds a full HTTP cache to Requests. This makes your web requests substantially more efficient, and should be used whenever you're making a lot of web requests.

### Requests-Toolbelt

[Requests-Toolbelt](http://toolbelt.readthedocs.io/en/latest/index.html) is a collection of utilities that some users of Requests may desire, but do not belong in Requests proper. This library is actively maintained by members of the Requests core team, and reflects the functionality most requested by users within the community.

### Requests-OAuthlib

[requests-oauthlib](https://requests-oauthlib.readthedocs.io/en/latest/) makes it possible to do the OAuth dance from Requests automatically. This is useful for the large number of websites that use OAuth to provide authentication. It also provides a lot of tweaks that handle ways that specific OAuth providers differ from the standard specifications.

### Betamax

[Betamax](https://github.com/sigmavirus24/betamax) records your HTTP interactions so the NSA does not have to. A VCR imitation designed only for Python-Requests.
