# Example 1: Using Descriptors to Compute Attributes
# Create the display name of an object when it is needed.


class DisplayName:

    def __get__(self, instance, owner=None):
        parts = []
        if instance.salutation:
            parts.append(instance.salutation)
        if instance.forename:
            parts.append(instance.forename[0] + '.')
        parts.append(instance.surname)
        return ' '.join(parts)


class Person:
    display_name = DisplayName()

    def __init__(self, salutation, forename, surname):
        self.salutation = salutation
        self.forename = forename
        self.surname = surname

southpaw = Person('Mr', 'Billy', 'Hope')
print(southpaw.display_name)
# Mr B. Hope

'''
When an attribute is read via a descriptor, the descriptor's
`__get__()` method is called. The `self` argument is the descriptor
instance, the `instance` argument is the instance of the object for
whose class the descriptor is defined, and the owner argument is
that class. So, when `southpaw.display_name` is used, the `Person`
class' instance of the `DisplayName` descriptor's `__get__()` method
is called with `Person.displayName` as the `self` argument,
`southpaw` as the instance argument, and `Person` as the owner
argument

Of course, the same goal could be achieved by using a display name
property. By using a descriptor, however, we can create as many
`display_name` attributes as we like, in as many different classes
as we like—all getting their behavior from the descriptor with
a single line of code for each one. This design eases maintenance;
if we need to change how the display name attribute works
(perhaps to change the format of the string it returns), we have to
change the code in only one place—in the descriptor—rather than
in individual property functions for each relevant attribute in
every affected class.
'''


# property version:
class Person:

    def __init__(self, salutation, forename, surname):
        self.salutation = salutation
        self.forename = forename
        self.surname = surname
        self._display_name = None

    @property
    def display_name(self):
        '''compute display_name'''
        parts = []
        if self.salutation:
            parts.append(self.salutation)
        if self.forename:
            parts.append(self.forename[0] + '.')
        parts.append(self.surname)
        return ' '.join(parts)

rival = Person('Mr', 'Miguel', 'Escobar')
print(rival.display_name)


'''
In some situations, we may prefer to store all or some of a class'
data outside the class, while at the same time being able to access
the data through instance attributes in the normal way.

For example, suppose we need to store large numbers of Book objects,
each holding the details of a particular book. Imagine further that
for some of the books we need to output the book's details as a
bibliographic entry in the DocBook XML format, and that when such
output is required once, it's very likely to be required again.
One way of handling this situation is to use a descriptor to
generate the XML—and to cache what it generates.
'''


# Example 2: Using Descriptors to Store Data
class BiblioEntry:

    def __init__(self):
        self.cache = {}

    def __get__(self, instance, owner=None):
        entry = self.cache.get(id(instance), None)
        if entry is not None:
            return entry
        entry = """<biblioentry>\n\t<abbrev>{surname}{yr:02d}</abbrev>\n\t<authorgroup><author>\n\t\t<firstname>{forename}</firstname>\n\t\t<surname>{surname}</surname>\n\t</author></authorgroup>\n\t<copyright><year>{year}</year></copyright>\n\t<isbn>{isbn}</isbn>\n\t<title>{title}</title>\n</biblioentry>\n""".format(
            yr=(instance.year - 2000 if instance.year >= 2000
                else instance.year - 1900),
            forename=instance.forename,
            surname=instance.surname,
            title=instance.title,
            isbn=instance.isbn, year=instance.year)
        self.cache[id(instance)] = entry
        return entry


class Book:

    biblioentry = BiblioEntry()

    def __init__(self, isbn, title, forename, surname, year):
        self.isbn = isbn
        self.title = title
        self.forename = forename
        self.surname = surname
        self.year = year

fake_book = Book(12332543534, 'Fake Song', 'Billy', 'Robb', 2016)
print(fake_book.biblioentry)


# Example 3: Combining Descriptors with Class Decorators for Validation
# - first, write a atrribute creator class (GenericDescriptor)
# - second, write a decorate function which receive a class and set
# an attribute for it using attribute creator.
class GenericDescriptor:

    def __init__(self, getter, setter):
        self.getter = getter
        self.setter = setter

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        return self.setter(instance, value)


def ValidString(attr_name, empty_allowed=True):
    def decorator(cls):
        name = '__' + attr_name
        # The decorator takes a class as argument and will create
        # a private data attribute based on the attribute name.

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            assert isinstance(value, str), (attr_name + ' must be a string')
            if not empty_allowed and not value:
                raise ValueError(attr_name + ' may not be empty')
            setattr(self, name, value)

        setattr(cls, attr_name, GenericDescriptor(getter, setter))
        return cls
    return decorator


def ValidNumber(attr_name, minimum=None, maximum=None):
    def decorator(cls):
        name = '__' + attr_name
        # The decorator takes a class as argument and will create
        # a private data attribute based on the attribute name.

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            import numbers
            assert isinstance(value, numbers.Number), (
                attr_name + " must be a number")
            if minimum is not None and value < minimum:
                raise ValueError("{0} {1} is too small".format(
                    attr_name, value))
            if maximum is not None and value > maximum:
                raise ValueError("{0} {1} is too big".format(
                    attr_name, value))
            setattr(self, name, value)

        setattr(cls, attr_name, GenericDescriptor(getter, setter))
        return cls
    return decorator


@ValidString("name", empty_allowed=False)
@ValidNumber("price", minimum=0, maximum=1e6)
@ValidNumber("quantity", minimum=1, maximum=1000)
class StockItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

cameras = StockItem("Camera", 45.99, 2)
cameras.quantity += 1  # works fine, quantity is now 3
print(cameras.quantity, cameras.__quantity)
phones = StockItem("Phone", 89.99, 14)
print(phones.quantity, phones.__quantity)
cameras.quantity = -2  # raises ValueError("quantity -2 is too small")

'''
The class decorated with one or more uses of `ValidString()` will
have two new attributes added for each use. For example, if the
name given is "name", the attributes will be `self.__name` (which
will hold the actual data) and `self.name` (a descriptor through
which the data can be accessed).
'''
