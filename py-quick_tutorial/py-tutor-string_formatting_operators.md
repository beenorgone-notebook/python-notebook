String Formatting Operators
===========================

<!-- toc orderedList:0 -->

- [String Formatting Operators](#string-formatting-operators)
	- [Resources](#resources)
	- [New Syntax (Python 3)](#new-syntax-python-3httpsmkaztechpython-string-formathtml)
		- [More String Formatting with `.format()`](#more-string-formatting-with-format)
			- [Named Arguments](#named-arguments)
			- [Reuse Same Variable Multiple Times](#reuse-same-variable-multiple-times)
			- [Convert Values to different Bases](#convert-values-to-different-bases)
			- [Use Format as a Function](#use-format-as-a-function)
		- [Escaping Braces](#escaping-braces)

<!-- tocstop -->

Resources
---------

-	[New syntax (Python 3): Python String Format Cookbook](https://mkaz.blog/code/python-string-format-cookbook/) by mkaz
-	[stackoverflow dicussion](http://stackoverflow.com/questions/13945749/string-formatting-in-python-3)
-	[Py Format](https://pyformat.info)

[New Syntax (Python 3)](https://mkaz.tech/python-string-format.html)
--------------------------------------------------------------------

**Syntax**: `"FORMAT".format(NUMBER)`

```python
my_age = 27
my_height = 165 #cm
my_weight = 76 #kg
print ("If i add {0}, {1}, and {2} I get {3}".format(my_age, my_height, my_weight, my_age + my_height + my_weight))
```

With the new python string formatter you can use numbered parameters so you don't have to count how many you have.

```python
set = " ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}) ".format(a,b,c,d,e,f,g)
```

### More String Formatting with `.format()`

#### Named Arguments

You can use the new string format as a templating engine and use named arguments, instead of requiring a strict order.

```python
madlib = " I {verb} the {object} off the {place} ".format(verb="took", object="cheese", place="table")
~~ I took the cheese off the table
```

#### Reuse Same Variable Multiple Times

The .format() method allows you to put them in any order as we saw above in the basics, but also allows for reuse.

```python
str = "Oh {0}, {0}! wherefore art thou {0}?".format("Romeo")
~~ Oh Romeo, Romeo! wherefore art thou Romeo?
```

#### Convert Values to different Bases

You can use the following letters to convert a number to their bases, decimal (**d**), hex (**x**), octal (**o**), binary (**b**\)

```python
print("{0:d} - {0:x} - {0:o} - {0:b}".format(21))
~~ 21 - 15 - 25 - 10101
```

#### Use Format as a Function

You can use `.format` as a function which allows for some separation of text and formatting from code. For example at the beginning of your program you could include all your formats and then use later. This also could be a nice way to handle internationalization which not only requires different text but often requires different formats for numbers.

```python
## defining formats
email_f = "Your email address was {email}".format

## use elsewhere
print(email_f(email="bob@example.com"))
```

### Escaping Braces

If you need to use braces when using str.format(), just double up

```python
print("The {} set is often represented as {% raw %}{{0}}{% endraw %}".format("empty"))
~~ The empty set is often represented as {0}
```

| Number     | Format    | Output    | Description                                   |
|------------|-----------|-----------|-----------------------------------------------|
| 3.1415926  | `{:.2f}`  | 3.14      | 2 decimal places                              |
| 3.1415926  | `{:+.2f}` | +3.14     | 2 decimal places with sign                    |
| -1         | `{:+.2f}` | -1.00     | 2 decimal places with sign                    |
| 2.71828    | `{:.0f}`  | 3         | No decimal places                             |
| 5          | `{:0>2d}` | 05        | Pad number with zeros (left padding, width 2) |
| 5          | `{:x<4d}` | 5xxx      | Pad number with x's (right padding, width 4)  |
| 10         | `{:x<4d}` | 10xx      | Pad number with x's (right padding, width 4)  |
| 1000000    | `{:,}`    | 1,000,000 | Number format with comma separator            |
| 0.25       | `{:.2%}`  | 25.00%    | Format percentage                             |
| 1000000000 | `{:.2e}`  | 1.00e+09  | Exponent notation                             |
| 13         | `{:10d}`  | 13        | Right aligned (default, width 10)             |
| 13         | `{:<10d}` | 13        | Left aligned (width 10)                       |
| 13         | `{:^10d}` | 13        | Center aligned (width 10)                     |
