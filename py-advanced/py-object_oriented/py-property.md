# Property

## Resources

- [Property (programming) - Wikiwand](https://www.wikiwand.com/en/Property_(programming))
- [Getters/Setters/Fuxors](http://2ndscale.com/rtomayko/2005/getters-setters-fuxors) by Ryan Tomayko
- [The Python Property Builtin](https://webcache.googleusercontent.com/search?q=cache:4k-sY61gGK8J:adam.gomaa.us/blog/2008/aug/11/the-python-property-builtin) by Adam Gomaa

## Why `property`

Let's take a look at the Python implementation of the basic `Contact` class:

```python
class Contact(object):

    def __init__(self, first_name=None, last_name=None,
                 display_name=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.email = email

    def print_info(self):
        print self.display_name, "<" + self.email + ">"

# And code to use it:

contact = Contact()
contact.first_name = "Phillip"
contact.last_name = "Eby"
contact.display_name = "Phillip J. Eby"
contact.email = "x@x.com"
contact.print_info()
```

Now we need to implement some logic that will raise an exception if an email address is set that doesn't look like an email address:

```python
class Contact(object):

    def __init__(self, first_name=None, last_name=None,
                 display_name=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.email = email

    def print_info(self):
        print self.display_name, "<" + self.email + ">"

    def set_email(self, value):
        if '@' not in value:
            raise Exception("This doesn't look like an email address.")
        self._email = value

    def get_email(self):
        return self._email

    email = property(get_email, set_email)
```

What's happened here is that we were able to add get/set methods and still maintain backward compatibility. The following code still runs properly:

```python
contact = Contact()
contact.email = "x@x.com"
```

When the email attribute is set, the `set_email` method is called. When the email attribute is got, the `get_email` method is called.

> Now why would you want to do this? In many cases, it's because something you used to have as an actual instance attribute (say, `.url`) became a computed value, based on other instance attributes. Now, you could update all your code to call `.get_url()` instead, and write a `.set_url()` if that's possible... or you could just turn `.url` into a property.

We can use `property` as a decorator

```python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```
