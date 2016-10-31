[Dive into Python 3: HTTP Web Services](http://www.diveintopython3.net/http-web-services.html)
==============================================================================================

**Content**:

1.	Diving In
2.	Features of HTTP

	1.	Caching
	2.	Last-Modified Checking
	3.	ETag Checking
	4.	Compression
	5.	Redirects

3.	How Not To Fetch Data Over HTTP

4.	What's On The Wire?

5.	Introducing httplib2

	1.	A Short Digression To Explain Why httplib2 Returns Bytes Instead of Strings
	2.	How httplib2 Handles Caching
	3.	How httplib2 Handles Last-Modified and ETag Headers
	4.	How http2lib Handles Compression
	5.	How httplib2 Handles Redirects

6.	Beyond HTTP GET

7.	Beyond HTTP POST

8.	Further Reading

Diving In
---------

Exchanging data with remote servers using nothing but the operations of `HTTP`.

-	If you want to get data from the server, use `http GET`.
-	If you want to send new data to the server, use `http POST`.
-	Some more advanced `http` web service apis also allow creating, modifying, and deleting data, using `http PUT` and `http DELETE`.

The "verbs" built into the `http` protocol (`GET`, `POST`, `PUT`, and `DELETE`) map directly to application-level operations for retrieving, creating, modifying, and deleting data.

The main advantage of this approach is simplicity, and its simplicity has proven popular. Data -- usually `xml` or `json` -- can be built and stored statically, or generated dynamically by a server-side script, and all major programming languages (including Python, of course!) include an `http` library for downloading it. Debugging is also easier; because each resource in an `http` web service has a unique address (in the form of a `url`), you can load it in your web browser and immediately see the raw data.

Examples of `http` web services:

-	Google Data apis allow you to interact with a wide variety of Google services, including Blogger and YouTube.
-	Flickr Services allow you to upload and download photos from Flickr.
-	Twitter api allows you to publish status updates on Twitter.

Python 3 comes with two different libraries for interacting with `http` web services:

-	`http.client` is a low-level library that implements rfc 2616, the http protocol.
-	`urllib.request` is an abstraction layer built on top of `http.client`. It provides a standard api for accessing both `http` and `ftp` servers, automatically follows `http` redirects, and handles some common forms of `http` authentication.

You should use `httplib2`, an open source third-party library that implements http more fully than `http.client` but provides a better abstraction than `urllib.request`.

Features of HTTP
----------------

There are five important features which all `http` clients should support.

### Caching

Here's a concrete example of how caching works. You visit `diveintomark.org` in your browser. That page includes a background image, `wearehugh.com/m.jpg`. When your browser downloads that image, the server includes the following `http` headers:

```
HTTP/1.1 200 OK
Date: Sun, 31 May 2009 17:14:04 GMT
Server: Apache
Last-Modified: Fri, 22 Aug 2008 04:28:16 GMT
ETag: "3075-ddc8d800"
Accept-Ranges: bytes
Content-Length: 12405
Cache-Control: max-age=31536000, public
Expires: Mon, 31 May 2010 17:14:04 GMT
Connection: close
Content-Type: image/jpeg
```

The `Cache-Control` and `Expires` headers tell your browser (and any caching proxies between you and the server) that this image can be cached for up to a year. A year! And if, in the next year, you visit another page which also includes a link to this image, your browser will load the image from its cache *without generating any network activity whatsoever*.

But wait, it gets better. Let's say your browser purges the image from your local cache for some reason. Maybe it ran out of disk space; maybe you manually cleared the cache. Whatever. But the `http` headers said that this data could be cached by public caching proxies. (Technically, the important thing is what the headers *don't* say; the `Cache-Control` header doesn't have the private keyword, so this data is cacheable by default.) Caching proxies are designed to have tons of storage space, probably far more than your local browser has allocated.

> If your company or `isp` maintain a caching proxy, the proxy may still have the image cached. When you visit `diveintomark.org` again, your browser will look in its local cache for the image, but it won't find it, so it will make a network request to try to download it from the remote server. But if the caching proxy still has a copy of the image, it will intercept that request and serve the image from *its* cache. That means that your request will never reach the remote server; in fact, it will never leave your company's network. That makes for a faster download (fewer network hops) and saves your company money (less data being downloaded from the outside world).

Python's `http` libraries do not support caching, but `httplib2` does.

### Last-Modified Checking

Some data never changes, while other data changes all the time. In between, there is a vast field of data that might have changed, but hasn't. I don't want to tell clients to cache my feed for weeks at a time, because then when I do actually post something, people may not read it for weeks (because they're respecting my cache headers which said "don't bother checking this feed for weeks"). On the other hand, I don't want clients downloading my entire feed once an hour if it hasn't changed!

`http` has a solution to this, too. When you request data for the first time, the server can send back a `Last-Modified` header. This is exactly what it sounds like: the date that the data was changed. That background image referenced from `diveintomark.org` included a `Last-Modified` header.

```
HTTP/1.1 200 OK
Date: Sun, 31 May 2009 17:14:04 GMT
Server: Apache
Last-Modified: Fri, 22 Aug 2008 04:28:16 GMT
ETag: "3075-ddc8d800"
Accept-Ranges: bytes
Content-Length: 12405
Cache-Control: max-age=31536000, public
Expires: Mon, 31 May 2010 17:14:04 GMT
Connection: close
Content-Type: image/jpeg
```

When you request the same data a second (or third or fourth) time, you can send an `If-Modified-Since` header with your request, with the date you got back from the server last time. If the data has changed since then, then the server gives you the new data with a `200` status code. But if the data hasn't changed since then, the server sends back a special `http 304` status code, which means "this data hasn't changed since the last time you asked for it." You can test this on the command line, using `curl`:

```
$ curl -I -H "If-Modified-Since: Fri, 22 Aug 2008 04:28:16 GMT" http://wearehugh.com/m.jpg
HTTP/1.1 304 Not Modified
Date: Sun, 31 May 2009 18:04:39 GMT
Server: Apache
Connection: close
ETag: "3075-ddc8d800"
Expires: Mon, 31 May 2010 18:04:39 GMT
Cache-Control: max-age=31536000, public
```

> Why is this an improvement? Because when the server sends a `304`, *it doesn't re-send the data*. All you get is the status code. Even after your cached copy has expired, last-modified checking ensures that you won't download the same data twice if it hasn't changed. (As an extra bonus, this `304` response also includes caching headers. Proxies will keep a copy of data even after it officially "expires," in the hopes that the data hasn't really changed and the next request responds with a `304` status code and updated cache information.)

Python's `http` libraries do not support last-modified date checking, but `httplib2` does.

### ETag Checking

ETags are an alternate way to accomplish the same thing as the last-modified checking. With Etags, the server sends a hash code in an `ETag` header along with the data you requested. (Exactly how this hash is determined is entirely up to the server. The only requirement is that it changes when the data changes.) That background image referenced from diveintomark.org had an `ETag` header.

```
HTTP/1.1 200 OK
Date: Sun, 31 May 2009 17:14:04 GMT
Server: Apache
Last-Modified: Fri, 22 Aug 2008 04:28:16 GMT
ETag: "3075-ddc8d800"
Accept-Ranges: bytes
Content-Length: 12405
Cache-Control: max-age=31536000, public
Expires: Mon, 31 May 2010 17:14:04 GMT
Connection: close
Content-Type: image/jpeg
```

The second time you request the same data, you include the ETag hash in an `If-None-Match` header of your request. If the data hasn't changed, the server will send you back a `304` status code. As with the last-modified date checking, the server sends back *only* the `304` status code; it doesn't send you the same data a second time. By including the ETag hash in your second request, you're telling the server that there's no need to re-send the same data if it still matches this hash, since you still have the data from the last time.

```
curl -I -H "If-None-Match: \"3075-ddc8d800\"" http://wearehugh.com/m.jpg  ①
HTTP/1.1 304 Not Modified
Date: Sun, 31 May 2009 18:04:39 GMT
Server: Apache
Connection: close
ETag: "3075-ddc8d800"
Expires: Mon, 31 May 2010 18:04:39 GMT
Cache-Control: max-age=31536000, public
```

### Compression

`http` supports several compression algorithms. The two most common types are `gzip` and `deflate`. When you request a resource over `http`, you can ask the server to send it in compressed format. You include an `Accept-encoding` header in your request that lists which compression algorithms you support. If the server supports any of the same algorithms, it will send you back compressed data (with a `Content-encoding` header that tells you which algorithm it used). Then it's up to you to decompress the data.

Python's `http` libraries do not support compression, but `httplib2` does.

> Important tip for server-side developers: make sure that the compressed version of a resource has a different Etag than the uncompressed version. Otherwise, caching proxies will get confused and may serve the compressed version to clients that can't handle it. Read the discussion of Apache bug 39727 for more details on this subtle issue.

### Redirects

Every time you request any kind of resource from an `http` server, the server includes a status code in its response.

-	Status code `200` means "everything's normal, here's the page you asked for".
-	Status code `404` means "page not found". (You've probably seen `404` errors while browsing the web.)
-	Status codes in the `300`'s indicate some form of redirection.

`http` has several different ways of signifying that a resource has moved. The two most common techiques are status codes `302` and `301`.

-	Status code `302` is a *temporary redirect*; it means "oops, that got moved over here temporarily" (and then gives the temporary address in a `Location` header).
-	Status code `301` is a *permanent redirect*; it means "oops, that got moved permanently" (and then gives the new address in a `Location` header).

How Not To Fetch Data Over HTTP
-------------------------------

Let's say you want to download a resource over `http`, such as an Atom feed. Being a feed, you're not just going to download it once; you're going to download it over and over again. (Most feed readers will check for changes once an hour.) Let's do it the quick-and-dirty way first, and then see how you can do better.

```python
import urllib.request
a_url = 'http://diveintopython3.net/examples/feed.xml'
data = urllib.request.urlopen(a_url).read()
type(data)
#<class 'bytes'>
print(data)
'''
<?xml version='1.0' encoding='utf-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'>
    <title>dive into mark</title>
    <subtitle>currently between addictions</subtitle>
    <id>tag:diveintomark.org,2001-07-29:/</id>
    <updated>2009-03-27T21:56:07Z</updated>
    <link rel='alternate' type='text/html' href='http://diveintomark.org/'/>
'''
```

1\. The `urllib.request` module has a handy `urlopen()` function that takes the address of the page you want, and returns a file-like object that you can just `read()` from to get the full contents of the page. It just can't get any easier.

2\. The `urlopen().read()` method always returns a bytes object, not a string. **Remember, bytes are bytes; characters are an abstraction.** `http` servers don't deal in abstractions. **If you request a resource, you get bytes**. If you want it as a string, you'll need to determine the character encoding and explicitly convert it to a string.

Once you start thinking in terms of a web service that you want to access on a regular basis (e.g. requesting this feed once an hour), then you're being inefficient, and you're being rude.

What's On The Wire?
-------------------

To see why this is inefficient and rude, let's turn on the debugging features of Python's `http` library and see what's being sent "on the wire" (i.e. over the network).

```python
from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
from urllib.request import urlopen
response = urlopen('http://www.feedforall.com/sample.xml')
'''
send: b'GET /sample.xml HTTP/1.1
Accept-Encoding: identity
Host: www.feedforall.com
User-Agent: Python-urllib/3.5
Connection: close
reply: 'HTTP/1.1 200 OK'
header: Date header: Server header: Last-Modified header: ETag header: Accept-Ranges header: Content-Length header: Connection header: Content-Type
'''
```

Now let's look at what the server sent back in its response.

1\. `urllib.request` relies on another standard Python library, `http.client`. We import it here so we can toggle the debugging flag on the HTTPConnection class that `urllib.request` uses to connect to the `HTTP` server.

2\. Now that the debugging flag is set, information on the http request and response is printed out in real time. As you can see, when you request the Atom feed, the urllib.request module sends eight lines to the server.

3\. The 1st line specifies the `HTTP` verb you're using, and the path of the resource (minus the domain name).

4\. The 2nd line specifies the compression algorithms that the client supports. `urllib.request` does not support compression by default.

5\. The 3rd line specifies the domain name from which we're requesting this feed.

6\. The fourth line specifies the name of the library that is making the request. By default, this is `Python-urllib` plus a version number. Both `urllib.request` and `httplib2` support changing the user agent, simply by adding a User-Agent header to the request (which will override the default value).

Now let's look at what the server sent back in its response.

```python
# continued from previous example
print(response.headers.as_string())
'''
Date: Mon, 27 Jun 2016 16:46:37 GMT
Server: Apache/2.2.31
Last-Modified: Tue, 19 Oct 2004 12:39:14 GMT
ETag: "21b7-3e6cc2e432080"
Accept-Ranges: bytes
Content-Length: 8631
Connection: close
Content-Type: application/xml
'''
data = response.read()
len(data)
# 8631
```

As you can see, this code is already inefficient: it asked for (and received) uncompressed data. I know for a fact that this server supports gzip compression, but `http` compression is opt-in. We didn't ask for it, so we didn't get it. That means we're fetching 8631 bytes when we could have fetched 2821.

But wait, it gets worse! To see just how inefficient this code is, let's request the same feed a second time.

```python
# continued from the previous example
response2 = urlopen('http://www.feedforall.com/sample.xml')
'''
send: b'GET /sample.xml HTTP/1.1
Accept-Encoding: identity
Host: www.feedforall.com
User-Agent: Python-urllib/3.5
Connection: close
reply: 'HTTP/1.1 200 OK'
header: Date header: Server header: Last-Modified header: ETag header: Accept-Ranges header: Content-Length header: Connection header: Content-Type
'''
```

It hasn't changed! It's exactly the same as the first request.

-	No sign of `If-Modified-Since` headers.
-	No sign of `If-None-Match` headers.
-	No respect for the caching headers.
-	Still no compression.

> And what happens when you do the same thing twice? You get the same response. Twice.

```python
# continued from previous example
print(response2.headers.as_string())
'''
Date: Mon, 27 Jun 2016 16:46:37 GMT
Server: Apache/2.2.31
Last-Modified: Tue, 19 Oct 2004 12:39:14 GMT
ETag: "21b7-3e6cc2e432080"
Accept-Ranges: bytes
Content-Length: 8631
Connection: close
Content-Type: application/xml
'''
data2 = response.read()
len(data2)
#8631
data2 == data
#True
```

http is designed to work better than this. It's time to upgrade to a library that speaks `HTTP` fluently.

Introducing `httplib2`
----------------------

To use `httplib2`, create an instance of the `httplib2.Http` class.

```python
import httplib2
h = httplib2.Http('cache')
response, content = h.request('http://www.feedforall.com/sample.xml')
response.status
#200
# a `status` code of `200` indicates that the request was successful.
content[:52]
b'<!DOCTYPE html><body style="padding:0; margin:0;"><h'
len(content)
#8631
```

1\. The primary interface to `httplib2` is the `Http` object. For reasons you'll see in the next section, **you should always pass a directory name when you create an `Http` object**. The directory does not need to exist; `httplib2` will create it if necessary.

2\. Once you have an `Http` object, retrieving data is as simple as calling the `request()` method with the address of the data you want. This will issue an `http GET` request for that `url`.

3\. The `content` variable contains the actual data that was returned by the `http` server. The data is returned as a `bytes` object, not a string. If you want it as a string, you'll need to determine the character encoding and convert it yourself.

> **You probably only need one `httplib2.Http` object. There are valid reasons for creating more than one, but you should only do so if you know why you need them**. "I need to request data from two different urls" is not a valid reason. Re-use the `Http` object and just call the `request()` method twice.

### Why `httplib2` Returns Bytes Instead of Strings

How could `httplib2` know what kind of resource you're requesting? It's usually listed in the `Content-Type http` header, but that's an optional feature of `http` and not all `http` servers include it. If that header is not included in the `http` response, it's left up to the client to guess. (This is commonly called "content sniffing," and it's never perfect.)

If you know what sort of resource you're expecting (an `xml` document in this case), perhaps you could "just" pass the returned bytes object to the `xml.etree.ElementTree.parse()` function. That'll work as long as the `xml` document includes information on its own character encoding (as this one does), but that's an optional feature and not all `xml` documents do that. If an `xml` document doesn't include encoding information, the client is supposed to look at the enclosing transport -- i.e. the `Content-Type http` header, which can include a charset parameter.

But it's worse than that. Now character encoding information can be in two places: within the `xml` document itself, and within the `Content-Type http` header. If the information is in both places, which one wins? According to [RFC 3023](http://www.ietf.org/rfc/rfc3023.txt), if the media type given in the `Content-Type http` header is `application/xml`, `application/xml-dtd`, `application/xml-external-parsed-entity`, or any one of the subtypes of `application/xml` such as `application/atom+xml` or `application/rss+xml` or even `application/rdf+xml`, then the encoding is

1.	the encoding given in the charset parameter of the `Content-Type http` header, or
2.	the encoding given in the encoding attribute of the `xml` declaration within the document, or
3.	`utf-8`

On the other hand, if the media type given in the `Content-Type http` header is `text/xml`, `text/xml-external-parsed-entity`, or a subtype like `text/AnythingAtAll+xml`, then the encoding attribute of the `xml` declaration within the document is ignored completely, and the encoding is

1.	the encoding given in the charset parameter of the `Content-Type http` header, or
2.	`us-ascii`

And that's just for `xml` documents. For `html` documents, web browsers have constructed such [byzantine rules for content-sniffing](http://www.adambarth.com/papers/2009/barth-caballero-song.pdf) that [we're still trying to figure them all out](http://www.google.com/search?q=barth+content-type+processing+model).

### How `httplib2` Handles Caching

You should always create an httplib2.Http object with a directory name. Caching is the reason.

```python
# continued from the previous example
response2, content2 = h.request('http://www.feedforall.com/sample.xml')

response2.status
#200
content2[:52]
b'<!DOCTYPE html><body style="padding:0; margin:0;"><h'
len(content2)
#8631
```

Relaunch it with a new session, and I'll show you.

```python
# NOT continued from previous example!
# Please exit out of the interactive shell
# and launch a new one.
import httplib2
httplib2.debuglevel = 1
h = httplib2.Http('cache')
response, content = h.request('http://www.feedforall.com/sample.xml')
len(content)
#8631
response.status
#200
response.fromcache
#True
```

1\. Request the same url as before. Nothing appears to happen. More precisely, nothing gets sent to the server, and nothing gets returned from the server. There is absolutely no network activity whatsoever.

2\. this "response" was generated from `httplib2`'s local cache. That directory name you passed in when you created the `httplib2.Http` object -- that directory holds `httplib2`'s cache of all the operations it's ever performed.

> If you want to turn on httplib2 debugging, you need to set a module-level constant (`httplib2.debuglevel`), then create a new `httplib2.Http` object. If you want to turn off debugging, you need to change the same module-level constant, then create a new httplib2.Http object.

You previously requested the data at this `url`. That request was successful (`status: 200`). That response included not only the feed data, but also a set of caching headers that told anyone who was listening that they could cache this resource for up to ... hours. `httplib2` understand and respects the Etag, and it stored the previous response in the `cache` directory (which you passed in when you create the `Http` object). That cache hasn't expired yet, so the second time you request the data at this `url`, `httplib2` simply returns the cached result without ever hitting the network.

Obviously there is a lot of complexity hidden behind that simplicity. `httplib2` handles `http` caching *automatically* and by *default*. If for some reason you need to know whether a response came from the cache, you can check `response.fromcache`. Otherwise, it Just Works.

Now, suppose you have data cached, but you want to bypass the cache and re-request it from the remote server. Browsers sometimes do this if the user specifically requests it. For example, pressing `F5` refreshes the current page, but pressing `Ctrl+F5` bypasses the cache and re-requests the current page from the remote server. You might think "oh, I'll just delete the data from my local cache, then request it again." You could do that, but remember that there may be more parties involved than just you and the remote server. What about those intermediate proxy servers? They're completely beyond your control, and they may still have that data cached, and will happily return it to you because (as far as they are concerned) their cache is still valid.

Instead of manipulating your local cache and hoping for the best, you should use the features of `http` to ensure that your request actually reaches the remote server.

```python
# continued from the previous example
response2, content2 = h.request('http://www.feedforall.com/sample.xml',
    headers={'cache-control':'no-cache'})
response2.status
#200
response2.fromcache
#False
```

`httplib2` allows you to add arbitrary `http` headers to any outgoing request. In order to bypass *all* caches (not just your local disk cache, but also any caching proxies between you and the remote server), add a *no-cache* header in the headers dictionary.

### How `httplib2` Handles `Last-Modified` and `ETag` Headers

The `Cache-Control` and `Expires` caching headers are called *freshness indicators*. They tell caches in no uncertain terms that you can completely avoid all network access until the cache expires. And that's exactly the behavior you saw in the previous section: given a freshness indicator, `httplib2` does not generate a single byte of network activity to serve up cached data (unless you explicitly bypass the cache, of course).

But what about the case where the data might have changed, but hasn't? `http` defines `Last-Modified` and `Etag` headers for this purpose. These headers are called *validators*. If the local cache is no longer fresh, a client can send the validators with the next request to see if the data has actually changed. If the data hasn't changed, the server sends back a `304` status code *and no data*. So there's still a round-trip over the network, but you end up downloading fewer bytes.

```python
import httplib2
httplib2.debuglevel = 1
h = httplib2.Http('cache')
response, content = h.request('http://www.diveintopython3.net')
'''
send: b'GET / HTTP/1.1
Host: www.diveintopython3.net
accept-encoding: gzip, deflate
user-agent: Python-httplib2/0.8 (gzip)'
reply: 'HTTP/1.1 200 OK'
header: x-amz-id-2 header: x-amz-request-id header: Date header: Last-Modified header: ETag header: Content-Type header: Content-Length header: Server'
header: x-amz-id-2 header: x-amz-request-id header: Date header: Last-Modified header: ETag header: Server
'''
import pprint
pprint.pprint(dict(response.items()))
'''
pprint(dict(response.items()))
{'content-length': '4524',
 'content-location': 'http://www.diveintopython3.net/',
 'content-type': 'text/html',
 'date': 'Tue, 28 Jun 2016 08:40:14 GMT',
 'etag': '"37f58e288616124be5daa1748f93d916"',
 'last-modified': 'Wed, 12 Oct 2011 19:46:20 GMT',
 'server': 'AmazonS3',
 'status': '304',
 'x-amz-id-2': 'vac4XErjlctSsIz1K2fuNOXa1Od43SGNQ5HB3Xdi02yba8C3PEzQQy7B7ExLLp13ad0w2ItYbL8=',
 'x-amz-request-id': 'DBE0B8BE790A474D'}
'''
len(content)
#8631
```

1\. Instead of the feed, this time we're going to download the site's home page, which is `html`. Since this is the first time you've ever requested this page, `httplib2` has little to work with, and it sends out a minimum of headers with the request.

2\. The response contains a multitude of `http` headers... but no caching information. However, it does include both an ETag and Last-Modified header.

Let request the same page again, with the same `Http` object (and the same local cache).

```python
# continued from the previous example
response, content = h.request('http://diveintopython3.net')
'''
send: b'GET / HTTP/1.1
Host: www.diveintopython3.net
if-modified-since: Wed, 12 Oct 2011 19:46:20 GMT
if-none-match: "37f58e288616124be5daa1748f93d916"
accept-encoding: gzip, deflate
user-agent: Python-httplib2/0.8 (gzip)'
reply: ''
send: b'GET / HTTP/1.1
Host: www.diveintopython3.net
if-modified-since: Wed, 12 Oct 2011 19:46:20 GMT
if-none-match: "37f58e288616124be5daa1748f93d916"
accept-encoding: gzip, deflate
user-agent: Python-httplib2/0.8 (gzip)'
reply: 'HTTP/1.1 304 Not Modified'
header: x-amz-id-2 header: x-amz-request-id header: Date header: Last-Modified header: ETag header: Server
'''
response.fromcache
#True
response.status
#200
response.dict['status']
#'304'
len(content)
#4524
```

1\. `httplib2` sends the `ETag` validator back to the server in the `If-None-Match` header.

2\. `httplib2` also sends the `Last-Modified` validator back to the server in the `If-Modified-Since` header.

3\. The server looked at these validators, looked at the page you requested, and determined that the page has not changed since you last requested it, so it sends back a `304` status code *and no data*.

4\. Back on the client, `httplib2` notices the `304` status code and loads the content of the page from its cache.

5\. This might be a bit confusing. There are really two status codes -- `304` (returned from the server this time, which caused `httplib2` to look in its cache), and `200` (returned from the server last time, and stored in `httplib2`'s cache along with the page data). `response.status` returns the status from the cache.

6\. If you want the raw status code returned from the server, you can get that by looking in `response.dict`, which is a dictionary of the *actual headers returned from the server*.

### How `http2lib` Handles Compression

`http` supports several types of compression; the two most common types are `gzip` and deflate. `httplib2` supports both of these.

```python
response, content = h.request('http://diveintopython3.net')
'''
send: b'GET / HTTP/1.1
Host: www.diveintopython3.net
if-modified-since: Wed, 12 Oct 2011 19:46:20 GMT
if-none-match: "37f58e288616124be5daa1748f93d916"
accept-encoding: gzip, deflate
user-agent: Python-httplib2/0.8 (gzip)'
reply: ''
send: b'GET / HTTP/1.1
Host: www.diveintopython3.net
if-modified-since: Wed, 12 Oct 2011 19:46:20 GMT
if-none-match: "37f58e288616124be5daa1748f93d916"
accept-encoding: gzip, deflate
user-agent: Python-httplib2/0.8 (gzip)'
reply: 'HTTP/1.1 304 Not Modified'
header: x-amz-id-2 header: x-amz-request-id header: Date header: Last-Modified header: ETag header: Server
'''
pprint(dict(response.items()))
'''
pprint(dict(response.items()))
{'content-length': '4524',
 'content-location': 'http://www.diveintopython3.net/',
 'content-type': 'text/html',
 'date': 'Tue, 28 Jun 2016 08:40:14 GMT',
 'etag': '"37f58e288616124be5daa1748f93d916"',
 'last-modified': 'Wed, 12 Oct 2011 19:46:20 GMT',
 'server': 'AmazonS3',
 'status': '304',
 'x-amz-id-2': 'vac4XErjlctSsIz1K2fuNOXa1Od43SGNQ5HB3Xdi02yba8C3PEzQQy7B7ExLLp13ad0w2ItYbL8=',
 'x-amz-request-id': 'DBE0B8BE790A474D'}
'''
```

Every time `httplib2` sends a request, it includes an `Accept-Encoding` header to tell the server that it can handle either `deflate` or `gzip` compression.

### How `httplib2` Handles Redirects

`http` defines two kinds of redirects: temporary and permanent. There's nothing special to do with temporary redirects except follow them, which httplib2 does automatically.

```python
import httplib2
httplib2.debuglevel = 1
h = httplib2.Http('cache')
response, content = h.request('http://diveintopython3.net/examples/feed-302.xml')
'''
connect: (diveintopython3.net, 80)
send: b'GET /examples/feed-302.xml HTTP/1.1
Host: diveintopython3.net
accept-encoding: deflate, gzip
user-agent: Python-httplib2/$Rev: 259 $'
reply: 'HTTP/1.1 302 Found'
send: b'GET /examples/feed.xml HTTP/1.1
Host: diveintopython3.net
accept-encoding: deflate, gzip
user-agent: Python-httplib2/$Rev: 259 $'
reply: 'HTTP/1.1 200 OK'
'''
```

1\. `httplib2` sends a request for the `url` you asked for. The server comes back with a response that says "No no, look over there instead." `httplib2` sends another request for the new `url`.

2\. The response you get back from this single call to the `request()` method is the response from the final `url`.

3\. `httplib2` adds the final `url` to the response dictionary, as `content-location`. This is not a header that came from the server; it's specific to `httplib2`.

The `response` you get back gives you information about the final `url`. What if you want more information about the intermediate `url`s, the ones that eventually redirected to the final `url`? `httplib2` lets you do that, too.

```python
# continued from the previous example
response.previous
'''
{'status': '302',
 'content-length': '228',
 'content-location': 'http://diveintopython3.net/examples/feed-302.xml',
 'expires': 'Thu, 04 Jun 2009 02:21:41 GMT',
 'server': 'Apache',
 'connection': 'close',
 'location': 'http://diveintopython3.net/examples/feed.xml',
 'cache-control': 'max-age=86400',
 'date': 'Wed, 03 Jun 2009 02:21:41 GMT',
 'content-type': 'text/html; charset=iso-8859-1'}
'''
type(response)
#<class 'httplib2.Response'>
type(response.previous)
#<class 'httplib2.Response'>
response.previous.previous
```

What happens if you request the same url again?

```python
# continued from the previous example
response2, content2 = h.request('http://diveintopython3.net/examples/feed-302.xml')
'''
connect: (diveintopython3.net, 80)
send: b'GET /examples/feed-302.xml HTTP/1.1
Host: diveintopython3.net
accept-encoding: deflate, gzip
user-agent: Python-httplib2/$Rev: 259 $'
reply: 'HTTP/1.1 302 Found'
'''
content2 == content
#True
```

1\. The `302` response was not cached, so `httplib2` sends another request for the same `url`.

2\. Once again, the server responds with a `302`. But notice what didn't happen: there wasn't ever a second request for the final `url`, `http://diveintopython3.net/examples/feed.xml`. That response was cached (remember the `Cache-Control` header that you saw in the previous example). Once `httplib2` received the `302` Found code, it checked its cache before issuing another request. The cache contained a fresh copy of `http://diveintopython3.net/examples/feed.xml`, so there was no need to re-request it

Permanent redirects are just as simple.

```python
# continued from the previous example
response, content = h.request('http://diveintopython3.net/examples/feed-301.xml')
'''
connect: (diveintopython3.net, 80)
send: b'GET /examples/feed-301.xml HTTP/1.1
Host: diveintopython3.net
accept-encoding: deflate, gzip
user-agent: Python-httplib2/$Rev: 259 $'
reply: 'HTTP/1.1 301 Moved Permanently'
'''
response.fromcache
#True

response2, content2 = h.request('http://diveintopython3.net/examples/feed-301.xml')
response2.fromcache
#True
content2 == content
#True
```

Here's the difference between temporary and permanent redirects: once `httplib2` follows a permanent redirect, all further requests for that `url` will transparently be rewritten to the target `url` without hitting the network for the original `url`. Remember, debugging is still turned on, yet there is no output of network activity whatsoever.

Beyond `httplib2`
-----------------

[Requests: HTTP for Humans](http://docs.python-requests.org/en/master/)

> Requests allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor. There's no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, powered by urllib3, which is embedded within Requests.

### Why not Httplib2?

Chris Adams gave an excellent summary on [Hacker News](http://news.ycombinator.com/item?id=2884406):

> `httplib2` is part of why you should use `requests`: it's far more respectable as a client but not as well documented and it still takes way too much code for basic operations. I appreciate what `httplib2` is trying to do, that there's a ton of hard low-level annoyances in building a modern HTTP client, but really, just use requests instead. Kenneth Reitz is very motivated and he gets the degree to which simple things should be simple whereas `httplib2` feels more like an academic exercise than something people should use to build production systems[1].
>
> [1]: http://code.google.com/p/httplib2/issues/detail?id=96 is a good example: an annoying bug which affect many people, there was a fix available for months, which worked great when I applied it in a fork and pounded a couple TB of data through it, but it took over a year to make it into trunk and even longer to make it onto PyPI where any other project which required `httplib2` would get the working version.
