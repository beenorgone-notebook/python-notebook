[Dive into Python 3: XML](http://www.diveintopython3.net/xml.html)
==================================================================

Table of contents
-----------------

1.	Diving In
2.	A 5-Minute Crash Course in XML
3.	The Structure Of An Atom Feed
4.	Parsing XML
5.	Elements Are Lists
6.	Attributes Are Dictonaries
7.	Searching For Nodes Within An XML Document
8.	Going Further With lxml
9.	Generating XML
10.	Parsing Broken XML
11.	Further Reading

Diving In
---------

We’ll be working with `xml` in this chapter. It’s a feed — specifically, an Atom syndication feed.

A 5-Minute Crash Course in XML
------------------------------

`xml` is a generalized way of describing hierarchical structured data. An `xml` *document* contains one or more *elements*, which are delimited by *start and end tags*. This is a complete (albeit boring) `xml` document:

```xml
<foo>
</foo>
```

Elements can be *nested* to any depth. An element `bar` inside an element `foo` is said to be a *subelement* or *child* of `foo`.

```xml
<foo>
  <bar></bar>
</foo>
```

The first element in every `xml` document is called the *root element*. An `xml` document can only have one root element. The following is **not an `xml` document**, because it has two root elements:

```xml
<foo></foo>
<bar></bar>
```

Elements can have *attributes*, which are name-value pairs. Attributes are listed within the start tag of an element and separated by whitespace. *Attribute names* can not be repeated within an element. *Attribute values* must be quoted. You may use either single or double quotes. Each element has its own set of attributes.

If an element has more than one attribute, the ordering of the attributes is not significant. An element’s attributes form an unordered set of keys and values, like a Python dictionary. There is no limit to the number of attributes you can define on each element.

Elements can have text content. Elements that contain no text and no children are *empty*.

```xml
<foo lang='en'>
  <bar id='papayawhip' lang="fr">Papayawhip</bar>
</foo>
```

There is a shorthand for writing empty elements. By putting a `/` character in the start tag, you can skip the end tag altogther. The `xml` document in the previous example could be written like this instead:

```xml
<foo/>
```

Like Python functions can be declared in different *modules*, `xml` elements can be declared in different *namespaces*. Namespaces usually look like URLs. You use an `xmlns` declaration to define a *default namespace*. A namespace declaration looks similar to an attribute, but it has a different purpose.

```xml
<feed xmlns='http://www.w3.org/2005/Atom'>
  <title>dive into mark</title>
</feed>
```

1.	The feed element is in the `http://www.w3.org/2005/Atom` namespace.
2.	The title element is also in the `http://www.w3.org/2005/Atom` namespace. The namespace declaration affects the element where it’s declared, plus all child elements.

You can also use an `xmlns:prefix` declaration to define a namespace and associate it with a *prefix*. Then each element in that namespace must be explicitly declared with the prefix.

```xml
<atom:feed xmlns:atom='http://www.w3.org/2005/Atom'>
  <atom:title>dive into mark</atom:title>
</atom:feed>
```

As far as an `xml` parser is concerned, the previous two `xml` documents are *identical*. Namespace + element name = `xml` identity. Prefixes only exist to refer to namespaces, so the actual prefix name (`atom:`) is irrelevant. The namespaces match, the element names match, the attributes (or lack of attributes) match, and each element’s text content matches, therefore the `xml` documents are the same.

Finally, `xml` documents can contain character encoding information on the first line, before the root element. (If you’re curious how a document can contain information which needs to be known before the document can be parsed, [Section F of the xml specification details](https://www.w3.org/TR/REC-xml/#sec-guessing-no-ext-info) how to resolve this Catch-22.)

```xml
<?xml version='1.0' encoding='utf-8'?>
```

The Structure Of An Atom Feed
-----------------------------

Think of a weblog, or in fact any website with frequently updated content, like CNN.com. The site itself has a title (“CNN.com”), a subtitle (“Breaking News, U.S., World, Weather, Entertainment & Video News”), a last-updated date (“updated 12:43 p.m. EDT, Sat May 16, 2009”), and a list of articles posted at different times. Each article also has a title, a first-published date (and maybe also a last-updated date, if they published a correction or fixed a typo), and a unique URL.

The Atom syndication format is designed to capture all of this information in a standard format. My weblog and CNN.com are wildly different in design, scope, and audience, but they both have the same basic structure. CNN.com has a title; my blog has a title. CNN.com publishes articles; I publish articles.

At the top level is the root element, which every Atom feed shares: the feed element in the `http://www.w3.org/2005/Atom` namespace.

```xml
<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'>
```

Any element can contain an `xml:lang` attribute, which declares the language of the element and its children. In this case, the `xml:lang` attribute is declared once on the root element, which means the entire feed is in English.

An Atom feed contains several pieces of information about the feed itself. These are declared as children of the root-level feed element.

```xml
<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'>
  <title>dive into mark</title>
  <subtitle>currently between addictions</subtitle>
  <id>tag:diveintomark.org,2001-07-29:/</id>
  <updated>2009-03-27T21:56:07Z</updated>
  <link rel='alternate' type='text/html' href='http://diveintomark.org/'/>
```

Now we know that this is a feed for a site named “dive into mark“ which is available at http://diveintomark.org and was last updated on March 27, 2009.

> Although the order of elements can be relevant in some `xml` documents, it is not relevant in an Atom feed.

After the feed-level metadata is the list of the most recent articles. An article looks like this:

```xml
<entry>
  <author>    
    <name>Mark</name>
    <uri>http://diveintomark.org/</uri>
  </author>
  <title>Dive into history, 2009 edition</title>
  <link rel='alternate' type='text/html'
    href='http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'/>
  <id>tag:diveintomark.org,2009-03-27:/archives/20090327172042</id>
  <updated>2009-03-27T21:56:07Z</updated>
  <published>2009-03-27T17:20:42Z</published>
  <category scheme='http://diveintomark.org' term='diveintopython'/>
  <category scheme='http://diveintomark.org' term='docbook'/>
  <category scheme='http://diveintomark.org' term='html'/>
  <summary type='html'>Putting an entire chapter on one page sounds bloated, but consider this &amp;mdash; my longest chapter so far would be 75 printed pages, and it loads in under 5 seconds&amp;hellip;
    On dialup.</summary>
</entry>
```

1\. The author element tells who wrote this article: some guy named Mark, whom you can find loafing at http://diveintomark.org/. (This is the same as the alternate link in the feed metadata, but it doesn’t have to be. Many weblogs have multiple authors, each with their own personal website.)

2\. The `title` element gives the title of the article, “Dive into history, 2009 edition”.

3\. As with the feed-level alternate link, this link element gives the address of the `html` version of this article.

4\. Entries, like feeds, need a unique identifier.

5\. Entries have two dates: a first-published date (`published`) and a last-modified date (`updated`).

6\. Entries can have an arbitrary number of categories. This article is filed under `diveintopython`, `docbook`, and `html`.

7\. The `summary` element gives a brief summary of the article. (There is also a `content` element, not shown here, if you want to include the complete article text in your feed.) This `summary` element has the Atom-specific `type='html'` attribute, which specifies that this summary is a snippet of `html`, not plain text. This is important, since it has html-specific entities in it (`&mdash;` and `&hellip;`) which should be rendered as “—” and “…” rather than displayed directly.

8\. Finally, the end tag for the entry element, signaling the end of the metadata for this article.

Parsing XML
-----------

Python can parse `xml` documents in several ways. It has traditional `dom` and `sax` parsers, but I will focus on a different library called ElementTree.

```python
import xml.etree.ElementTree as etree
tree = etree.parse('feed.xml')
root = tree.getroot()
root
#<Element '{http://www.w3.org/2005/Atom}feed' at 0x7f0d97342d18>
tree
#<xml.etree.ElementTree.ElementTree object at 0x7f0d9739eb00>
```

1\. The ElementTree library is part of the Python standard library, in `xml.etree.ElementTree`.

2\. The primary entry point for the ElementTree library is the `parse()` function, which can take a filename or a file-like object. This function parses the entire document at once. If memory is tight, there are ways to parse an `xml` document incrementally instead.

3\. The `parse()` function returns an object which represents the entire document. This is *not* the root element. To get a reference to the root element, call the `getroot()` method.

4\. The root element is the feed element in the http://www.w3.org/2005/Atom namespace. *An `xml` element is a combination of its namespace and its tag name (also called the local name)*. Every element in this document is in the Atom namespace, so the root element is represented as `{http://www.w3.org/2005/Atom}feed`.

> ElementTree represents `xml` elements as `{namespace}localname`. You’ll see and use this format in multiple places in the ElementTree `api`.

### Elements Are Lists

In the `ElementTree API`, an element acts like a list. The items of the list are the element’s children.

```python
# continued from the previous example
root.tag
#'{http://www.w3.org/2005/Atom}feed'
len(root)
#8
for child in root:
	print(child)

#<Element '{http://www.w3.org/2005/Atom}title' at 0x7f0d973582c8>
#<Element '{http://www.w3.org/2005/Atom}subtitle' at 0x7f0d97358318>
#<Element '{http://www.w3.org/2005/Atom}id' at 0x7f0d97358408>
#<Element '{http://www.w3.org/2005/Atom}updated' at 0x7f0d97358458>
#<Element '{http://www.w3.org/2005/Atom}link' at 0x7f0d973584f8>
#<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358548>
#<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d973589f8>
#<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358db8>
```

1\. The “length” of the root element is the number of child elements.

2\. You can use the element itself as an iterator to loop through all of its child elements.

3\. The list of child elements only includes *direct* children. Each of the `entry` elements contain their own children, but those are not included in the list.

### Attributes Are Dictonaries

`xml` isn’t just a collection of elements; each element can also have its own set of attributes. Once you have a reference to a specific element, you can easily get its attributes as a Python dictionary.

```python
# continuing from the previous example
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
```

**The `attrib` property is a dictionary of the element’s attributes**. The original markup here was `<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'>`. The `xml:` prefix refers to a built-in namespace that every `xml` document can use without declaring it.

Searching For Nodes Within An XML Document
------------------------------------------

Many uses of `xml` require you to find specific elements. `Etree` can do that, too.

```python
import xml.etree.ElementTree as etree
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
```

1\. The `findall()` method finds child elements that match a specific query. (More on the query format in a minute.)

2\. Each element — including the `root` element, but also child elements — has a `findall()` method. It finds all matching elements among the element’s children. But why aren’t there any results? Although it may not be obvious, this particular query only searches the element’s children. Since the `root` feed element has no child named `feed`, this query returns an empty list.

3\. `findall()` only return *direct children* of the root elements. If you want to look for author elements at any nesting level, you can do that, but the query format is slightly different.

Use `findall()` with `tree` object (returned from the `etree.parse()` function)

```python
tree.findall('{http://www.w3.org/2005/Atom}entry')
#[<Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358548>, <Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d973589f8>, <Element '{http://www.w3.org/2005/Atom}entry' at 0x7f0d97358db8>]
tree.findall('{http://www.w3.org/2005/Atom}author')
#[]
```

There is also a `find()` method which returns the first matching element.

```python
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
foo_element
type(foo_element)
#<class 'NoneType'>
```

> In a boolean context, ElementTree element objects will evaluate to `False` if they contain no children (i.e. if `len(element)` is 0). This means that `if element.find('...')` is not testing whether the `find()` method found a matching element; it’s testing whether that matching element has any child elements! To test whether the `find()` method returned an element, use `if element.find('...') is not None`.

There *is* a way to search for *descendant* elements, i.e. children, grandchildren, and any element at any nesting level.

```python
all_links = tree.findall('//{http://www.w3.org/2005/Atom}link')
all_links
#[<Element {http://www.w3.org/2005/Atom}link at e181b0>,
# <Element {http://www.w3.org/2005/Atom}link at e2b570>,
# <Element {http://www.w3.org/2005/Atom}link at e2b480>,
# <Element {http://www.w3.org/2005/Atom}link at e2b5a0>]
all_links[0].attrib
#{'href': 'http://diveintomark.org/',
# 'type': 'text/html',
# 'rel': 'alternate'}
all_links[1].attrib
#{'href': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
# 'type': 'text/html',
# 'rel': 'alternate'}
all_links[2].attrib
#{'href': 'http://diveintomark.org/archives/2009/03/21/accessibility-is-a-harsh-mistress',
# 'type': 'text/html',
# 'rel': 'alternate'}
all_links[3].attrib
#{'href': 'http://diveintomark.org/archives/2008/12/18/give-part-1-container-formats',
# 'type': 'text/html',
# 'rel': 'alternate'}
```

Those two slashes in `//{http://www.w3.org/2005/Atom}link` mean “don’t just look for direct children; I want any elements, regardless of nesting level.” So the result is a list of four link elements, not just one.

Going Further With `lxml`
-------------------------

[`lxml`](http://lxml.de/) is an open source third-party library that builds on the popular `libxml2` parser. It provides a 100% compatible ElementTree `api`, then extends it with full XPath 1.0 support and a few other niceties.

Once imported, `lxml` provides the same `api` as the built-in ElementTree library.

For large `xml` documents, `lxml` is significantly faster than the built-in ElementTree library. If you’re only using the ElementTree api and want to use the fastest available implementation, you can try to import `lxml` and fall back to the built-in ElementTree.

```python
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
```

But `lxml` is more than just a faster ElementTree. Its `findall()` method includes support for more complicated expressions.

```python
import lxml.etree
tree = lxml.etree.parse('feed.xml')
tree.findall('//{http://www.w3.org/2005/Atom}*[@href]')
#[<Element {http://www.w3.org/2005/Atom}link at 0x7eff872e6208>, <Element {http://www.w3.org/2005/Atom}link at 0x7eff872e6188>, <Element {http://www.w3.org/2005/Atom}link at 0x7eff872e6148>, <Element {http://www.w3.org/2005/Atom}link at 0x7eff8729f6c8>]
tree.findall("//{http://www.w3.org/2005/Atom}*[@href='http://diveintomark.org/']")
#[<Element {http://www.w3.org/2005/Atom}link at 0x7eff872e6208>]
NS = '{http://www.w3.org/2005/Atom}'
tree.findall('//{NS}author[{NS}uri]'.format(NS=NS))
#[<Element {http://www.w3.org/2005/Atom}author at 0x7eff872d9c88>, <Element {http://www.w3.org/2005/Atom}author at 0x7eff872d9f88>]
```

1\. `tree.findall('//{http://www.w3.org/2005/Atom}*[@href]')` finds all elements in the Atom namespace, anywhere in the document, that have an `href` attribute. The `//` at the beginning of the query means "elements anywhere (not just as children of the root element)."

2\. `tree.findall("//{http://www.w3.org/2005/Atom}*[@href='http://diveintomark.org/']")` finds all Atom elements with an `href` whose value is `http://diveintomark.org/`.

3\. `tree.findall('//{NS}author[{NS}uri]'.format(NS=NS))` searches for Atom `author` elements that have an Atom `uri` element as a child.

`lxml` also integrates support for arbitrary XPath 1.0 expressions (for xpath syntax, read xml-xpath note)

```python
import lxml.etree
tree = lxml.etree.parse('feed.xml')
NSMAP = {'atom': 'http://www.w3.org/2005/Atom'}
entries = tree.xpath("//atom:category[@term='accessibility']/..", namespaces=NSMAP)
entries
#[<Element {http://www.w3.org/2005/Atom}entry at 0x7eff87309ec8>]
entry = entries[0]
entry.xpath('./atom:title/text()', namespaces=NSMAP)
#['Accessibility is a harsh mistress']
```

1\. To perform XPath queries on namespaced elements, you need to define a namespace prefix mapping. This is just a Python dictionary: `NSMAP = {'atom': 'http://www.w3.org/2005/Atom'}`

2\. This XPath expressions `//atom:category[@term='accessibility']/..` searches for`category` elements (in the Atom namespace) that contain a `term` attribute with the value`accessibility`. But that’s not actually the query result. Look at the very end of the query string; did you notice the `/..` bit? That means “and then return the parent element of the `category` element you just found.” So this single XPath query will find all entries with a child element of `<category term='accessibility'>`.

3\. The `xpath()` function returns a list of ElementTree objects. In this document, there is only one entry with a `category` whose term is `accessibility`.

4\. XPath expressions don't always return a list of elements. Technically, the `DOM` of a parsed `xml` document doesn’t contain elements; it contains *nodes*. Depending on their type, nodes can be elements, attributes, or even text content. The result of an XPath query is a list of nodes. This query returns a list of text nodes: the text content (`text()`) of the title element (`atom:title`) that is a child of the current element (`./`).

Generating XML
--------------

Python’s support for `xml` is not limited to parsing existing documents. You can also create `xml` documents from scratch.

```python
import xml.etree.ElementTree as etree
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
			 attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
print(etree.tostring(new_feed))
#'<ns0:feed xmlns:ns0="http://www.w3.org/2005/Atom" xml:lang="en" />'
```

1\. To create a new element, instantiate the `Element` class. You pass the element name (namespace + local name) as the first argument. This statement creates a `feed` element in the Atom namespace. This will be our new document’s root element.

2\. To add attributes to the newly created element, pass a dictionary of attribute names and values in the `attrib` argument. Note that the attribute name should be in the standard ElementTree format, `{namespace}localname`.

3\. At any time, you can serialize any element (and its children) with the ElementTree `tostring()` function.

The way ElementTree serializes namespaced `xml` elements is technically accurate but not optimal. An `xml` parser won’t “see” any difference between an `xml` document with a default namespace and an xml document with a prefixed namespace. The resulting `DOM` of this serialization:

`<ns0:feed xmlns:ns0='http://www.w3.org/2005/Atom' xml:lang='en'/>`

is identical to the `DOM` of this serialization:

`<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'/>`

The only practical difference is that the second serialization is several characters shorter. For something like an Atom feed, which may be downloaded several thousand times whenever it changes, saving a few bytes per request can quickly add up.

The built-in ElementTree library does not offer this fine-grained control over serializing namespaced elements, but `lxml` does.

```python
import lxml.etree
NSMAP = {None: 'http://www.w3.org/2005/Atom'}
new_feed = lxml.etree.Element('feed', nsmap=NSMAP)
new_feed
#<Element feed at 0x7eff872d9d08>
print(lxml.etree.tounicode(new_feed))
#<feed xmlns="http://www.w3.org/2005/Atom"/>
new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
print(lxml.etree.tounicode(new_feed))
#<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en"/>
NSMAP = {NotNone: 'http://www.w3.org/2005/Atom'}
#Traceback (most recent call last):
#  File "<pyshell#55>", line 1, in <module>
#    NSMAP = {NotNone: 'http://www.w3.org/2005/Atom'}
#NameError: name 'NotNone' is not defined
```

1\. To start, define a namespace mapping as a dictionary. Dictionary values are namespaces; dictionary keys are the desired prefix. Using `None` as a prefix effectively declares a default namespace.

2\. Now you can pass the `lxml`-specific `nsmap` argument when you create an element, and `lxml` will respect the namespace prefixes you’ve defined.

3\. As expected, this serialization defines the Atom namespace as the default namespace and declares the `feed` element without a namespace prefix.

4\. You can always add attributes to any element with the `set()` method. It takes two arguments: the attribute name in standard ElementTree format, then the attribute value. (This method is not `lxml`-specific. The only `lxml`-specific part of this example was the nsmap argument to control the namespace prefixes in the serialized output.)

You can easily create child elements, too.

```python
title = lxml.etree.SubElement(new_feed, 'title',
			      attrib={'type':'html'})
print(lxml.etree.tounicode(new_feed))
#<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en"><title type="html"/></feed>
title.text
title.text = 'dive into &hellip;'
print(lxml.etree.tounicode(new_feed))
#<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en"><title type="html">dive into &amp;hellip;</title></feed>
print(lxml.etree.tounicode(new_feed, pretty_print=True))
#<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
#  <title type="html">dive into &amp;hellip;</title>
#</feed>
```

1\. To create a child element of an existing element, instantiate the `SubElement` class. The only required arguments are the parent element (`new_feed` in this case) and the new element’s name. Since this child element will inherit the namespace mapping of its parent, there is no need to redeclare the namespace or prefix here.

2\. You can also pass in an attribute dictionary. Keys are attribute names; values are attribute values.

3\. Since the title element has no text content and no children of its own, `lxml` serializes it as an empty element (with the `/>` shortcut).

4\. To set the text content of an element, simply set its `.text` property.

5\. You can also apply “pretty printing” to the serialization, which inserts line breaks after end tags, and after start tags of elements that contain child elements but no text content. In technical terms, `lxml` adds “insignificant whitespace” to make the output more readable.

> You might also want to check out `xmlwitch`, another third-party library for generating `xml`. It makes extensive use of the `with` statement to make `xml` generation code more readable.

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

Parsing Broken XML
------------------

The `xml` specification mandates that all conforming `xml` parsers employ “draconian error handling.” That is, they must halt and catch fire as soon as they detect any sort of wellformedness error in the `xml` document. Wellformedness errors include mismatched start and end tags, undefined entities, illegal Unicode characters, and a number of other esoteric rules. This is in stark contrast to other common formats like `html` — your browser doesn’t stop rendering a web page if you forget to close an `html` tag or escape an ampersand in an attribute value.

Here is a fragment of a broken xml document. I’ve highlighted the wellformedness error.

```xml
<?xml version='1.0' encoding='utf-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'>
  <title>dive into &hellip;</title>
...
</feed>
```

That’s an error, because the `&hellip;` entity is not defined in `xml`. (It is defined in `html`.) If you try to parse this broken feed with the default settings, `lxml` will choke on the undefined entity.

```python
tree1 = lxml.etree.parse('feed_broken.xml')
#Traceback (most recent call last):
#  File "<pyshell#67>", line 1, in <module>
#  tree1 = lxml.etree.parse('feed_broken.xml')
#  File "src/lxml/lxml.etree.pyx", line 3427, in lxml.etree.parse (src/lxml/lxml.etree.c:85131)
#  File "src/lxml/parser.pxi", line 1782, in lxml.etree._parseDocument (src/lxml/lxml.etree.c:124005)
#  File "src/lxml/parser.pxi", line 1808, in lxml.etree._parseDocumentFromURL (src/lxml/lxml.etree.c:124374)
#  File "src/lxml/parser.pxi", line 1712, in lxml.etree._parseDocFromFile (src/lxml/lxml.etree.c:123169)
#  File "src/lxml/parser.pxi", line 1115, in lxml.etree._BaseParser._parseDocFromFile (src/lxml/lxml.etree.c:117533)
#  File "src/lxml/parser.pxi", line 573, in lxml.etree._ParserContext._handleParseResultDoc (src/lxml/lxml.etree.c:110510)
#  File "src/lxml/parser.pxi", line 683, in lxml.etree._handleParseResult (src/lxml/lxml.etree.c:112276)
#  File "src/lxml/parser.pxi", line 613, in lxml.etree._raiseParseError (src/lxml/lxml.etree.c:111124)
#  File "<string>", line None
#lxml.etree.XMLSyntaxError: Entity 'hellip' not defined, line 3, column 28
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

1\. To create a custom parser, instantiate the `lxml.etree.XMLParser` class. It can take a number of different named arguments. The one we’re interested in here is the `recover` argument. When set to `True`, the `xml` parser will try its best to “recover” from wellformedness errors.

2\. To parse an `xml` document with your custom parser, pass the parser object as the second argument to the `parse()` function. Note that `lxml` does not raise an exception about the undefined `&hellip;` entity.

3\. The parser keeps a log of the wellformedness errors that it has encountered. (This is actually true regardless of whether it is set to recover from those errors or not.)

4\. Since it didn’t know what to do with the undefined `&hellip;` entity, the parser just silently dropped it. The text content of the title element becomes `'dive into '`.

5\. As you can see from the serialization, the `&hellip;` entity didn’t get moved; it was simply dropped.

It is important to reiterate that there is no guarantee of interoperability with “recovering” xml parsers. A different parser might decide that it recognized the `&hellip;` entity from `html`, and replace it with `&amp;hellip;` instead. Is that “better”? Maybe. Is it “more correct”? No, they are both equally incorrect. The correct behavior (according to the `xml` specification) is to halt and catch fire. If you’ve decided not to do that, you’re on your own.
