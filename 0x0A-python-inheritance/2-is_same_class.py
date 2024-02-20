#!/usr/bin/python3
"""contains is_class module"""


def is_same_class(obj, a_class):
    """returns true if obj is exactly class a_class, else false"""
    if type(obj) == a_class:
        return True
    else:
        return False
