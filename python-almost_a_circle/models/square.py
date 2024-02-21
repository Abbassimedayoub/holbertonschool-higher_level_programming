#!/usr/bin/python3
""" Module containing class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance """
        super().__init__(size, size, x, y, id)
        self.size = size
