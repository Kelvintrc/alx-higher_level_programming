#!/usr/bin/python3
""" This module contains a file that writes to a file """


def write_file(filename="", text=""):
    """ Function that writes to a text file

    Args:
        filename: filename
        text: text to write

    Raises:
        Exception: when file cannot be opened

    """

    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
