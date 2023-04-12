#!/usr/bin/python3
"""
Module documentation - returns the JSON representation
"""


def to_json_string(my_obj):
    """
    in python object representation of json
    """
    if my_obj is None:
        return ""
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    elif isinstance(my_obj, str):
        return '"' + my_obj + '"'
    elif isinstance(my_obj, (list, tuple)):
        json_list = [to_json_string(elem) for elem in my_obj]
        return "[" + ", ".join(json_list) + "]"
    elif isinstance(my_obj, dict):
        json_dict = ['"{}": {}'.format(k, to_json_string(v)) for k, v in my_obj.items()]
        return "{" + ", ".join(json_dict) + "}"
    elif isinstance(my_obj, bool):
        return "true" if my_obj else "false"
