#!/usr/bin/python3
"""
Module documentation - returns the JSON representation
"""


def to_json_string(my_obj):
    """
    object representation of json in python

    Args:
        my_obj(any): any object(string) to be listed as JSON

    Return:
        JSON representation of object(string)
    """
    if my_obj is None:
        return
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    elif isinstance(my_obj, str):
        return '"' + my_obj + '"'
    elif isinstance(my_obj, (list, tuple)):
        json_list = [to_json_string(elem) for elem in my_obj]
        return "[" + ", ".join(json_list) + "]"
    elif isinstance(my_obj, dict):
        json_dict = []
        for k, v in my_obj.items():
            json_dict.append(f'"{k}": {to_json_string(v)}')
        return "{" + ", ".join(json_dict) + "}"
    elif isinstance(my_obj, bool):
        return "true" if my_obj else "false"
