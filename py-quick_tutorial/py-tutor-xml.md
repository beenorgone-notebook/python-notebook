Python Quick References
=======================

**Content:**

1.	`xml` module or `lxml` module
2.	Parsing XML
	1.	Parser objects
	2.	Incremental parsing
	3.	Event-driven parsing
	4.	Parsing Broken XML
3.	Generate A XML
	1.	Elements Are Lists
	2.	Attributes Are Dictonaries
	3.	Elements contain text
4.	Searching For Nodes Within An XML Document
5.	Using XPath to find text
6.	Serialisation
7.	The `ElementTree` class
8.	Namespace

`xml` or `lxml`
---------------

```python
try:
	from lxml import etree
	print("running with lxml.etree")
except ImportError:
	try:
		import xml.etree.ElementTree as etree
		print("running with ElementTree on Python")
	except ImportError:
		try:
			# normal ElementTree install
			import elementtree.ElementTree as etree
			print("running with ElementTree")
		except ImportError:
			print("Failed to import ElementTree from any known place")
```

Parsing XML
-----------

`xml` module

```python
import xml.etree.ElementTree as etree
tree = etree.parse('feed.xml')
root = tree.getroot()
root
#<Element '{http://www.w3.org/2005/Atom}feed' at 0x7f0d97342d18>
tree
#<xml.etree.ElementTree.ElementTree object at 0x7f0d9739eb00>
```

`lxml.etree`

```python
#The `fromstring()` function
some_xml_data = "<root>data</root>"
root = etree.fromstring(some_xml_data)
print(root.tag)
#root
etree.tostring(root)
#b'<root>data</root>'

#The `XML()` function commonly used to write XML literals right into the source:. There is also a corresponding function `HTML()` for HTML literals.
root = etree.XML("<root>data</root>")
print(root.tag)
#root
etree.tostring(root)
#b'<root>data</root>

#The `parse()` function is used to parse from files and file-like objects
some_file_like_object = BytesIO("<root>data</root>")
tree = etree.parse(some_file_like_object)
etree.tostring(tree)
#b'<root>data</root>'
```

### Parser objects

By default, `lxml.etree` uses a standard parser with a default setup. If you want to configure the parser, you can create a you instance:

```python
parser = etree.XMLParser(remove_blank_text=True) # lxml.etree only!

root = etree.XML("<root>  <a/>   <b>  </b>     </root>", parser)
etree.tostring(root)
#b'<root><a/><b>  </b></root>'

# he whitespace content inside the <b> tag was not removed, as content at leaf elements tends to be data content (even if blank). You can easily remove it in an additional step by traversing the tree:
for element in root.iter("*"):
    if element.text is not None and not element.text.strip():
        element.text = None

etree.tostring(root)
#b'<root><a/><b/></root>'
```

### Incremental parsing

`lxml.etree` provides two ways for incremental step-by-step parsing.

```python
# This is best used where the data arrives from a source like `urllib` or any other file-like object that can provide data on request.
# NOTE: the parser will block and wait until data becomes available in this case:
class DataSource:
    data = [ b"<roo", b"t><", b"a/", b"><", b"/root>" ]
    def read(self, requested_size):
        try:
            return self.data.pop(0)
        except IndexError:
            return b''

tree = etree.parse(DataSource())
etree.tostring(tree)
#b'<root><a/></root>'

# The second way is through a feed parser interface, given by the feed(data) and close() methods:
parser = etree.XMLParser()

parser.feed("<roo")
parser.feed("t><")
parser.feed("a/")
parser.feed("><")
parser.feed("/root>")

root = parser.close()
etree.tostring(root)j
#b'<root><a/></root>'j

# NOTE: This comes in handy if you want to avoid blocking calls to the parser, e.g. in frameworks like Twisted, or whenever data comes in slowly or in chunks and you want to do other things while waiting for the next chunk.
```

### Event-driven parsing

Sometimes, all you need from a document is a small fraction somewhere deep inside the tree. `lxml.etree` supports this use case with two event-driven parser interfaces, one that generates parser events while building the tree (`iterparse`), and one that does not build the tree at all, and instead calls feedback methods on a target object in a SAX-like fashion.

