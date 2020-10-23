# class Immutable(object):
#
#     __slots__ = ["one", "two", "three"]
#     print(type(__slots__))
#
#     def __init__(self, one, two, three):
#         super(Immutable, self).__setattr__("one", one)
#         super(Immutable, self).__setattr__("two", two)
#         super(Immutable, self).__setattr__("three", three)
#
#     def __setattr__(self, key, value):
#         msg = "%s has no attribute %s" % (self.__class__, key)
#
#         raise AttributeError(msg)
#
#
# i = Immutable(1, 2, 3)
# i.one = 1


class A:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


# a = A(12)
# b = A(22)
# c = A("aa")
# d = A("bb")
# print(a+b)
# print(c+d)

import copy

a = [10,20,30,[4,5]]
b = copy.copy(a)
a[3][1] = 11
a[2] = 1
print(a, b)
