Python Regular Expressions
==========================

Resources
---------

-	[Python Regular Expressions](https://developers.google.com/edu/python/regular-expressions#basic-patterns) by Google Developers

Note
----

### Basic Patterns

-	`a`, `X`, `9`, `<` -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: . `^ $ * + ? { [ ] \ | ( )` (details below)
-	`.` (a period) -- matches any single character except newline `\n`
-	`\w` -- (lowercase w) matches a "word" character: a letter or digit or underbar `[a-zA-Z0-9_]`. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. `\W` (upper case W) matches any non-word character.
-	`\b` -- boundary between word and non-word
-	`\s` -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ `\n\r\t\f`]. `\S` (upper case S) matches any non-whitespace character.
-	\t, \n, \r -- tab, newline, return
-	`\d` -- decimal digit [0-9](some older regex utilities do not support but `d`, but they all support `w` and `s`)
-	`^` = start, `$` = end -- match the start or end of the string
-	`\` -- inhibit the "specialness" of a character. So, for example, use . to match a period or `\\` to match a slash. If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, `\@`, to make sure it is treated just as a character.

### Repetition

-	`+` -- 1 or more occurrences of the pattern to its left, e.g. `i+` = one or more i's
-	`*` -- 0 or more occurrences of the pattern to its left
-	`?` -- match 0 or 1 occurrences of the pattern to its left

### Square Brackets

Square brackets can be used to indicate a set of chars, so `[abc]` matches `a` or `b` or `c`. The codes `\w`, `\s` etc. work inside square brackets too with the one *exception that dot `.` just means a literal dot*.

```python
match = re.search(r'[\w.-]+@[\w.-]+', str)
    if match:
print match.group()  ## 'alice-b@google.com'
```

### Group Extraction

The "group" feature of a regular expression allows you to pick out parts of the matching text.

```python
str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search('([\w.-]+)@([\w.-]+)', str)
  if match:
    print match.group()   ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)
```

### `findall`

`findall()` is probably the single most powerful function in the `re` module. Above we used `re.search()` to find the first match for a pattern. `findall()` finds *all* the matches and returns them as a list of strings, with each string representing one match.

```python
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
  # do something with each found email string
  print email
#alice@google.com
#bob@abc.com
```

### `findall` and Groups

The parenthesis `()` group mechanism can be combined with `findall()`. If the pattern includes 2 or more parenthesis groups, then instead of returning a list of strings, `findall()` returns a list of *tuples*. Each tuple represents one match of the pattern, and inside the tuple is the group(1), group(2) .. data.

```python
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
  print tuple[0]  ## username
  print tuple[1]  ## host
```

Obscure optional feature: Sometimes you have paren `()` groupings in the pattern, but which you do not want to extract. In that case, write the parens with a `?:` at the start, e.g. `(?: )` and that left paren will not count as a group result.

### RE Workflow and Debug

Set up your runtime so you can run a pattern and print what it matches easily, for example by running it on a small test text and printing the result of `findall()`. If the pattern matches nothing, try weakening the pattern, removing parts of it so you get too many matches. When it's matching nothing, you can't make any progress since there's nothing concrete to look at. Once it's matching too much, then you can work on tightening it up incrementally to hit just what you want.

### Options

The `re` functions take options to modify the behavior of the pattern match. The option flag is added as an extra argument to the `search()` or `findall()` etc., e.g. `re.search(pat, str, re.IGNORECASE)`.

-	`IGNORECASE` -- ignore upper/lowercase differences for matching, so 'a' matches both 'a' and 'A'.
-	`DOTALL` -- allow dot (.) to match newline -- normally it matches anything but newline. This can trip you up -- you think `.*` matches everything, but by default it does not go past the end of a line. Note that `\s` (whitespace) includes newlines, so if you want to match a run of whitespace that may include a newline, you can just use `\s*`
-	`MULTILINE` -- Within a string made of many lines, allow `^` and `$` to match the start and end of each line. Normally `^/$` would just match the start and end of the whole string.

### Greedy vs. Non-Greedy

Suppose you have text with tags in it: `<b>foo</b>` and `<i>so on</i>`

Suppose you are trying to match each tag with the pattern `<.*>` -- what does it match first?

The result is a little surprising, but the greedy aspect of the `.*` causes it to match the whole `<b>foo</b>` and `<i>so on</i>` as one big match. The problem is that the `.*` *goes as far as is it can*, instead of stopping at the first `>` (aka it is "greedy").

There is an extension to regular expression where you add a `?` at the end, such as `.*?` or `.+?`, changing them to be non-greedy. Now they stop as soon as they can. So the pattern `(<.*?>)` will get just `<b>` as the first match, and `</b>` as the second match, and so on getting each `<..>` pair in turn. The style is typically that you use a `.*?`, and then immediately its right look for some concrete marker (`>` in this case) that forces the end of the `.*?` run.

```python
str = '<b>foo</b> and <i>so on</i>'
tags = re.findall(r'<.*>', str)
tags
#['<b>foo</b> and <i>so on</i>']
tags = re.findall(r'<.*?>', str)
tags
#['<b>', '</b>', '<i>', '</i>']
```

The `*?` extension originated in Perl, and regular expressions that include Perl's extensions are known as Perl Compatible Regular Expressions -- pcre. Python includes pcre support. Many command line utils etc. have a flag where they accept pcre patterns.

An older but widely used technique to code this idea of "all of these chars except stopping at X" uses the square-bracket style. For the above you could write the pattern, but instead of `.*` to get all the chars, use `[^>]*` which skips over all characters which are not `>` (the leading `^` "inverts" the square bracket set, so it matches any char not in the brackets).

### Substitution

The `re.sub(path, replacement, str)` function searches for all the instances of pattern in the given string, and replaces them. The replacement string can include `\1`, `\2` which refer to the text from group(1), group(2), and so on from the original matching text.

```python
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
```
