"""he dictionary description with simple data structure
 (list, dictionary, string, integer and boolean) for 
 JSON serialization of an object:"""


def class_to_json(obj):
    """difine class"""
    return obj.__dict__
