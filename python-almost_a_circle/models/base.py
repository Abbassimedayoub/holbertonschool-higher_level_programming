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
