#!/usr/bin/python3
""" the function cheks if the obejct is a subclass"""


def inherits_from(obj, a_class):
    """chack if the object is an instance"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