```python
some_file_like = BytesIO("<root><a>data</a></root>")

for event, element in etree.iterparse(some_file_like):
    print("%s, %4s, %s" % (event, element.tag, element.text))
#end,    a, data
#end, root, None

# By default, iterparse() only generates events when it is done parsing an element, but you can control this through the events keyword argument:
for event, element in etree.iterparse(some_file_like,
                                        events=("start", "end")):
    print("%5s, %4s, %s" % (event, element.tag, element.text))
#start, root, None
#start,    a, data
#  end,    a, data
#  end, root, None

some_file_like = BytesIO("<root><a><b>data</b></a><a><b/></a></root>")

for event, element in etree.iterparse(some_file_like):
    if element.tag == 'b':
        print(element.text)
    elif element.tag == 'a':
        print("** cleaning up the subtree")
        element.clear()
#data
#** cleaning up the subtree
#None
#** cleaning up the subtree

xml_file = BytesIO('''<root>
        <a><b>ABC</b><c>abc</c></a>
        <a><b>MORE DATA</b><c>more data</c></a>
        <a><b>XYZ</b><c>xyz</c></a>
    </root>''')

for _, element in etree.iterparse(xml_file, tag='a'):
    print('%s -- %s' % (element.findtext('b'), element[1].text))
    element.clear()
#ABC -- abc
#MORE DATA -- more data
#XYZ -- xyz
```

### Parsing Broken XML

feed_broken.xml

```xml
<?xml version='1.0' encoding='utf-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'>
  <title>dive into &hellip;</title>
...
</feed>
```

```python
tree1 = lxml.etree.parse('feed_broken.xml')
#Error ....
```

To parse this broken `xml` document, despite its wellformedness error, you need to create a custom `xml` parser.

```python
parser = lxml.etree.XMLParser(recover=True)
tree = lxml.etree.parse('feed_broken.xml', parser)
parser.error_log
#feed_broken.xml:3:28:FATAL:PARSER:ERR_UNDECLARED_ENTITY: Entity 'hellip' not defined
tree.findall('{http://www.w3.org/2005/Atom}title')
#[<Element {http://www.w3.org/2005/Atom}title at 0x7eff8620e648>]
title = tree.findall('{http://www.w3.org/2005/Atom}title')[0]
title.text
#'dive into '
print(lxml.etree.tounicode(tree.getroot()))
#<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
#  <title>dive into </title>
#...
#</feed>
```

Generating XML
--------------

`xml.etree.ElementTree`

```python
import xml.etree.ElementTree as etree
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
			 attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
print(etree.tostring(new_feed))
#'<ns0:feed xmlns:ns0="http://www.w3.org/2005/Atom" xml:lang="en" />'
```

`lxml.etree`

```python
import lxml.etree as etree
root = etree.Element("root")
print(root.tag)
#root

NSMAP = {None: 'http://www.w3.org/2005/Atom'}
new_feed = lxml.etree.Element('feed', nsmap=NSMAP)
new_feed
#<Element feed at 0x7eff872d9d08>
print(lxml.etree.tounicode(new_feed))
#<feed xmlns="http://www.w3.org/2005/Atom"/>
new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
print(lxml.etree.tounicode(new_feed))
#<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en"/>

#To create child elements and add them to a parent element, you can use the `append()` method or `SubElement` factory:
root.append(etree.Element("child1"))
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

print(etree.tostring(root, pretty_print=True))
#b'<root>\n  <child1/>\n  <child2/>\n  <child3/>\n</root>\n'
print(etree.tounicode(root, pretty_print=True))
#<root>
#  <child1/>
#  <child2/>
#  <child3/>
#</root>

title = lxml.etree.SubElement(new_feed, 'title',
			      attrib={'type':'html'})
print(lxml.etree.tounicode(new_feed))
#<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en"><title type="html"/></feed>
title.text = 'dive into &hellip;'
print(lxml.etree.tounicode(new_feed, pretty_print=True))
#<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
#  <title type="html">dive into &amp;hellip;</title>
#</feed>
```

Third-party library `xmlwitch` makes extensive use of the `with` statement to make `xml` generation code more readable.

```python
import xmlwitch
xml = xmlwitch.Builder(version='1.0', encoding='utf-8')
with xml.feed(xmlns='http://www.w3.org/2005/Atom'):
	xml.title('Example Feed')
	xml.updated('2003-12-13T18:30:02Z')
	with xml.author:
		xml.name('John Doe')
	xml.id('urn:uuid:60a76c80-d399-11d9-b93C-0003939e0af6')
	with xml.entry:
		xml.title('Atom-Powered Robots Run Amok')
		xml.id('urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a')
		xml.updated('2003-12-13T18:30:02Z')
		xml.summary('Some text.')
print(xml)
```

### Elements Are Lists

`xml.etree.ElementTree`

