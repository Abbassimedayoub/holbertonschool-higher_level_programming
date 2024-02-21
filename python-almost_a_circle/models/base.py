#!/usr/bin/python3
"""Base Module"""


class Base:
    """Base class for managing ids"""

    __nb_objects = 0  # private class attribute to manage ids

    def __init__(self, id=None):
        """Initialize Base instance with id"""
        if id is not None:  # if id is provided, use it
            self.id = id
        else:
            Base.__nb_objects += 1  # if no id provided, generate a new one
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dictionary to JSON format"""
        if list_dictionaries is None or len(list_dictionaries):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
