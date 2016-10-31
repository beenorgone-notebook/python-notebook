[XPath](http://www.w3schools.com/xsl/xpath_syntax.asp)
======================================================

XPath uses path expressions to select nodes or node-sets in an XML document. The node is selected by following a path or steps.

We will use the following XML document in the examples below:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<bookstore>

<book>
  <title lang="en">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="en">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
```

Selecting Nodes
---------------

XPath uses path expressions to select nodes in an XML document. The node is selected by following a path or steps. The most useful path expressions are listed below:

| Expression | Description                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------|
| `nodename` | Selects all nodes with the name "nodename"                                                            |
| `/`        | Selects from the root node                                                                            |
| `//`       | Selects nodes in the document from the current node that match the selection no matter where they are |
| `.`        | Selects the current node                                                                              |
| `..`       | Selects the parent of the current node                                                                |
| `@`        | Selects attributes                                                                                    |

EXAMPLES:

| Path Expression   | Result                                                                                                                                   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `bookstore`       | Selects all nodes with the name `bookstore`                                                                                              |
| `/bookstore`      | Selects the root element `bookstore`. **Note**: If the path starts with a slash `/` it always represents an absolute path to an element! |
|                   |                                                                                                                                          |
| `bookstore/book`  | Selects all `book` elements that are children of `bookstore`                                                                             |
| `//book`          | Selects all `book` elements no matter where they are in the document                                                                     |
| `bookstore//book` | Selects all `book` elements that are descendant of the `bookstore` element, no matter where they are under the `bookstore` element       |
| `//@lang`         | Selects all attributes that are named `lang`                                                                                             |

Predicates
----------

Predicates are used to find a specific node or a node that contains a specific value.

Predicates are always embedded in square brackets.

| Path Expression                      | Result                                                                                                                                                                                                                                                                                         |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/bookstore/book[1]`                 | *Selects the first book element that is the child of the bookstore element*. **Note**: In IE 5,6,7,8,9 first node is[0], but according to W3C, it is [1]. To solve this problem in IE, set the `SelectionLanguage` to `XPath:`. In JavaScript: `xml.setProperty("SelectionLanguage","XPath");` |
| `/bookstore/book[last()]`            | Selects the last `book` element that is the child of the `bookstore` element                                                                                                                                                                                                                   |
| `/bookstore/book[last()-1]`          | Selects the last but one `book` element that is the child of the `bookstore` element                                                                                                                                                                                                           |
| `/bookstore/book[position()<3]`      | Selects the first two `book` elements that are children of the `bookstore` element                                                                                                                                                                                                             |
| `//title[@lang]`                     | Selects all the `title` elements that have an attribute named `lang`                                                                                                                                                                                                                           |
| `//title[@lang='en']`                | Selects all the `title` elements that have a `lang` attribute with a value of `en`                                                                                                                                                                                                             |
| `/bookstore/book[price>35.00]`       | Selects all the `book` elements of the `bookstore` element that have a `price` element with a value greater than `35.00`                                                                                                                                                                       |
| `/bookstore/book[price>35.00]/title` | Selects all the `title` elements of the `book` elements of the `bookstore` element that have a `price` element with a value greater than `35.00`                                                                                                                                               |

Selecting Unknown Nodes
-----------------------

XPath wildcards can be used to select unknown XML nodes.

| Wildcard | Description                  |
|----------|------------------------------|
| `\*`     | Matches any element node     |
| `@\*`    | Matches any attribute node   |
| `node()` | Matches any node of any kind |

EXAMPLES:

| Path Expression | Result                                                                   |
|-----------------|--------------------------------------------------------------------------|
| `/bookstore/*`  | Selects all the child element nodes of the `bookstore` element           |
| `//*`           | Selects all elements in the document                                     |
| `//title[@*]`   | Selects all title elements which have at least one attribute of any kind |

Selecting Several Paths
-----------------------

By using the `|` operator in an XPath expression you can select several paths.

XPath Operators
---------------

Below is a list of the operators that can be used in XPath expressions:

| Operator      | Description                  | Example                     |
|---------------|------------------------------|-----------------------------|
| vertical line | Computes two node-sets       |                             |
| `+`           | Addition                     | `6 + 4`                     |
| `-`           | Subtraction                  | `6 - 4`                     |
| `*`           | Multiplication               | `6 * 4`                     |
| `div`         | Division                     | `8 div 4`                   |
| `=`           | Equal                        | `price=9.80`                |
| `!=`          | Not equal                    | `price!=9.80`               |
| `<`           | Less than                    | `price<9.80`                |
| `<=`          | Less than or equal to        | `price<=9.80`               |
| `>`           | Greater than                 | `price>9.80`                |
| `>=`          | Greater than or equal to     | `price>=9.80`               |
| `or`          | or                           | `price=9.80 or price=9.70`  |
| `and`         | and                          | `price>9.00 and price<9.90` |
| `mod`         | Modulus (division remainder) | `5 mod 2`                   |