```python
root.tag
'{http://www.w3.org/2005/Atom}feed'
len(root)
8
for child in root:
	print(child)

<Element '{http://www.w3.org/2005/Atom}title' at 0x7f0d973582c8>
<Element '{http://www.w3.org/2005/Atom}subtitle' at 0x7f0d97358318>
<Element '{http://www.w3.org/2005/Atom}id' at 0x7f0d97358408>
<Element '{http://www.w3.org/2005/Atom}updated' at 0x7f0d97358458>
<Element '{http://www.w3.org/2005/Atom}link' at 0x7f0d973584f8>
<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358548>
<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d973589f8>
<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358db8>
```

`lxml.etree`

In the `ElementTree API`, an element acts like a list. The items of the list are the element’s children. Elements mimic the behavior of normal Python lists as closely as possible:

```python
child = root[0]
print(child.tag)
#child1
print(len(root))
#3
root.index(root[1])
#1
children = list(root)
children
#[<Element child1 at 0x7eff8620e248>, <Element child2 at 0x7eff8620e8c8>, <Element child3 at 0x7eff87309d08>]

for child in root:
	print(child.tag)
#child1
#child2
#child3

root.insert(0, etree.Element('child0'))

start = root[:1]
end = root[-1:]
print(start[0].tag)
#child0
print(end[0].tag)
#child3

print(etree.iselement(root))  # test if it's some kind of Element
#True
if len(root):                 # test if it has children
	print("The root element has children")
#The root element has children
```

```python
for child in root:
	print(child.tag)
#child0
#child1
#child2
#child3
root[0] = root[-1]  # this moves the element in lxml.etree!
for child in root:
	print(child.tag)
#child3
#child1
#child2

root is root[0].getparent()  # lxml.etree only!
#True

#If you want to *copy* an element to a different position in `lxml.etree`,
#consider creating an independent *deep copy* using the `copy` module from Python's standard library:
```python
from copy import deepcopy
element = etree.Element("neu")
element.append( deepcopy(root[1]) )
print(element[0].tag)
#child1
print([ c.tag for c in root ])
#['child3', 'child1', 'child2']

root[0] is root[1].getprevious() # lxml.etree only!
#True
root[1] is root[0].getnext() # lxml.etree only!
#True
```

### Attributes Are Dictonaries

**The `attrib` property is a dictionary of the element’s attributes**.

```python
root.attrib
#{'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
root[4]
#<Element {http://www.w3.org/2005/Atom}link at e181b0>
root[4].attrib
#{'href': 'http://diveintomark.org/',
# 'type': 'text/html',
# 'rel': 'alternate'}
root[3]
#<Element {http://www.w3.org/2005/Atom}updated at e2b4e0>
root[3].attrib
#{}

root = etree.Element("root", interesting="totally")
etree.tounicode(root)
#'<root interesting="totally"/>'

print(root.get("interesting"))
#totally
print(root.get("hello"))
#None

root.set("hello", "Huhu")
print(root.get("hello"))
#Huhu
etree.tounicode(root)
'<root interesting="totally" hello="Huhu"/>'
sorted(root.keys())
#['hello', 'interesting']
root.keys() == root.attrib.keys()
#True

for name, value in sorted(root.items()):
	print('%s = %r' % (name, value))
#hello = 'Huhu'
#interesting = 'totally'

root.items()
#[('interesting', 'totally'), ('hello', 'Huhu')]
root.items() == root.attrib.items()
#True

#To get an independent snapshot of the attributes
#that does not depend on the XML tree, copy it into a dict:
d = dict(root.attrib)
d
#{'interesting': 'totally', 'hello': 'Huhu'}
d.items()
#dict_items([('interesting', 'totally'), ('hello', 'Huhu')])
sorted(d.items())
#[('hello', 'Huhu'), ('interesting', 'totally')]
```

### Elements contain text

```python
html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"
etree.tounicode(html)
#'<html><body>TEXT</body></html>'

br = etree.SubElement(body, "br")
etree.tounicode(html)
#'<html><body>TEXT<br/></body></html>'

br.tail = "TAIL"
etree.tostring(html)
#b'<html><body>TEXT<br/>TAIL</body><body><br/></body></html>'

# `tostring()` & `tounicode()` accepts the keyword argument `with_tail`
etree.tounicode(br)
#'<br/>TAIL'
etree.tounicode(br, with_tail=False) #lxml.etree only!
#'<br/>'

# Read only text without any intermediate tags
etree.tostring(html, method="text")
#b'TEXTTAIL'
```

Searching For Nodes Within An XML Document
------------------------------------------

```python
import xml.etree.ElementTree as etree

