#!/usr/bin/python3
def lookup(objec):
    """
    Return the list of available attributes and methods of and objects.


    Args:
        objec: The object to lookup.


    Return:
        A list of strings containing the available attributes and methods
    
    for name, value in inspect.getmembers(objec):
        if name.startswith('__') and name.endswith('__'):
            continue
        elif inspect.ismethod(value):
            methods.append(name)
        else:
            attributes.append(name)
    return attributes + methods
    """
    return list(objec.__class__.__dict__)
