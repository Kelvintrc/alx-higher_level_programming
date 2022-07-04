#!/usr/bin/python3
""" This module defines a function is_same_class """


def is_same_class(obj, a_class):
    """ A function that returns True/False if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise

    """
    return type(obj) is a_class
