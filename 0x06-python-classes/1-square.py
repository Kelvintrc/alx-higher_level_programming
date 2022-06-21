#!/usr/bin/python3
""" this module defines a class Square """


class Square:
    """Class Square that defines a square object.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
