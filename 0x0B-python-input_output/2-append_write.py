#!/usr/bin/python3
""" This module contains a file that appends to a file """


def append_write(filename="", text=""):
    """ Function that appends to a text file

    Args:
        filename: filename
        text: text to append

    Raises:
        Exception: when file cannot be opened

    """

    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
