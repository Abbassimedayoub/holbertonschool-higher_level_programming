#!/usr/bin/python3
"""
     that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """my_obj: the string to be changed to JSON repesentation"""
    return json.dumps(my_obj)
