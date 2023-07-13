#!/usr/bin/python3
"""documentation"""


def inherits_from(obj, a_class):
    """True if the object is an instance of class that inherited"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
