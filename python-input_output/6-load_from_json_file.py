#!/usr/bin/python3
"""define function load_from_json_file"""
import json


def load_from_json_file(filename):
    with open(filename, "r") as f:
        return json.load(f)
