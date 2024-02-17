#!/usr/bin/python3
"""function that retun a load"""
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
