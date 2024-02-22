#!/usr/bin/python3
"""Base Module"""
from json import dumps

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
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ that writes the JSON string representation"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)
    @staticmethod
    def from_json_string(json_string):
        """list of dictionaries represented by json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instance with all attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary)
                             for dictionary in dictionaries]
            return instances
        except FileNotFoundError:
            return []
        