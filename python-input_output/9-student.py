#!/usr/bin/python3
"""
Defines a Student class 
"""


class student:
    def __init__(self, first_name, last_name, age):
        """initilize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
