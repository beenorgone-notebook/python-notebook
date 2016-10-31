class C:

    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property"""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def delx(self):
        del self._x


c = C()
c.x = 12
print(c.x)
