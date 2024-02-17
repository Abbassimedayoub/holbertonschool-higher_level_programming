#!/usr/bin/python3
"""
    function that add text at the end of a file
    and return the number of added charcters
"""


def append_write(filename="", text=""):
    """
    @filename: the file to be treated
    @text: the text to be added at the end of the file 
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
