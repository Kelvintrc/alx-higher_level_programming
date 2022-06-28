#!/usr/bin/python3
"""

This is a module that contains a class that avoids
dynamically created attributes

"""


class LockedClass:
    """ No class and attributes """
    __slots__ = ["first_name"]

    def __init__(self):
        """ Init Method """
        pass
