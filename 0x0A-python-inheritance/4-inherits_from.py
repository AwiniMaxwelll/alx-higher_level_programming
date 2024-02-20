#!/usr/bin/python3
"""contains inherit from function"""


def inherits_from(obj, a_class):
    """returns True if obj is a subclass of a_class, otherwise False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
