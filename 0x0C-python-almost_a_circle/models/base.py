#!/usr/bin/python3
""" This module defines a Base Class """
import json
import csv
import os.path


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to Json Stirng from dictionary """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