# `findall()` only return *direct children*
tree = etree.parse('examples/feed.xml')
root = tree.getroot()
root.findall('{http://www.w3.org/2005/Atom}entry')
#[<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358548>, <Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d973589f8>, <Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358db8>]
root.tag
#'{http://www.w3.org/2005/Atom}feed'
root.findall('{http://www.w3.org/2005/Atom}feed')
#[]
root.findall('{http://www.w3.org/2005/Atom}author')
#[]

tree.findall('{http://www.w3.org/2005/Atom}entry')
#[<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358548>, <Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d973589f8>, <Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358db8>]
tree.findall('{http://www.w3.org/2005/Atom}author')
#[]

root.findall('{http://www.w3.org/2005/Atom}entry') == tree.findall('{http://www.w3.org/2005/Atom}entry')
#True
root == tree
#False

# There is also a `find()` method which returns the first matching element.
entries = tree.findall('{http://www.w3.org/2005/Atom}entry')
len(entries)
#3
entries[0]
#<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358548>
entries[0][1]
#<Element '{http://www.w3.org/2005/Atom}title' at 0x7f0d973586d8>
entries[0][0]
#<Element '{http://www.w3.org/2005/Atom}author' at 0x7f0d97358598>
title_element = entries[0].find('{http://www.w3.org/2005/Atom}title')
entries[0][1].text
#'Dive into history, 2009 edition'
title_element.text
#'Dive into history, 2009 edition'
foo_element = entries[0].find('{http://www.w3.org/2005/Atom}foo')
type(foo_element)
#<class 'NoneType'>

# search for *descendant* elements
all_links = tree.findall('//{http://www.w3.org/2005/Atom}link')
all_links
#[<Element {http://www.w3.org/2005/Atom}link at e181b0>,
# <Element {http://www.w3.org/2005/Atom}link at e2b570>,
# <Element {http://www.w3.org/2005/Atom}link at e2b480>,
# <Element {http://www.w3.org/2005/Atom}link at e2b5a0>]
```

Using XPath to find text
------------------------

```python
print(html.xpath("string()")) # lxml.etree only!
#TEXTTAIL
print(html.xpath("//text()")) # lxml.etree only!
#['TEXT', 'TAIL']
build_text_list = etree.XPath("//text()") # lxml.etree only!
print(build_text_list(html))
#['TEXT', 'TAIL']

# NOTE:*a string result returned by XPath is a special 'smart' object that knows about its origins*. You can ask it where it came from through its `getparent()` method, just as you would with Elements:
texts = build_text_list(html)
print(texts[0])
#TEXT
parent = texts[0].getparent()
print(parent.tag)
#body

# You can also find out if it's normal text content or tail text:
print(texts[0].is_text)
#True
print(texts[1].is_text)
#False
print(texts[1].is_tail)
#True

# `lxml` will not tell you the origin of a string value that was constructed by the XPath functions `string()` or `concat()`:
stringify = etree.XPath("string()")
print(stringify(html))
#TEXTTAIL
print(stringify(html).getparent())
#None
```

Tree iteration
--------------

If you are only interested in a single tag, you can pass its name to `iter()` to have it filter for you.

```python
root = etree.Element("root")
etree.SubElement(root, "child").text = "Child 1"
etree.SubElement(root, "child").text = "Child 2"
etree.SubElement(root, "another").text = "Child 3"

for element in root.iter("child"):
	print("%s - %s" % (element.tag, element.text))
#child - Child 1
#child - Child 2

for element in root.iter("another", "child"):
	print("%s - %s" % (element.tag, element.text))
#child - Child 1
#child - Child 2
#another - Child 3

# NOTE: By default, iteration yields all nodes in the tree, including ProcessingInstructions, Comments and Entity instances. If you want to make sure only Element objects are returned, you can pass the `Element` factory as tag parameter:
root.append(etree.Entity("#234"))
root.append(etree.Comment("some comment"))

for element in root.iter():
	print("{} - {}".format(element.tag, element.text))
#root - None
#child - Child 1
#child - Child 2
#another - Child 3
#<cyfunction Entity at 0x7fef8c57d328> - &#234;
#<cyfunction Comment at 0x7fef8c57d1b8> - some comment

for element in root.iter(tag=etree.Entity):
	print(element.text)
