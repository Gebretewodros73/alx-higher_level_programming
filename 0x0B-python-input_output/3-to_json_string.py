#!/usr/bin/python3
"""
Module documentation - a function to return the JSON representation of and object(string)
"""


def to_json_string(my_obj):
    """
    return the JSON representation
    """
    if isinstance(my_obj, (str, int, float, bool)) or my_obj is None:
        return json.dumps(my_obj)
    elif isinstance(my_obj, (list, tuple)):
        return '[' + ', '.join(to_json_string(elem) for elem in my_obj) + ']'
    elif isinstance(my_obj, dict):
        return '{' + ', '.join(f'"{key}": {to_json_string(value)}' for key, value in my_obj.item()) + '}'
    else:
        raise TypeError(f"Object of type '{type(my_obj).__name__}' is not JSON serializable")
