import math
import datetime
from enum import Enum

class X:
    def __init__(self):
        self.a = 1
        self._a = 2
        self.__a = 3
    def get_hidden_attribute(self):
        return self.__a
    def set_hidden_attribute(self, a):
        self.__a = a

class Y(object):
    def __init__(self):
        self.__a = 1
    def get_a(self):
        print("hello from get_a")
        return self.__a
    a = property(get_a)

#--------------------------------------------------------------------------------

class Point:
    """ this is help for Point class """
    def __init__(self, x: float, y: float):
        if (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            self._x = x
            self._y = y
        else:
            self._x = 0
            self._y = 0
            print("x,y values must be numbers. setting them to 0,0 by default")

    # getter
    @property
    def x(self):
        """ get/set x value of point entity """
        return self._x
    @property
    def y(self):
        """ get/set y value of point entity """
        return self._y

    # setter
    @x.setter
    def x(self, value):
        self._x = value
    @y.setter
    def y(self, value):
        self._y = value

    # deleter
    @x.deleter
    def x(self):
        """ x value cannot be deleted """
        print("point values cannot be deleted")
    @y.deleter
    def y(self):
        """ y value cannot be deleted """
        print("point values cannot be deleted")


# EX2 (implement property class)

class MyProperty:
    def __init__(self, fget):
        self.fget = fget
        self.fset = None
        self.fdel = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("Can't delete attribute")
        self.fdel(instance)

    def setter(self, fset):
        self.fset = fset
        return self

    def deleter(self, fdel):
        self.fdel = fdel
        return self

class MyTestClass:
    def __init__(self, val):
        self.__x = int(val)

    @MyProperty
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be integer")
        self.__x = value

    @x.deleter
    def x(self):
        print("Deleting x")
        del self.__x


#-----------------------------------------------------------------------------------------

if __name__ == '__main__':
    x = X()
    print(x.a)
    print(x._a)
#    print(x.__a)
    print(x.__dict__)
    print(x._X__a)
    x._X__a = 56
    print(x._X__a)
    print(x.get_hidden_attribute())
    x.set_hidden_attribute(45)
    print(x.get_hidden_attribute())

    y = Y()
    print(y.a)

    p = Point(10, 20)
    print(p.x, p.y)
    p.x = 12
    print(p.x, p.y)
    p.y = 45
    print(p.x, p.y)
    del(p.x)
    print(p.x, p.y)

    p2 = Point('a',6)
    print(p2.x, p2.y)

    #help(Point)

    print("EX2: ")
    a = MyTestClass(3)
    print(a.x)
    print(MyTestClass(4).x)
    a.x = 8
    print(a.x)
    del a.x

    try:
        b = 10/0
    except Exception as e:
        print("something went wrong", e)
    except ZeroDivisionError:
        print("division by zero2")