#&#234;
```

Serialisation
-------------

```python
root = etree.XML('<root><a><b/></a></root>')
etree.tostring(root)
#b'<root><a><b/></a></root>'
print(etree.tostring(root, xml_declaration=True))
#b"<?xml version='1.0' encoding='ASCII'?>\n<root><a><b/></a></root>"
print(etree.tostring(root, encoding='iso-8859-1'))
#b"<?xml version='1.0' encoding='iso-8859-1'?>\n<root><a><b/></a></root>"
print(etree.tostring(root, pretty_print=True))
#b'<root>\n  <a>\n    <b/>\n  </a>\n</root>\n'
print(etree.tounicode(root, pretty_print=True))
#<root>
#  <a>
#    <b/>
#  </a>
#</root>
```

`method` keyword:

```python
root = etree.XML(
	'<html><head/><body><p>Hello<br/>World</p></body></html>')

etree.tostring(root) # default: method = 'xml'
#b'<html><head/><body><p>Hello<br/>World</p></body></html>'

etree.tostring(root, method='xml') # same as above
#b'<html><head/><body><p>Hello<br/>World</p></body></html>'

etree.tostring(root, method='html')
#b'<html><head></head><body><p>Hello<br>World</p></body></html>'

etree.tostring(root, method='text')
#b'HelloWorld'

'''
As for XML serialisation, the default encoding for plain text serialisation is ASCII:
'''
br = next(root.iter('br'))  # get first result of iteration
br.tail =u'W\xf6rld'
etree.tostring(root, method='text')  # doctest: +ELLIPSIS
#UnicodeEncodeError: 'ascii' codec can't encode character '\xf6' in position 6: ordinal not in range(128)
etree.tostring(root, method='text', encoding="UTF-8")
b'HelloW\xc3\xb6rld'
etree.tostring(root, encoding='unicode', method='text')
#'HelloWörld'
```

The `ElementTree` class
-----------------------

An `ElementTree` is mainly a document wrapper around a tree with a root node. It provides a couple of methods for serialisation and general document handling.

An `ElementTree` is also what you get back when you call the `parse()` function to parse files or file-like objects.

```python
root = etree.XML('''<?xml version="1.0"?> <!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]> <root> <a>&tasty;</a> </root> ''')

tree = etree.ElementTree(root) print(tree.docinfo.xml_version) #1.0 print(tree.docinfo.doctype) #<!DOCTYPE root SYSTEM "test"> tree.docinfo.public_id = '-//W3C//DTD XHTML 1.0 Transitional//EN' tree.docinfo.system_url = 'file://local.dtd' print(tree.docinfo.doctype) #<!DOCTYPE root PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "file://local.dtd">

print(etree.tounicode(tree))
#<!DOCTYPE root PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "file://local.dtd" \[ #<!ENTITY tasty "parsnips"> #]>
#<root>
#   <a>parsnips</a>
#</root>
```

8. Namespace
============

The ElementTree API avoids **namespace prefixes** wherever possible and deploys the real namespace (the URI) instead:

```python
xhtml = etree.Element("{http://www.w3.org/1999/xhtml}html")
body = etree.SubElement(xhtml, "{http://www.w3.org/1999/xhtml}body")
body.text = "Hello World"

print(etree.tostring(xhtml, pretty_print=True))
#<html:html xmlns:html="http://www.w3.org/1999/xhtml">
#  <html:body>Hello World</html:body>
#</html:html>

# To define the default namespace:
XHTML_NAMESPACE = "http://www.w3.org/1999/xhtml"
XHTML = "{%s}" % XHTML_NAMESPACE

NSMAP = {None : XHTML_NAMESPACE} # the default namespace (no prefix)

xhtml = etree.Element(XHTML + "html", nsmap=NSMAP) # lxml only!
body = etree.SubElement(xhtml, XHTML + "body")
body.text = "Hello World"

print(etree.tostring(xhtml, pretty_print=True))
#<html xmlns="http://www.w3.org/1999/xhtml">
#   <body>Hello World</body>
#</html>

# Use `QName` helper class to build or split qualified tag names:
tag = etree.QName('http://www.w3.org/1999/xhtml', 'html')
print(tag.localname)
#html
print(tag.namespace)
#http://www.w3.org/1999/xhtml
print(tag.text)
#{http://www.w3.org/1999/xhtml}html

tag = etree.QName('{http://www.w3.org/1999/xhtml}html')
print(tag.localname)
#html
print(tag.namespace)
#http://www.w3.org/1999/xhtml

root = etree.Element('{http://www.w3.org/1999/xhtml}html')
tag = etree.QName(root)
print(tag.localname)
#html

tag = etree.QName(root, 'script')
print(tag.text)
#{http://www.w3.org/1999/xhtml}script
tag = etree.QName('{http://www.w3.org/1999/xhtml}html', 'script')
print(tag.text)
#{http://www.w3.org/1999/xhtml}script

xhtml.nsmap
{None: 'http://www.w3.org/1999/xhtml'}
```
